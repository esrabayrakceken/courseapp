from django.urls import path
from . import views
#http://127.0.0.1:8000/        --> anasayfa
#http://127.0.0.1:8000/home    --> anasayfa
#http://127.0.0.1:8000/kurslar -->kurslar


urlpatterns = [
    path('',views.index),
    path('<slug:slug>',views.details, name="course_details"),
    
       # datails metoduyla getCourses metodları birbirine karışmasın diye, kategori/ adında sabit belirledik.
       # Aksi halde details üstte olduğu için o methodu görür, alttakileri çalıştırmaz.
       # kurs/programlama yazarsam programlama detayları der. buna engel olmak için kurs/kategori/programlama yapıyorum.
    
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>',views.getCoursesByCategory, name = 'courses_by_category'),
  
    
    
    
]
