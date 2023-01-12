from django.shortcuts import render, redirect

from document.forms import PostForm
from project.models import Project
from service.Constant import COMMAND_LIST
from service.DirectoryService import DirectoryService
from service.DocumentService import DocumentService
from .models import Document


def create(request):
    if request.method == "POST":
        DocumentService.create(request.POST)

        return redirect('findAll')
    else:
        projectList = Project.objects.all()
        directoryList = DirectoryService.getDirectoryList()
        return render(request,
                      'manager/document/document_create.html',
                      {
                          'directoryList': directoryList,
                          'projectList': projectList,
                          'commandList': COMMAND_LIST
                      })


# TODO: deprecated
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'manager/document/document_edit.html', {'form': form})


def post_detail(request, pk):
    # for e in Document.objects.all():
    #     print(e.pk)

    if Document.objects.filter(pk=pk):
        doc = Document.objects.get(pk=pk)

    return render(request, 'manager/document/document_detail.html')
