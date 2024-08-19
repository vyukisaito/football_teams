from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.CharField(max_length=100)
    year = models.DateField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    national_titles = models.TextField(max_length=500, blank=True, null=True)
    international_titles = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='teams', blank=True, null=True)

    def get_national_titles_as_list(self):
        return self.national_titles.split(',')

    def get_international_titles_as_list(self):
        return self.international_titles.split(',')

    def __str__(self):
        return self.team
