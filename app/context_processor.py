# context_processors.py

from .models import Project

def projects(request):
    projects_list=[]
    print(request.user)
    if not request.user.is_anonymous:
        user=request.user
        owned=Project.objects.filter(owner=request.user)
        contributed=Project.objects.filter(contributor=request.user)
        for x in owned:
            if not x in projects_list:
                projects_list.append(x)
        for x in contributed:
            if not x in projects_list:
                projects_list.append(x)
        print(projects_list)
        return {'all_projects': projects_list}
    return {'answer':'userdoesnotexist'}