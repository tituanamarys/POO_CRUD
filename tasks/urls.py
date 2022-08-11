from asyncio import tasks
from django.urls import path
from .views import list_tasks,create_tasks,delete_tasks
from .views import update_tasks,inicio,about,list_tasks
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', inicio, name='index'),
    path('about', about, name='about'),
    path('list_tasks', list_tasks, name='list_tasks'),
    # path('',list_tasks),
    path('create_tasks/',create_tasks,name='create_tasks') , #/tasks/create/usercliente/
    path('delete_tasks/<int:task_id>/',delete_tasks,name='delete_task'),
    path('update_tasks/',update_tasks,name='update_task'),
   # path('eliminar_tasks/<int:task_id>',delete_tasks,name='delete_task'),
    path('update_tasks/<int:task_id>',update_tasks,name='update_task'),
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
