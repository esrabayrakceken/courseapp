
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('kurs/',include('courses.urls')),
    path('',include('pages.urls')),
    path('admin/', admin.site.urls),
]
#courseapp -- ana proje klasörü
#courses   -- uygulama1
#pages     -- uygulama2