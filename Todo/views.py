from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from Todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks_list.html"
    context_object_name = "tasks"
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do:task")
    template_name = "to_do_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do:task")
    template_name = "to_do_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do:task")
    template_name = "task_confirm_delete.html"


def task_status_change(request, pk):
    task = Task.objects.get(pk=pk)
    if task.progres is False:
        task.progres = True
    else:
        task.progres = False
    task.save()
    return HttpResponseRedirect(reverse_lazy("to_do:tasks"))


class TagsListView(generic.ListView):
    model = Tag
    template_name = "tags_list.html"
    context_object_name = "tags"
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tags")
    template_name = "tags_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tags")
    template_name = "tags_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do:tags")
    template_name = "tag_confirm_delete.html"
