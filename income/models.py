from django.db import models
from authenticated.models import User
# Create your models here.



class Income(models.Model):

    SOURCE_OPTION = [
        ('SALARY', 'SALARY'),
        ('BUSINESS', 'BUSINESS'),
        ('OTHERS', 'OTHERS'),
    ]

    source = models.CharField(choices=SOURCE_OPTION, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=250)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    descriptions = models.TextField()
    date = models.DateField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



    class Meta:
       ordering=['-update_at']


    def __str__(self):
        return str(self.owner)+'s income'


