from django.shortcuts import redirect, render

from projects.forms import ProjectCreateForm

from django.contrib.auth.decorators import login_required

from .models import Project

from employees.decorators import manager_login_required
from employees.models import Employee


@login_required
def project_list_view(request):
    projects = Project.objects.all()
    if request.user.is_employee:
        employee = Employee.objects.get(user__id=request.user.id)
        projects = employee.project
    context = {'projects': projects}
    return render(request, 'projects/project_list.html', context=context)


@login_required
def project_detail_view(request, pk):
    project = Project.objects.get(id=pk)
    employees = Employee.objects.filter(project=project)
    context = {'project': project, 'employees': employees}
    return render(request, 'projects/project_detail.html', context=context)


@manager_login_required
def project_create_view(request):
    form = ProjectCreateForm()
    if(request.method == 'POST'):
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.manager = request.user
            form.save()
            return redirect('projects:list')
    context = {'form': form}
    return render(request, 'projects/project_create.html', context=context)


@manager_login_required
def project_delete_view(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:list')
    context = {'project': project}
    return render(request, 'projects/project_delete.html', context=context)


@manager_login_required
def project_update_view(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectCreateForm(instance=project)
    if(request.method == 'POST'):
        form = ProjectCreateForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:detail', pk)
    context = {'form': form, 'project': project}
    return render(request, 'projects/project_update.html', context=context)
