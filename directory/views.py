import json

from django.http import HttpResponse
from django.shortcuts import render

from service.DirectoryService import DirectoryService
from service.model.DirectoryViewModel import DirectoryViewModel, DirectoryViewModelEncoder


def create(request):
    dirName = request.GET.get("dirName")
    code = DirectoryService.create(dirName)

    if code:
        json_str = json.dumps(DirectoryViewModel(directoryCode=code, directoryName=dirName), cls=DirectoryViewModelEncoder)

        print(json_str)
        return HttpResponse(
            json_str,
            content_type="application/json")
    else:
        return HttpResponse("Creazione cartella %s fallita" % dirName)


def findAll(request):
    directoryList = DirectoryService.getDirectoryList()

    list = []

    for directory in directoryList:
        dir = dict()
        dir["name"] = directory
        dir["files"] = DirectoryService.getFileList(directory)

        list.append(dir)

    print(list)

    return render(request, 'manager/directory.html', {'directoryList': list, 'countDirectories': len(directoryList)})
