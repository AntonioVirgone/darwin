import json

from django.shortcuts import render, redirect

from service.DirectoryService import DirectoryService
from service.model.DirectoryViewModel import DirectoryViewModel, DirectoryViewModelEncoder


def create(request):
    if request.method == "POST":
        dirName = request.POST.get("dirName")
        code = DirectoryService.create(dirName)

        if code:
            json_str = json.dumps(DirectoryViewModel(directoryCode=code, directoryName=dirName),
                                  cls=DirectoryViewModelEncoder)
            print(json_str)
        else:
            print("Creazione cartella %s fallita" % dirName)

        return redirect('findAll')
    else:
        return render(request, 'manager/directory_create.html')


def findAll(request):
    directoryList = DirectoryService.getDirectoryList()

    list = []

    for directory in directoryList:
        if directory != ".DS_Store":
            dir = dict()
            dir["name"] = directory
            dir["files"] = DirectoryService.getFileList(directory)

            list.append(dir)

    print(list)

    return render(request, 'manager/directory.html', {'directoryList': list, 'countDirectories': len(directoryList)})
