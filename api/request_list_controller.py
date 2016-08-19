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
    per_page, current_page, start = self._pagination_args(request.GET)

    paginator = Paginator(queryset_filtered, per_page)

    try:
      page = paginator.page(current_page)
    except EmptyPage:
      page = paginator.page(paginator.num_pages)

    result_page = page.object_list
    total = paginator.count
    num_pages = paginator.num_pages
    hal_objects = [obj.to_json_hal() for obj in result_page]

    page_range = []

    start = 0 if page.number - self.offset < 0 else page.number - self.offset
    end = page.number + self.offset

    for p in paginator.page_range[start:end]:
      query_page = query_filters.copy()
      query_page.update({ "page": p })
      query_page.update({ "per_page": paginator.per_page })
      page_range.append({
        "page": p,
        "current": page.number == p,
        "filter_args": query_page.urlencode()
      })

    objects = {
      "total": total,
      "num_pages": num_pages,
      "per_page": per_page,
      "current_page": page.number,
      "pages": {
        "range": page_range
      },
      "_embedded": { self.resource_type: hal_objects },
      "_links": self._links(),
    }

    return JsonResponse(objects)

  def _apply_permitted_filters(self, queryset, querydict):
    query_filters = QueryDict(mutable=True)

    for permited_filter in self.permited_filters:
      if not permited_filter in querydict:
        continue
      for filter_item in querydict.getlist(permited_filter):
        query_filters.update({permited_filter: filter_item})
        queryset = queryset.filter(**{ permited_filter: filter_item })

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

  def _start_at(self, current_page = 1, per_page = False):
    """Calculate start index based on page and per page information"""
    if not per_page:
      per_page = self.default_per_page
    return (current_page - 1) * per_page

  def _pagination_args(self, query = False):
    """Retrieves information for paginate items in models"""
    per_page = self._per_page(query)
    current_page = self._current_page(query)
    start_at = self._start_at(current_page, per_page)
    return (per_page, current_page, start_at)
