# 🚀 Django REST Framework (DRF) — To'liq Dars Qo'llanmasi

> **O'qituvchi:** Diyorbek | **Kurs:** Python Backend Juft (14:00–16:00)  
> **Loyiha nomi:** `vision` (asosiy Django project), `motorolla` (app)  
> **Maqsad:** DRF yordamida `Talaba` modelini API sifatida chiqarish

---

## 📋 Mundarija

1. [Virtual muhit va DRF o'rnatish](#1-virtual-muhit-va-drf-ornatish)
2. [Django Proyekt va App yaratish](#2-django-proyekt-va-app-yaratish)
3. [Settings.py sozlash](#3-settingspy-sozlash)
4. [Model yaratish](#4-model-yaratish)
5. [Migration qilish](#5-migration-qilish)
6. [Admin panelga model qo'shish](#6-admin-panelga-model-qoshish)
7. [Superuser yaratish va admin panelni ko'rish](#7-superuser-yaratish-va-admin-panelni-korish)
8. [Serializer yaratish](#8-serializer-yaratish)
9. [View yaratish (ListAPIView)](#9-view-yaratish-listapiview)
10. [URL routing (app va project)](#10-url-routing-app-va-project)
11. [API ni brauzerda tekshirish](#11-api-ni-brauzerda-tekshirish)

---

## 1. Virtual muhit va DRF o'rnatish

**Virtual muhit yaratish va faollashtirish:**
```bash
# Virtual muhit yaratish
python -m venv .venv

# Faollashtirish (Linux/Mac)
source .venv/bin/activate

# Faollashtirish (Windows)
.venv\Scripts\activate
```

**Django va DRF o'rnatish:**
```bash
pip install djangorestframework
```

> Bu buyruq avtomatik ravishda Django va boshqa kerakli paketlarni ham o'rnatadi.

---

## 2. Django Proyekt va App yaratish

```bash
# Django proyekt yaratish
django-admin startproject vision

# Proyekt papkasiga kirish
cd vision

# Fayllari ko'rish
ls
# manage.py  vision/

# App yaratish
python manage.py startapp motorolla
```

**Natija — Papka strukturasi:**
```
vision/
│
├── manage.py
├── db.sqlite3
│
├── vision/              # Asosiy project papkasi
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── motorolla/           # Bizning App
    ├── migrations/
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py   # ← biz yaratamiz
    ├── tests.py
    ├── urls.py          # ← biz yaratamiz
    └── views.py
```

---

## 3. Settings.py sozlash

`vision/settings.py` faylini oching va `INSTALLED_APPS` ga quyidagilarni qo'shing:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'motorolla',        # ← bizning app
    'rest_framework',   # ← DRF
]
```

> ⚠️ Ikkalasini ham qo'shishni unutmang!

---

## 4. Model yaratish

`motorolla/models.py` faylini oching va quyidagilarni yozing:

```python
from django.db import models


class Talaba(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)

    def __str__(self):
        return self.name
```

**Izoh:**
- `Talaba` — model nomi (jadval nomi DB da `motorolla_talaba` bo'ladi)
- `name` va `surname` — 25 ta belgigacha CharField
- `__str__` — admin panelda ob'ekt nomi sifatida `name` ni ko'rsatadi

---

## 5. Migration qilish

Model yaratilgandan so'ng, uni database ga qo'shish kerak:

```bash
# Migration fayl yaratish
python manage.py makemigrations

# Migration ni bajarish (DB ga jadval qo'shish)
python manage.py migrate
```

---

## 6. Admin panelga model qo'shish

`motorolla/admin.py` faylini oching:

```python
from django.contrib import admin
from .models import Talaba

admin.site.register(Talaba)
```

**Izoh:**
- `from .models import Talaba` — modelni import qilamiz
- `admin.site.register(Talaba)` — admin panelga ro'yxatdan o'tkazamiz

---

## 7. Superuser yaratish va admin panelni ko'rish

```bash
# Superuser yaratish
python manage.py createsuperuser
# Username: admin
# Email: admin@mail.com
# Password: (xohlagan parol, masalan: admin1234)

# Serverni ishga tushirish
python manage.py runserver
```

Brauzerda oching: **http://127.0.0.1:8000/admin/**

Admin panelda login qiling va:
- **MOTOROLLA** bo'limida **Talabas** ko'rinadi
- "Add talaba" tugmasi bilan ma'lumot qo'shish mumkin

**Ma'lumot qo'shing (sinov uchun):**
| Name | Surname |
|------|---------|
| Sarvar | Iskandarov |
| Temurmalik | Allaberdiyev |
| Lazizbek | Uralov |

---

## 8. Serializer yaratish

`motorolla/` papkasida `serializers.py` nomli yangi fayl yarating:

```python
from rest_framework import serializers
from .models import Talaba


class TalabaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'
```

**Izoh:**
- `ModelSerializer` — modeldan avtomatik serializer yaratadi
- `fields = '__all__'` — modelning barcha maydonlarini API da ko'rsatadi
- Agar faqat ba'zi maydonlarni ko'rsatmoqchi bo'lsangiz:
  ```python
  fields = ['name', 'surname']
  ```

---

## 9. View yaratish (ListAPIView)

`motorolla/views.py` faylini oching:

```python
from django.shortcuts import render
from rest_framework import generics
from .serializers import TalabaSerializers
from .models import Talaba


class MalumotAPi(generics.ListAPIView):
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializers
```

**Izoh:**
- `generics.ListAPIView` — barcha ob'ektlarni **GET** bilan ro'yxat sifatida qaytaradi
- `queryset` — qaysi ma'lumotlarni olish kerak
- `serializer_class` — qaysi serializer ishlatilsin

---

## 10. URL routing (app va project)

### 10.1 App URL (motorolla/urls.py)

`motorolla/` papkasida `urls.py` nomli yangi fayl yarating:

```python
from django.urls import path
from .views import MalumotAPi

urlpatterns = [
    path('api', MalumotAPi.as_view()),
]
```

### 10.2 Project URL (vision/urls.py)

`vision/urls.py` faylini oching va app URL ni qo'shing:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('talaba/', include('motorolla.urls')),
]
```

**Izoh:**
- `include('motorolla.urls')` — `motorolla` app ning URL larini `talaba/` path ostida ulaydi
- Natijada API manzili: **http://127.0.0.1:8000/talaba/api**

---

## 11. API ni brauzerda tekshirish

Server ishlab turgan bo'lishi kerak:
```bash
python manage.py runserver
```

Brauzerda oching: **http://127.0.0.1:8000/talaba/api**

**Kutilgan natija (DRF browsable API):**
```json
[
    {
        "name": "Sarvar",
        "surname": "Iskandarov"
    },
    {
        "name": "Temurmalik",
        "surname": "Allaberdiyev"
    },
    {
        "name": "Lazizbek",
        "surname": "Uralov"
    }
]
```

> 🎉 DRF browsable API avtomatik ravishda chiroyli interfeys yaratadi!
> Sahifa sarlavhasi: **Malumot A Pi** (view klassi nomidan)

---

## 📁 Yakuniy fayl tuzilmasi

```
vision/
│
├── manage.py
├── db.sqlite3
│
├── vision/
│   ├── settings.py     ← rest_framework va motorolla qo'shilgan
│   └── urls.py         ← path('talaba/', include('motorolla.urls'))
│
└── motorolla/
    ├── models.py       ← Talaba modeli
    ├── serializers.py  ← TalabaSerializers
    ├── views.py        ← MalumotAPi (ListAPIView)
    ├── urls.py         ← path('api', MalumotAPi.as_view())
    └── admin.py        ← admin.site.register(Talaba)
```

---

## 🔑 Asosiy tushunchalar

| Tushuncha | Izoh |
|-----------|------|
| **Model** | Database jadvalini ifodalaydi |
| **Serializer** | Python ob'ektlarini JSON ga va aksincha aylantiradi |
| **View (APIView)** | HTTP so'rovlarni qabul qilib javob qaytaradi |
| **URL** | Qaysi URL da qaysi View ishlashi kerakligini belgilaydi |
| **Migration** | Model o'zgarishlarini database ga qo'llaydi |
| **ListAPIView** | GET so'rovda barcha ob'ektlar ro'yxatini qaytaradi |

---

## ⚡ Tez eslatma (Barcha buyruqlar)

```bash
# 1. Virtual muhit
python -m venv .venv
.venv\Scripts\activate          # Windows

# 2. O'rnatish
pip install djangorestframework

# 3. Proyekt va app
django-admin startproject vision
cd vision
python manage.py startapp motorolla

# 4. Migration
python manage.py makemigrations
python manage.py migrate

# 5. Superuser
python manage.py createsuperuser

# 6. Server ishga tushurish
python manage.py runserver
```

---

## 🎯 Uy vazifa (Ustoz bergan)

> **Vazifa:** 10 ta ustundan iborat table yaratish

10 ta field li model yarating, masalan:

```python
class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    miqdori = models.IntegerField()
    kategoriya = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    rang = models.CharField(max_length=30)
    og_irligi = models.FloatField()
    ishlab_chiqarilgan_yil = models.IntegerField()
    tavsif = models.TextField()
    mavjud = models.BooleanField(default=True)

    def __str__(self):
        return self.nomi
```

Keyin shu model uchun ham serializer, view va URL yarating!
