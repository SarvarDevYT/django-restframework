from django.urls import path
from .views import MalumotAPi, AvtomobilListAPI

urlpatterns = [
    path('api', MalumotAPi.as_view()),
    path('avto/', AvtomobilListAPI.as_view()),
]
