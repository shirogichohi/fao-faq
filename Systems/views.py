from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, get_object_or_404
from .models import System


class SystemList(ListView):
    model = System

    def get_queryset(self):
        return self.model.objects.filter(status=1)


class SystemView(DetailView):
    model = System


class SystemCreate(SuccessMessageMixin, CreateView):
    model = System
    fields = ['project','description' ]
    success_url = reverse_lazy('system_list')
    success_message = "%(system)s was created successfully"


class SystemUpdate(SuccessMessageMixin, UpdateView):
    model = System
    fields = ['system']
    success_url = reverse_lazy('system_list')
    success_message = "%(system)s was updated successfully"


class SystemDelete(SuccessMessageMixin, DeleteView):
    model = System
    fields = '__all__'
    template_name = 'system/system_confirm_delete.html'
    success_url = reverse_lazy('system_list')


