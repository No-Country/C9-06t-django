from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField('Nombre', max_length=50)
    email = models.EmailField('Gmail', max_length=254)
    affair = models.CharField('Asunto', max_length=50)
    message = models.TextField('Mensaje',  max_length=50)

    def __str__(self):

        return self.name + ' ' + self.affair
