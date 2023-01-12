import json

from django.core import serializers

from document.models import Document
from project.models import Project
from service import CreateDocumentService


def jsonSerializer(articles):
    return serializers.serialize("json", articles)


class DocumentService:

    @staticmethod
    def create(document):
        directoryName = document.get("directoryName")
        projectName = document.get("projectName")
        fileName = document.get("fileName")
        serviceVersion = document.get("serviceVersion")

        project = Project.objects.get(projectName=projectName)

        dokerImageName = project.dokerImageName
        gkeServiceName = project.gkeServiceName

        commandList = [document.get("command1"), document.get("command2"), document.get("command3")]

        document = Document(projectName=projectName,
                            directoryName=directoryName,
                            fileName=fileName,
                            serviceName=dokerImageName,
                            serviceVersion=serviceVersion,
                            gkeServiceName=gkeServiceName,
                            commandList=json.dumps(commandList))
        
        document.save()
        CreateDocumentService.createDocument(document)

    @staticmethod
    def findByCode(documentCode):
        return Document.objects.get(code=documentCode)

    @staticmethod
    def findInRoot(root):
        articles = Document.objects.all().filter(directoryName=root)
        return jsonSerializer(articles)
