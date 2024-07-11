from django.db import models

# Create your models here.
class Century(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Decade(models.Model):
    century = models.ForeignKey(Century, on_delete=models.CASCADE, related_name='decades')
    name = models.CharField(max_length=100, default='no name')
    start_year = models.CharField(max_length=100, default = 'no start')
    end_year = models.CharField(max_length=100, default = 'no end')

    def __str__(self):
        return self.name
    
class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=100, default='no name')
    image_url = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=100, default = 'no description')

    def __str__(self):
        return self.name