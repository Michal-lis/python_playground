from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=140)
    director = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
        # like a table
        # each variable is a column
        # each attribut es is a row


# class Sala(models.Model):
#     number = models.IntegerField()
#     capacity = models.IntegerField()

class Viewing(models.Model):
    title = models.ForeignKey(Film)
    #sala = models.ForeignKey(Sala)
    viewdate = models.DateTimeField()

    def __str__(self):
        return self.viewdate
