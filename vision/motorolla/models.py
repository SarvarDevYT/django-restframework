from django.db import models

class Talaba(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Avtomobil(models.Model):
    brend = models.CharField(max_length=50)
    
    model = models.CharField(max_length=50)
    
    yil = models.IntegerField()
    
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    
    rangi = models.CharField(max_length=30)
    
    dvigatel_hajmi = models.FloatField()
    
    yurgan_masofasi = models.IntegerField()
    
    yoqilgi_turi = models.CharField(max_length=20)
    
    uzatmalar_qutisi = models.CharField(max_length=20)
    
    yangi = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brend} {self.model} ({self.yil})"
