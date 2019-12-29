from django.conf.urls.static import static
from django.urls import path

from FAQ import settings
from . import views

urlpatterns = [
    path('', views.IssueList.as_view(), name='issue_list'),
    path('search', views.SearchResultsView.as_view(), name='search_results'),
    path('new', views.IssueCreate.as_view(), name='issue_new'),
    path('view/<int:pk>', views.IssueView.as_view(), name='issue_view'),
    path('edit/<int:pk>', views.IssueUpdate.as_view(), name='issue_edit'),
    path('delete/<int:pk>', views.IssueDelete.as_view(), name='issue_delete'),
]
