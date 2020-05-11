from django.db import models

# Create your models here.

class Home(models.Model):
    first=models.CharField("First Line Of Text in Homepage",max_length = 100,null=True,blank=True)
    second=models.CharField("Second Line Of Text in Homepage",max_length = 100,null=True,blank=True)
    third=models.CharField("Third Line Of Text in Homepage",max_length = 100,null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Home"

    def __str__(self):
        return self.first+" "+self.second