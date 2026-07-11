from django.urls import path
from .views import MalumotAPi, AvtomobilListCreateAPI

urlpatterns = [
    path('api', MalumotAPi.as_view()),
    path('avto/', AvtomobilListCreateAPI.as_view()),
]
