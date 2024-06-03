from django.urls import path
from .views import index,mytask,addtask,project,addproject,mark_task_completed_view,mark_task_incompleted_view,deleteTask



urlpatterns = [
    
    path('index/<int:project_id>/', index, name='project_detail'),
    path('mytask/',mytask,name='mytask'),
    path('index/<int:project_id>/addtask/',addtask,name='addtask'),
    path('project/',project,name='projects'),
    path('project/addproject/',addproject,name='addprojects'),
    path('mark_task_completed/', mark_task_completed_view, name='mark_task_completed'),
    path('mark_task_incompleted/', mark_task_incompleted_view, name='mark_task_incompleted'),
    path('deleteTask/',deleteTask, name='deleteTask'),
    
]