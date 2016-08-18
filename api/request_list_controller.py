class RequestListController():
  """Module to fetch and filter request"""
  max_per_page = 100
  default_per_page = 10

  def current_page(self, query = False):
    try:
      current_page = int(query.get('page', 1))
      return (1, current_page)[current_page > 1]
    except:
      return 1

  def per_page(self, query = False):
    try:
      per_page = int(query.get('per_page', self.default_per_page))
      if per_page > self.max_per_page:
        per_page = self.max_per_page
      return (1, per_page)[per_page > 1]
    except:
      return self.default_per_page

  def start_at(self, current_page = 1, per_page = False):
    if not per_page:
      per_page = self.default_per_page
    return (current_page - 1) * per_page

  def pagination_args(self, query = False):
    per_page = self.per_page(query)
    current_page = self.current_page(query)
    start_at = self.start_at(current_page, per_page)
    return (per_page, current_page, start_at)
