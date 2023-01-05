import uuid

from document.models import Document
from service import CreateDocumentService
from service.model.DataDocument import DataDocument

from django.core import serializers


def jsonSerializer(articles):
    return serializers.serialize("json", articles)


class DocumentService:

    @staticmethod
    def create(data):
        dataDocument = DataDocument.fromJson(data)

        document = Document(code=str(uuid.uuid4()),
                            projectName=dataDocument.fileName,
                            serviceName=dataDocument.serviceName,
                            directoryName=dataDocument.directoryName,
                            serviceVersion=dataDocument.serviceVersion,
                            gkeServiceName=dataDocument.gkeServiceName,
                            fileName=dataDocument.fileName)
        document.save()

        CreateDocumentService.createDocument(dataDocument)

    @staticmethod
    def findByCode(documentCode):
        return Document.objects.get(code=documentCode)

    @staticmethod
    def findInRoot(root):
        articles = Document.objects.all().filter(directoryName=root)
        return jsonSerializer(articles)
