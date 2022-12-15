from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from Todo.forms import TaskCreateForm
from Todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks_list.html"
    context_object_name = "tasks"
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("to_do:tasks")
    template_name = "to_do_form.html"
    form_class = TaskCreateForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do:tasks")
    template_name = "to_do_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do:tasks")
    template_name = "task_confirm_delete.html"


def task_status_change(request, pk):
    task = Task.objects.get(pk=pk)
    if task.is_done is False:
        task.is_done = True
    else:
        task.is_done = False
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
