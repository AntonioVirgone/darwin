from django.shortcuts import render, redirect

from project.models import Project


# Create your views here.
def create(request):
    if request.method == "POST":
        projectName = request.POST.get("projectName")
        kProjectName = request.POST.get("KProjectName")
        dokerImageName = request.POST.get("dokerImageName")
        gkeServiceName = request.POST.get("gkeServiceName")

        project = Project(projectName=projectName,
                          kProjectName=kProjectName,
                          dokerImageName=dokerImageName,
                          gkeServiceName=gkeServiceName)
        project.save()

        return findAll(request)
    else:
        return render(request, 'manager/project/project_create.html')


def findBy(request, pk):
    if Project.objects.filter(pk=pk):
        doc = Project.objects.get(pk=pk)

    return render(request, 'manager/document/document_detail.html')


def findAll(request):
    projectList = Project.objects.all()
    return render(request, 'manager/project/project_list.html', {'projectList': projectList})


def delete(request, pk):
    if Project.objects.filter(pk=pk):
        doc = Project.objects.get(pk=pk)
        Project.delete(doc)
    else:
        print("Project not found")

    return findAll(request)
