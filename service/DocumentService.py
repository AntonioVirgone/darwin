import uuid

from django.core import serializers

from document.models import Document
from service import CreateDocumentService


def jsonSerializer(articles):
    return serializers.serialize("json", articles)


class DocumentService:

    @staticmethod
    def create(document):
        document.save()
        CreateDocumentService.createDocument(document)

    @staticmethod
    def findByCode(documentCode):
        return Document.objects.get(code=documentCode)

    @staticmethod
    def findInRoot(root):
        articles = Document.objects.all().filter(directoryName=root)
        return jsonSerializer(articles)
