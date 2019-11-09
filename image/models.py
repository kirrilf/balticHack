from django.db import models

def nameFile(instance, filename):
    return '/'.join([filename])

class UploadImageTest(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, max_length=254, blank=True, null=True)