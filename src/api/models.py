from django.db import models

class Personne(models.Model):
    nom = models.CharField('Nom', max_length=255)
    prenom = models.CharField('Prénom', max_length=255)
    date_de_naissance = models.DateField('Date de naissance')
    created_at = models.DateTimeField('Date de création', auto_now_add=True)
    updated_at = models.DateTimeField('Date de modification', auto_now=True)
    
    def __str__(self):
        return "%s, %s" % (super().__str__(), self.nom)

    class Meta:
        verbose_name = "Personne"
        verbose_name_plural = "Personnes"
