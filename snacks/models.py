from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    snack_name = models.CharField(max_length=255,help_text="Name of the snack you want to add")
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField(default="no desc available")

    
    def __str__(self):
        return self.snack_name
        