from django.db import models
import datetime
from musician.models import MusicianForm
# Create your models here.

class Ratings(models.IntegerChoices):
    ONE = 1, 'One'
    TWO = 2, 'Two'
    THREE = 3, 'Three'
    FOUR = 4, 'Four'
    FIVE = 5, 'Five'

# Define the AlbumForm model
class AlbumForm(models.Model):
    Album_name = models.CharField(max_length=50)
    Release_Date = models.DateField(default=datetime.date.today)
    Ratings = models.IntegerField(choices=Ratings.choices,default=1)
    musician = models.ForeignKey(MusicianForm, on_delete=models.CASCADE)

    def __str__(self):
        return self.Album_name