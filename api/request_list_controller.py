from django.http import JsonResponse

class RequestListController():
  """Module to fetch and filter request"""
  max_per_page = 100
  default_per_page = 10

  def get(self, request):
    per_page, current_page, start = self._pagination_args(request.GET)
    queryset_filtered = self._filter(self.queryset, request.GET)

    total = queryset_filtered.count()
    result_page = queryset_filtered[start:start+per_page]
    pages = math.ceil(total / per_page)
    hal_objects = [obj.to_json_hal() for obj in result_page]

    objects = {
      "total": total,
      "pages": pages,
      "per_page": per_page,
      "current_page": current_page,
      "_embedded": { self.resource_type: hal_objects },
      "_links": self._links(),
    }

    return JsonResponse(objects)

  def _filter(self, queryset, querydict):
    """This method can be redefined with intuit do filter data"""
    # TODO: apply filters based on _filters attribute
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
