import sys
sys.path.append("..")

from django.test import TestCase
from django.test import tag
from django.http.request import QueryDict
from api.request_list_controller import RequestListController

class RequestListControllerTestCase(TestCase):
  def setUp(self):
    self.subject = RequestListController()

  @tag('core')
  def test_respond_current_page(self):
    methods = [method for method in dir(self.subject) if method == '_current_page']
    self.assertEqual(1, len(methods))

  @tag('core')
  def test_current_page_retrieve_one_if_not_defined(self):
    self.assertEqual(1, self.subject._current_page())

  @tag('core')
  def test_current_page_retrieve_one_if_not_defined_params(self):
    self.assertEqual(1, self.subject._current_page(QueryDict()))

  @tag('core')
  def test_current_page_retrieve_one_if_invalid_data(self):
    self.assertEqual(1, self.subject._current_page(QueryDict('page=my-page')))

  @tag('core')
  def test_current_page_retrieve_value_if_defined(self):
    self.assertEqual(5, self.subject._current_page(QueryDict('page=5')))

  @tag('core')
  def test_current_page_retrieve_one_if_negative_number(self):
    self.assertEqual(1, self.subject._current_page(QueryDict('page=-5')))

  @tag('core')
  def test_respond_per_page(self):
    methods = [method for method in dir(self.subject) if method == '_per_page']
    self.assertEqual(1, len(methods))

  @tag('core')
  def test_per_page_respond_ten_as_default(self):
    self.assertEqual(10, self.subject._per_page())

  @tag('core')
  def test_per_page_respond_scoped_by_default_per_page(self):
    self.subject.default_per_page = 15
    self.assertEqual(15, self.subject._per_page())

  @tag('core')
  def test_per_page_respond_value_when_passed(self):
    self.assertEqual(50, self.subject._per_page(QueryDict('per_page=50')))

  @tag('core')
  def test_per_page_respond_one_if_passed_minor_value(self):
    self.assertEqual(1, self.subject._per_page(QueryDict('per_page=-2')))

  @tag('core')
  def test_per_page_respond_maximun_to_hunred_value(self):
    self.assertEqual(100, self.subject._per_page(QueryDict('per_page=101')))

  @tag('core')
  def test_per_page_respond_maximun_can_be_setted(self):
    self.subject.max_per_page = 200
    self.assertEqual(200, self.subject._per_page(QueryDict('per_page=201')))

  @tag('core')
  def test_start_at_default_is_zero(self):
    self.assertEqual(0, self.subject._start_at())

  @tag('core')
  def test_start_at_must_be_ten_when_page_is_two(self):
    self.assertEqual(10, self.subject._start_at(2))

  @tag('core')
  def test_start_at_must_be_twenty_when_page_is_three(self):
    self.assertEqual(20, self.subject._start_at(3))

  @tag('core')
  def test_start_at_can_recive_per_page_value(self):
    self.assertEqual(0, self.subject._start_at(1, 15))
    self.assertEqual(15, self.subject._start_at(2, 15))
    self.assertEqual(30, self.subject._start_at(3, 15))

  @tag('core')
  def test_start_at_uses_per_page_attribute(self):
    self.subject.default_per_page = 25
    self.assertEqual(0, self.subject._start_at(1))
    self.assertEqual(25, self.subject._start_at(2))
    self.assertEqual(50, self.subject._start_at(3))

  @tag('core')
  def test_pagination_args_default_values(self):
    per_page, current_page, start_at = self.subject._pagination_args()
    self.assertEqual(10, per_page)
    self.assertEqual(1, current_page)
    self.assertEqual(0, start_at)

  @tag('core')
  def test_pagination_accept_page_query(self):
    query = QueryDict('page=3')
    self.assertEqual((10, 3, 20), self.subject._pagination_args(query))

  @tag('core')
  def test_pagination_accept_per_page_query(self):
    query = QueryDict('page=4&per_page=20')
    self.assertEqual((20, 4, 60), self.subject._pagination_args(query))

  @tag('core')
  def test_pagination_accept_default_per_page(self):
    self.subject.default_per_page = 15
    query = QueryDict('page=2')
    self.assertEqual((15, 2, 15), self.subject._pagination_args(query))
