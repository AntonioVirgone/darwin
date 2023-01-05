from django.db import models
from django.utils import timezone


# Create your models here.
class Document(models.Model):
    code = models.CharField(max_length=200)
    projectName = models.CharField(max_length=200)
    directoryName = models.CharField(max_length=200)
    fileName = models.CharField(max_length=200)
    serviceName = models.CharField(max_length=200)
    serviceVersion = models.CharField(max_length=200)
    gkeServiceName = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Project(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    serviceName = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()