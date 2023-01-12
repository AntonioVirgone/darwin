from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    projectName = models.CharField(max_length=200)
    kProjectName = models.CharField(max_length=200)
    dokerImageName = models.CharField(max_length=200)
    gkeServiceName = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
