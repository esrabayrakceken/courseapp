from django.urls import path
from . import views
#http://127.0.0.1:8000/        --> anasayfa
#http://127.0.0.1:8000/home    --> anasayfa
#http://127.0.0.1:8000/kurslar -->kurslar


urlpatterns = [
    path('',views.home),
    path('anasayfa',views.home),
    path('kurslar',views.kurslar),
]
