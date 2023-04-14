from django.db import models
from django.http import HttpResponse, HttpRequest

# Create your models here.

#Defining Database Object 
class ScanData(models.Model):
    #From Tag
    UID = models.CharField(max_length=200, default='')
    UTC = models.CharField(max_length=200, default='')
    TKN_ID = models.CharField(max_length=200, default='')
    TAMP_CHCK = models.BooleanField(null=False, default=False)
    

    #Not from Tag
    ValidScan = models.CharField(max_length=200, default='')

    #Shoe info
    Model = models.CharField(max_length=200, default='')
    ShoeImage = models.ImageField(null=True,blank=True, upload_to = "images/")

    '''
    def __str__(self):
        return self.UID + self.UTC + self.TKN_ID + self.Model + self.TAMP_CHCK
    '''


