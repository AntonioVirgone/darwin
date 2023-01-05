# Python program to explain os.mkdir() method

# importing os module
import os
import uuid

from directory.models import Directory
from service import Constant


def mapSort(map, reverse):
    def get_name(entity):
        return entity.get('name')

    # sort by name (Ascending order)
    map.sort(key=get_name, reverse=reverse)
    print(map, end='\n\n')
    return map


class DirectoryService:
    @staticmethod
    def getDirectoryList():
        directoryList = os.listdir(path=Constant.PARENT_DIR)

        resultList = []

        for directory in directoryList:
            if directory != ".DS_Store":
                directoryMap = dict()
                directoryMap["name"] = directory
                directoryMap["files"] = DirectoryService.getFileList(directory)

                resultList.append(directoryMap)

        return mapSort(resultList, True)


    @staticmethod
    def getFileList(dirName):
        path = Constant.PARENT_DIR + "/" + dirName
        print(path)

        return os.listdir(path)

    @staticmethod
    def create(dirName):
        list = DirectoryService.getDirectoryList()

        if not list.__contains__(dirName):
            try:
                os.mkdir(Constant.PARENT_DIR + "/" + dirName)
                print("Directory '%s' created" % dirName)

                directoryCode = str(uuid.uuid4())
                directory = Directory(code=directoryCode, name=dirName)
                directory.save()
                return directoryCode

            except (Exception) as error:
                print("Failed to select record from table", error)
            return False

        else:
            return False
