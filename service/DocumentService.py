import json

from django.core import serializers

from document.models import Document
from project.models import Project
from service import CreateDocumentService
from service.DirectoryService import DirectoryService


def jsonSerializer(articles):
    return serializers.serialize("json", articles)


class DocumentService:

    @staticmethod
    def fileNameGenerator(directoryName, kProjectName, projectName):
        files = []
        directoryList = DirectoryService.getDirectoryList()

        documentList = filter(lambda directory: directory['name'] == directoryName, directoryList)

        for document in documentList:
            files = filter(lambda file: file[0:3] == kProjectName, document['files'])

        count = len(list(files))

        count = count if count > 0 else 0
        print(count)

        return kProjectName + "_" + str(count) + "_" + projectName.lower().replace(' ', '-')

    @staticmethod
    def create(document):
        directoryName = document.get("directoryName")
        projectName = document.get("projectName")
        serviceVersion = document.get("serviceVersion")

        project = Project.objects.get(projectName=projectName)

        kProjectName = project.kProjectName
        dokerImageName = project.dokerImageName
        gkeServiceName = project.gkeServiceName
        fileName = DocumentService.fileNameGenerator(directoryName=directoryName, kProjectName=kProjectName, projectName=projectName)

        commandList = [document.get("command1"), document.get("command2"), document.get("command3")]

        document = Document(projectName=kProjectName + " " + project.projectName,
                            directoryName=directoryName,
                            fileName=fileName,
                            serviceName=dokerImageName,
                            serviceVersion=serviceVersion,
                            gkeServiceName=gkeServiceName,
                            commandList=json.dumps(commandList))

        CreateDocumentService.createDocument(document)

    @staticmethod
    def findByCode(documentCode):
        return Document.objects.get(code=documentCode)

    @staticmethod
    def findInRoot(root):
        documents = Document.objects.all().filter(directoryName=root)
        return jsonSerializer(documents)
