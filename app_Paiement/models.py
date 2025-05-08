from django.db import models

from app_Eleve.models import Eleve


class Frais(models.Model):
    nom_frais = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Frais de {self.eleve.user.username} - {self.nom_frais}"
    
class paiement(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='paiements')
    date_paiement = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    frais = models.ForeignKey(Frais, on_delete=models.CASCADE, related_name='paiements')

    reference = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Paiement de {self.eleve.user.username} - {self.date_paiement}"
    

    