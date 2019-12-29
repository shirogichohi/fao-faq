from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, get_object_or_404
from .models import Issue


class IssueList(ListView):
    model = Issue

    def get_queryset(self):
        return self.model.objects.filter(status=1)


class IssueView(DetailView):
    model = Issue


class IssueCreate(SuccessMessageMixin, CreateView):
    model = Issue
    fields = ['project','question','answer']
    success_url = reverse_lazy('issue_list')
    success_message = "%(question)s was created successfully"


class IssueUpdate(SuccessMessageMixin, UpdateView):
    model = Issue
    fields = ['question','answer']
    success_url = reverse_lazy('issue_list')
    success_message = "%(question) was updated successfully"


class IssueDelete(SuccessMessageMixin, UpdateView):
    model = Issue
    fields = ['status']
    template_name = 'Issue/issue_confirm_delete.html'
    success_url = reverse_lazy('Issue_list')


class SearchResultsView(ListView):
    model = Issue
    template_name = 'Issue/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Issue.objects.filter(
            Q(question__icontains=query) | Q(answer__icontains=query)
        )
        return object_list
