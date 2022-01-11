from django.db import models



class Owner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=False)
    email = models.EmailField(max_length=100)
    class Meta:
        db_table = 'owners'
        
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=False)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, null=False)
    
    class Meta:
        db_table = 'dogs'
        
    