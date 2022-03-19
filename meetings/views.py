from django.shortcuts import render, redirect
from employees.models import Employee
from meetings.forms import CreateMeetingForm
from .models import Meeting
from employees.decorators import manager_login_required
from django.contrib.auth.decorators import login_required

@manager_login_required
def create(request):
    form = CreateMeetingForm()
    if request.method == 'POST':
        form = CreateMeetingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user
            form.save()
            return redirect('meetings:list')
    return render(request, 'meetings/create.html', {'form':form})

@manager_login_required
def delete(request, pk):
    meeting = Meeting.objects.get(id=pk)
    if request.method == 'POST':
        meeting.delete()
        return redirect('meetings:list')
    context = {'meeting': meeting}
    return render(request, 'meetings/delete.html', context=context)

@login_required
def detail(request, id):
    meeting = Meeting.objects.get(id=id)
    context = {'meeting': meeting}
    return render(request, 'meetings/details.html', context=context)

@login_required
def list(request):
    if request.user.is_manager:
        meetings = Meeting.objects.filter(host=request.user)
    else:
        employee = Employee.objects.get(user=request.user)
        meetings = Meeting.objects.filter(employee=employee)
    return render(request, 'meetings/list.html', {'meetings': meetings})