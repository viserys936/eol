from django.db import models

class Creature(models.Model):
    c_id = models.TextField(default="", primary_key=True)
    s_name = models.TextField(default="")
    c_name = models.TextField(default="")
    category = models.TextField(default="")
    iucn_level = models.TextField(default="")
    level = models.TextField(default="")
    location = models.TextField(default="")
    location_number = models.TextField(default="")
    location_style = models.TextField(default="")
    
    
