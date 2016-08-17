class RequestList():
  """Module to fetch and filter request"""
  max_per_page = 100

  def current_page(self, query = False):
    try:
      current_page = int(query.get('page', 1))
      return (1, current_page)[current_page > 1]
    except:
      return 1

  def per_page(self, query = False):
    try:
      per_page = int(query.get('per_page', 10))
      if per_page > self.max_per_page:
        per_page = self.max_per_page
      return (1, per_page)[per_page > 1]
    except:
      return 10

  def start_at(self):
    return 0
