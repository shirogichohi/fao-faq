from django.db import models


class System(models.Model):
    project = models.CharField(max_length=250 , unique=True)
    description = models.TextField(max_length=250)
    status = models.CharField(max_length=1,default=1)

    def __str__(self):
        return f"{self.project}"

    def __repr__(self):
        return f"{self.project}"

