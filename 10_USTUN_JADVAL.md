# 🚗 Django REST Framework: 10 ta ustunli jadval (Table) yaratish qo'llanmasi

Ushbu qo'llanmada **Avtomobil** (`Avtomobil`) modeli misolida 10 ta ustunli jadvalni alohida yaratishni bosqichma-bosqich o'rganasiz. Buni o'zingiz mustaqil boshqa papkada bajarishingiz mumkin!

---

## 1. Modellar bilan ishlash (`models.py`)

Jadval ustunlarini aniqlash uchun app ichidagi `models.py` fayliga quyidagi kodni yozing. Biz turli xil ma'lumot turlaridan (matn, son, boolean, decimal) foydalanamiz:

```python
from django.db import models

class Avtomobil(models.Model):
    # 1. Brend (Chevrolet, BYD, Hyundai)
    brend = models.CharField(max_length=50)
    
    # 2. Model (Gentra, Song Plus, Elantra)
    model = models.CharField(max_length=50)
    
    # 3. Ishlab chiqarilgan yili (masalan: 2024)
    yil = models.IntegerField()
    
    # 4. Narxi (masalan: 15000.00)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    
    # 5. Rangi (Oq, Qora, Kulrang)
    rangi = models.CharField(max_length=30)
    
    # 6. Dvigatel hajmi (masalan: 1.5, 2.0)
    dvigatel_hajmi = models.FloatField()
    
    # 7. Yurgan masofasi (km da)
    yurgan_masofasi = models.IntegerField()
    
    # 8. Yoqilg'i turi (Benzin, Gaz, Elektr, Gibrid)
    yoqilgi_turi = models.CharField(max_length=20)
    
    # 9. Uzatmalar qutisi (Mexanika, Avtomat)
    uzatmalar_qutisi = models.CharField(max_length=20)
    
    # 10. Holati (True bo'lsa - yangi, False bo'lsa - haydalgan)
    yangi = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brend} {self.model} ({self.yil})"
```

**Databasega qo'llash:**
Kodni yozgandan so'ng terminalda quyidagi buyruqlarni ishga tushiring:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 2. Serializer yaratish (`serializers.py`)

App papkasi ichida `serializers.py` faylini ochib, ma'lumotlarni JSON shakliga o'tkazuvchi class yozamiz:

```python
from rest_framework import serializers
from .models import Avtomobil

class AvtomobilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avtomobil
        fields = '__all__' # Barcha 10 ta ustunni API ga chiqaradi
```

---

## 3. View yaratish (`views.py`)

Ma'lumotlarni ro'yxat shaklida ko'rsatish va yangi avtomobil qo'shish uchun `views.py` fayliga yozing:

```python
from rest_framework import generics
from .models import Avtomobil
from .serializers import AvtomobilSerializer

# Faqat ro'yxatni ko'rish (GET) uchun:
class AvtomobilListAPI(generics.ListAPIView):
    queryset = Avtomobil.objects.all()
    serializer_class = AvtomobilSerializer

# Agar ham ko'rish (GET), ham yangi qo'shish (POST) ni xohlasangiz:
class AvtomobilListCreateAPI(generics.ListCreateAPIView):
    queryset = Avtomobil.objects.all()
    serializer_class = AvtomobilSerializer
```

---

## 4. URL marshrutlash (`urls.py`)

### 4.1 App ichidagi `urls.py` ga ulash:
App papkangizda `urls.py` yaratib, quyidagi kodni kiriting:

```python
from django.urls import path
from .views import AvtomobilListCreateAPI

urlpatterns = [
    path('avto/', AvtomobilListCreateAPI.as_view()),
]
```

### 4.2 Project ichidagi `urls.py` ga ulash:
Asosiy loyiha papkasidagi `urls.py` ga app-ni ulaymiz:

```python
from django.urls import path, include

urlpatterns = [
    # ... boshqa url-lar
    path('api/', include('app_nomi.urls')), # 'app_nomi' o'rniga o'z app-ingiz nomini yozing
]
```

Natijada API manzili: `http://127.0.0.1:8000/api/avto/` bo'ladi.

---

## 5. Admin panelda ko'rsatish (`admin.py`)

Avtomobillarni admin paneldan turib boshqarish va yangi ma'lumotlar kiritish uchun:

```python
from django.contrib import admin
from .models import Avtomobil

admin.site.register(Avtomobil)
```
