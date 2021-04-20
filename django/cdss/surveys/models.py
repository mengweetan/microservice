from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class survey(models.Model):

    loc = models.CharField(max_length=10,default='wcp',)
    block = models.IntegerField(max_length=4,)
    data = JSONField(default={},)

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}
