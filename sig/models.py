from django.db import models

class Database(models.Model):
    display= models.CharField(max_length=250)
    shortcut = models.CharField(max_length=10)

    def __str__(self):
       return self.shortcut

class Signal(models.Model):
    database = models.ForeignKey(Database, on_delete=models.CASCADE)
    display = models.CharField(max_length=10)
    shortcut = models.CharField(max_length=10)

    def __str__(self):
       return self.shortcut