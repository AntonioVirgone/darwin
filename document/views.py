import json

from django.shortcuts import render, redirect

from document.forms import PostForm
from service.DocumentService import DocumentService
from .models import Document


def create(request):
    if request.method == "POST":
        projectName = request.POST.get("projectName")
        directoryName = request.POST.get("directoryName")
        fileName = request.POST.get("fileName")
        serviceName = request.POST.get("serviceName")
        serviceVersion = request.POST.get("serviceVersion")
        gkeServiceName = request.POST.get("gkeServiceName")
        commandList = [request.POST.get("command1"), request.POST.get("command2"), request.POST.get("command3")]

        document = Document(projectName=projectName,
                            directoryName=directoryName,
                            fileName=fileName,
                            serviceName=serviceName,
                            serviceVersion=serviceVersion,
                            gkeServiceName=gkeServiceName,
                            commandList=json.dumps(commandList))
        print(document)

        DocumentService.create(document)

        return redirect('findAll')
    else:
        return render(request, 'manager/document_create.html')


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print(str(form))
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'manager/document_edit.html', {'form': form})


def post_detail(request, pk):
    # for e in Document.objects.all():
    #     print(e.pk)

    if Document.objects.filter(pk=pk):
        doc = Document.objects.get(pk=pk)
        print(doc)

    return render(request, 'manager/document_detail.html')
