from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, get_object_or_404
from .models import Project


class ProjectList(ListView):
    model = Project

    def get_queryset(self):
        return self.model.objects.filter(status=1)


class ProjectView(DetailView):
    model = Project


class ProjectCreate(SuccessMessageMixin, CreateView):
    model = Project
    fields = ['project', 'description']
    success_url = reverse_lazy('project_list')
    success_message = "%(project)s was created successfully"


class ProjectUpdate(SuccessMessageMixin, UpdateView):
    model = Project
    fields = ['project', 'description']
    success_url = reverse_lazy('project_list')
    success_message = "%(project)s was updated successfully"


class ProjectDelete(SuccessMessageMixin, DeleteView):
    model = Project
    fields = '__all__'
    template_name = 'project/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')


