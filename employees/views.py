from django.shortcuts import render, redirect

from employees.forms import EmployeeAssignProjectForm, EmployeeCreateForm, User

from .models import Employee

from .decorators import manager_login_required


@manager_login_required
def employee_list_view(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'employees/employee_list.html', context=context)


@manager_login_required
def employee_detail_view(request, pk):
    employee = Employee.objects.get(id=pk)
    context = {'employee': employee}
    return render(request, 'employees/employee_detail.html', context=context)


@manager_login_required
def employee_create_view(request):
    form = EmployeeCreateForm()
    if(request.method == 'POST'):
        form = EmployeeCreateForm(request.POST)
        if form.is_valid():
            form = form.save()
            Employee.objects.create(user=form, manager=request.user)
            return redirect('employees:list')
    context = {'form': form}
    return render(request, 'employees/employee_create.html', context=context)


@manager_login_required
def employee_delete_view(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.user.delete()
        employee.delete()
        return redirect('employees:list')
    context = {'employee': employee}
    return render(request, 'employees/employee_delete.html', context=context)


@manager_login_required
def employee_assign_project(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeAssignProjectForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeAssignProjectForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees:detail', pk)
    context = {'form': form, 'employee': employee}
    return render(request, 'employees/employee_assign_project.html', context=context)


# def employee_update_view(request, pk):
#     employee = employee.objects.get(id=pk)
#     form = employeeCreateForm(instance=employee)
#     if(request.method == 'POST'):
#         form = employeeCreateForm(request.POST, instance=employee)
#         if form.is_valid():
#             form.save()
    #         return redirect('employees:detail', pk)
    # context = {'form': form, 'employee': employee}
    # return render(request, 'employees/employee_update.html', context=context)
