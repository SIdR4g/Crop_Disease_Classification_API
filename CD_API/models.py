from django.db import models

# Create your models here.
class CropDiseaseAPI(models.Model):
    id = models.AutoField(primary_key=True)
    crop = models.CharField(max_length= 50,null = True,blank = True)
    file = models.FileField(upload_to='file')

    def __str__(self):
        return str(self.id)

class Farmers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 50,null = True,blank = True)
    level = models.CharField(max_length= 50,null = True,blank = True)

    def __str__(self):
        return str(self.id)

