from django.urls import path ,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('task',TODOList,basename="menu")

get_post_tasks = TODOList.as_view({'get':'list','post':'create'})

urlpatterns = [
 path('',include(router.urls),name='todo_tasks'),
 path('single_task/',get_post_tasks,name='tasks'),
]