from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from Project.models import Project


class Issue(models.Model):
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    question = models.CharField(max_length=250, unique=True)
    answer = RichTextUploadingField()
    #pub_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1,default=1)

