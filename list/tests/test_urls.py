from django.test import SimpleTestCase
from django.urls import reverse ,resolve , path,include
from ..api.views import TODOList
from rest_framework.test import APIClient , APITestCase ,APIRequestFactory ,URLPatternsTestCase
from  rest_framework import status
from ..api.urls import get_post_tasks
class TestURLList(SimpleTestCase):

    # def test_viewsets(self):
    #     url = reverse('todo_tasks')
    #     self.assertEquals(resolve(url),TODOList)
    def test_list_GET(self):
        url = reverse('tasks')
        self.assertEquals(resolve(url).func,get_post_tasks)

    # def test_task_POST(self):
    #     url = reverse('single_task')
    #     self.assertEquals(resolve(url).func.view_class,get_update_delete_task)