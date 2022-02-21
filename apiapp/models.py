from django.db import models
class ourusers(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    userId = models.IntegerField()
    def __str__(self):
        return self.firstName