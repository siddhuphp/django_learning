from django.db import models

# Create your models here.
class fruits(models.Model):
        fruit_name = models.CharField(max_length=20)       
        cost = models.CharField(max_length=20)
        quanty = models.CharField(max_length=10)        

        def __str__(self):
                return self.fruit_name

class Album(models.Model):
        artist = models.ForeignKey(fruits, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        release_date = models.DateField()
        num_stars = models.IntegerField()    
             

        def __str__(self):
                return self.artist