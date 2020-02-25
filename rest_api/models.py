from django.db import models

# Create your models here.
class players(models.Model):
        first_name = models.CharField(max_length=20)
        last_name = models.CharField(max_length=20)
        email = models.CharField(max_length=20)
        contact = models.CharField(max_length=10)
        player_id = models.IntegerField(primary_key=True)

        def __str__(self):
                return self.first_name