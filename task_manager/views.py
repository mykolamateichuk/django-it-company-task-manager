import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import TaskForm, RegisterWorkerForm, WorkerUpdateForm
from task_manager.models import Task, Worker, Position


@login_required
def index(request: HttpRequest) -> HttpResponse:
    user_tasks = Task.objects.filter(
        assignees__username=request.user.username
    )

    context = {
        "tasks": user_tasks,
        "due_tasks": user_tasks.filter(is_completed=False).count()
    }

    return render(request,
                  "task_manager/index.html",
                  context=context)


@login_required
def task_update_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)

    task.is_completed = True
    task.save()

    return redirect(reverse_lazy("task_manager:index"), args=(pk,))


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:index")


@login_required
def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    current_date = datetime.date.today()
    next_date = current_date + datetime.timedelta(days=1)

    context = {
        "task": task,
        "current_date": current_date,
        "next_date": next_date
    }

    return render(request,
                  "task_manager/task_detail.html",
                  context=context)


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = Task.objects.all().prefetch_related("assignees", "task_type")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:index")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:index")


class WorkerCreateForm:
    pass


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = RegisterWorkerForm
    success_url = reverse_lazy("task_manager:index")

    def form_valid(self, form):
        form.save()

        username = self.request.POST["username"]
        password = self.request.POST["password1"]

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return redirect(reverse_lazy("task_manager:index"))


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    fields = "__all__"
    queryset = Worker.objects.select_related("position")


def worker_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    worker = Worker.objects.select_related("position").get(pk=pk)
    tasks_due = Task.objects.filter(
        assignees__username=worker.username
    ).filter(is_completed=False).count()

    context = {
        "worker": worker,
        "tasks_due": tasks_due
    }

    return render(request,
                  "task_manager/worker_detail.html",
                  context=context)


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    template_name = "task_manager/worker_update_form.html"
    success_url = reverse_lazy("task_manager:index")
