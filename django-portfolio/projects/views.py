from django.shortcuts import render
from projects.models import Project
#from django.http import HttpResponse

# Create your views here.
def project_list(request):
    #return HttpResponse("<h1>Hello everyone!</h1>")
    return render(request, 'projects/index.html ')


def all_projects(request):
    #query the db to return all project objects
    projects = Project.objects.all()
    #print(projects)
    return render(request, 'projects/all_projects.html', {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html',
                  {'project':project})