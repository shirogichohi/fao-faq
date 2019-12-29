from django.urls import path

from . import views

urlpatterns = [
    path('', views.SystemList.as_view(), name='system_list'),
    path('new', views.SystemCreate.as_view(), name='system_new'),
    path('view/<int:pk>', views.SystemView.as_view(), name='system_view'),
    path('edit/<int:pk>', views.SystemUpdate.as_view(), name='system_edit'),
    path('delete/<int:pk>', views.SystemDelete.as_view(), name='system_delete'),
]