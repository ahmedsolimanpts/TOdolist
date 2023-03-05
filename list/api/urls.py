from django.urls import path ,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list',TODOList,basename='todo_list')

urlpatterns = [
 path('',include(router.urls)),
]