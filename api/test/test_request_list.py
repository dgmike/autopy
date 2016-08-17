import sys
sys.path.append("..")

from django.test import TestCase
from django.test import tag
from django.http.request import QueryDict
from api.request_list import RequestList

class RequestListTestCase(TestCase):
  def setUp(self):
    self.subject = RequestList()

  @tag('core')
  def test_respond_current_page(self):
    methods = [method for method in dir(self.subject) if method == 'current_page']
    self.assertEqual(1, len(methods))

  @tag('core')
  def test_current_page_retrieve_one_if_not_defined(self):
    self.assertEqual(1, self.subject.current_page())

  @tag('core')
  def test_current_page_retrieve_one_if_not_defined_params(self):
    self.assertEqual(1, self.subject.current_page(QueryDict()))

  @tag('core')
  def test_current_page_retrieve_one_if_invalid_data(self):
    self.assertEqual(1, self.subject.current_page(QueryDict('page=my-page')))

  @tag('core')
  def test_current_page_retrieve_value_if_defined(self):
    self.assertEqual(5, self.subject.current_page(QueryDict('page=5')))

  @tag('core')
  def test_current_page_retrieve_one_if_negative_number(self):
    self.assertEqual(1, self.subject.current_page(QueryDict('page=-5')))

  @tag('core')
  def test_respond_per_page(self):
    methods = [method for method in dir(self.subject) if method == 'per_page']
    self.assertEqual(1, len(methods))

  @tag('core')
  def test_per_page_respond_ten_as_default(self):
    self.assertEqual(10, self.subject.per_page())

  @tag('core')
  def test_per_page_respond_value_when_passed(self):
    self.assertEqual(50, self.subject.per_page(QueryDict('per_page=50')))

  @tag('core')
  def test_per_page_respond_one_if_passed_minor_value(self):
    self.assertEqual(1, self.subject.per_page(QueryDict('per_page=-2')))

  @tag('core')
  def test_per_page_respond_maximun_to_hunred_value(self):
    self.assertEqual(100, self.subject.per_page(QueryDict('per_page=101')))

  @tag('core')
  def test_per_page_respond_maximun_can_be_setted(self):
    self.subject.max_per_page = 200
    self.assertEqual(200, self.subject.per_page(QueryDict('per_page=201')))

  @tag('core')
  def start_at(self):
    self.assertEqual(0, self.subject.start_at())
