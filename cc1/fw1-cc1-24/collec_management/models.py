from django.db import models

class Collec ( models . Model ):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    creation_date = models.DateField(null=False, blank=False)
    #null=False et blank=False signifient que ce champ ne peut pas être vide ou null

    def __str__ ( self ):
        return self.title

