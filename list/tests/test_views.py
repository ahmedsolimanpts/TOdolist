from django.test import Client, TestCase
from django.urls import reverse,resolve
from ..models import Tasks
from rest_framework import status
class TestList(TestCase):
    def setUp(self):
        self.client = Client()
        self.get_tasks_url = 'task-list'
        self.get_specific_task_url = 'task-detail'
        self.post_task_url = 'task-list'
        self.put_specific_task_url    = 'task-detail'
        self.delete_specific_task_url = 'task-detail'
        self.data = {
        "description": "not me",
        "status": "Done",
        "name": "xxxx",
        "day": "2020-01-01",
        # "user_id":1
        }
    def test_task_GET(self):
        url = reverse(self.get_tasks_url)
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    def test_GET_specific_task(self):
        Tasks.objects.create(**self.data)
        url = reverse(self.get_specific_task_url,kwargs={"pk":1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,status.HTTP_200_OK)

    def test_POST_new_task(self):
        url = reverse(self.post_task_url)
        response = self.client.post(url,self.data)
        self.assertEquals(response.status_code,status.HTTP_201_CREATED)

    def test_DELETE_specific_task(self):
        Tasks.objects.create(**self.data)
        url = reverse(self.delete_specific_task_url,kwargs={"pk":1})
        response = self.client.delete(url,self.data)
        self.assertEquals(response.status_code,status.HTTP_200_OK)
    def test_UPDATE_specific_task(self):
        Tasks.objects.create(**self.data)
        url = reverse(self.put_specific_task_url,kwargs={"pk":1})
        new_data = {
        "description": "not me",
        "day": "2020-01-01",
        }
        response = self.client.put(url,new_data)
        self.assertEquals(response.status_code,status.HTTP_200_OK)
