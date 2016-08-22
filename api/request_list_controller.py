from django.http import JsonResponse
from django.http.request import QueryDict
from django.core.paginator import Paginator, EmptyPage

class RequestListController():
  """Module to fetch and filter request"""
  max_per_page = 100
  default_per_page = 10
  offset = 5
  permited_filters = []

  def get(self, request):
    query_set = self._apply_permitted_filters(self.queryset, request.GET)
    queryset_filtered, query_filters = self._filter(query_set, request.GET)
    per_page, current_page = self._pagination_args(request.GET)

    paginator = Paginator(queryset_filtered, per_page)
    page = self._fetch_page(paginator, current_page)
    hal_objects = [obj.to_json_hal() for obj in page.object_list]

    page_links = self._page_links(page, query_filters, self.offset)

    params = []
    for param in request.GET.lists():
      if len(param[1]) > 1:
        params.append(param)
      else:
        params.append([param[0], param[1][0]])

    return JsonResponse({
      "total": paginator.count,
      "num_pages": paginator.num_pages,
      "per_page": per_page,
      "current_page": page.number,
      "has_other_pages": page.has_other_pages(),
      "params": params,
      "_embedded": {
        self.resource_type: hal_objects,
        "pages": page_links
      },
      "_links": self._links(),
    })

  def _page_links(self, page, query_filters, offset):
    next_page = False
    previous_page = False

    if page.has_previous():
      previous_page = self._page_link(page.number - 1, page, query_filters)
    if page.has_next():
      next_page = self._page_link(page.number + 1, page, query_filters)

    page_range = self._page_range_links(page, query_filters, offset)
    last_page = self._page_link(page.paginator.num_pages, page, query_filters)
    first_page = self._page_link(1, page, query_filters)

    return {
      "first_page": first_page,
      "previous_page": previous_page,
      "next_page": next_page,
      "last_page": last_page,
      "page_range": page_range
    }

  def _page_range_links(self, page, query_filters, offset):
    return [
      self._page_link(p, page, query_filters)
      for p in self._page_range(page, offset)
    ]

  def _page_range(self, page, offset):
    if page.number - offset < 0: start = 0
    else: start = page.number - offset
    end = page.number + offset
    return page.paginator.page_range[start:end]

  def _page_link(self, p, page, query_filters):
    query_page = query_filters.copy()
    query_page.update({ "page": p })
    query_page.update({ "per_page": page.paginator.per_page })
    return {
      "page": p,
      "current": page.number == p,
      "filter_args": query_page.urlencode()
    }

  def _fetch_page(self, paginator, current_page):
    try:
      return paginator.page(current_page)
    except EmptyPage:
      return paginator.page(paginator.num_pages)

  def _apply_permitted_filters(self, queryset, querydict):
    query_filters = QueryDict(mutable=True)
    for permited_filter in self.permited_filters:
      if not permited_filter in querydict:
        continue
      for filter_item in querydict.getlist(permited_filter):
        try:
          queryset = queryset.filter(**{ permited_filter: filter_item })
          query_filters.update({permited_filter: filter_item})
        except:
          pass
    return (queryset, query_filters)

  def _filter(self, queryset, querydict):
    """This method can be redefined with intuit do filter data"""
    return queryset

  def _current_page(self, query = False):
    """Fetchs current page based on QueryDict.get('page') information"""
    try:
      current_page = int(query.get('page', 1))
      return (1, current_page)[current_page > 1]
    except:
      return 1

  def _per_page(self, query = False):
    """Fetchs quantity items per page based on QueryDict.get('per_page') information"""
    try:
      per_page = int(query.get('per_page', self.default_per_page))
      if per_page > self.max_per_page:
        per_page = self.max_per_page
      return (1, per_page)[per_page > 1]
    except:
      return self.default_per_page

  def _pagination_args(self, query = False):
    """Retrieves information for paginate items in models"""
    per_page = self._per_page(query)
    current_page = self._current_page(query)
    return (per_page, current_page)
