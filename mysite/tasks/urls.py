from django.urls import path, re_path
import views

app_name = 'tasks'

urlpatterns = [
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('', views.TaskListView.as_view(), name='task_list'),
    re_path(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='task_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name='task_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete'),

    # path('create/', views.task_create, name='task_create'),
    # path('', views.task_list, name='task_list'),
    # re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    # re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
]
