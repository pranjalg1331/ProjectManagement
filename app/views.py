from django.http import JsonResponse
from django.shortcuts import render,redirect
from . import models,forms
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request,project_id):

    project=models.Project.objects.get(id=project_id)
    tasks=models.Tasks.objects.filter(project=project)
    
    return render(request,"index.html",{"project":project,"tasks":tasks})

def mytask(request):
    user=request.user
    tasks = models.Tasks.objects.filter(assigned=user)
    print(tasks)
    return render(request,"task.html",{"tasks":tasks})

def project(request):
    projects_list=[]
    user=request.user
    owned=models.Project.objects.filter(owner=request.user)
    contributed=models.Project.objects.filter(contributor=request.user)
    for x in owned:
        if not x in projects_list:
            projects_list.append(x)
    for x in contributed:
        if not x in projects_list:
            projects_list.append(x)
    print(projects_list)
        
    return render(request,"projects.html",{'user': user,"projects":projects_list})

def addproject(request):
    
    if request.method=="GET":
        form=forms.ProjectForm()
        return render(request,"addproject.html", {'form': form})
    
    elif request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a relevant page, such as the project detail page
            return redirect('projects') 
        return render(request,"addproject.html", {'form': form})
    
    
def addtask(request,project_id):
    
    if request.method=="GET":
        form=forms.TaskForm()
        return render(request,"addtask.html", {'form': form})
    
    elif request.method == 'POST':
        project=models.Project.objects.get(id=project_id)
        form = forms.TaskForm(request.POST)
        print(form.data)
        if form.is_valid():
            task=form.save(commit=False)
            task.project=project
            task.save()
            form.save_m2m()
            # Redirect to a relevant page, such as the project detail page
            return redirect('project_detail',project_id=project_id) 
        print(form.errors)
        return render(request,"addtask.html", {'form': form})
    

def mark_task_completed(task_id):
    try:
        task = models.Tasks.objects.get(id=task_id)
        if task.status == 'Pending':
            task.status = 'Completed'
            task.save()
            return True
        else:
            return False  # Task is not pending
    except models.Tasks.DoesNotExist:
        return False  # Task does not exist
    
@csrf_exempt    
def mark_task_completed_view(request):
    if request.method == 'POST':
        print("hi")
        task_id = request.POST.get('task_id')
        success = mark_task_completed(task_id)
        print(success)
        if success:
            print("success")
            return JsonResponse({'success': success})
    return JsonResponse({'success': False})


def mark_task_incompleted(task_id):
    try:
        task = models.Tasks.objects.get(id=task_id)
        if task.status == 'Completed':
            task.status = 'Pending'
            task.save()
            return True
        else:
            return False  # Task is not pending
    except models.Tasks.DoesNotExist:
        return False  # Task does not exist
    
@csrf_exempt    
def mark_task_incompleted_view(request):
    if request.method == 'POST':
        print("hi")
        task_id = request.POST.get('task_id')
        success = mark_task_incompleted(task_id)
        print(success)
        if success:
            print("success")
            return JsonResponse({'success': success})
    return JsonResponse({'success': False})


@csrf_exempt    
def deleteTask(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task=models.Tasks.objects.get(id=task_id)
        task.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
