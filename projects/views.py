from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/projects.html", context)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        "project": project,
    }
    return render(request, "projects/project_detail.html", context)


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            print(request.POST["tags"])
            print(request.POST)
            project.save()
            return redirect("projects")

    context = {
        "form": form
    }
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        "form": form
    }
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect("projects")

    context = {
        "object": project
    }
    return render(request, "projects/project_delete.html", context)
