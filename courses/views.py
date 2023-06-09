from datetime import date,datetime
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course,Category
data = {
    "programlama" : "programlama kategorisine ait kurslar",
    "mobil-uygulama" : "mobil uygulamalara ait kurslar",
    "web-gelistirme" : "web geliştirmeye ait kurslar",
}

db ={
    "courses": [
        {
            "title" : "javascript kursu",
            "description" : "javascript kurs açıklaması",
            "imageurl" : "1.jpg",
            "slug" : "javascript-kursu",
            "date" : datetime.now,
            "isActive" : True,
            "isUpdated" : True
        },
        {
            "title" : "python kursu",
            "description" : "python kurs açıklaması",
            "imageurl" : "2.jpg",
            "slug" : "python-kursu",
            "date" : datetime.now,
            "isActive" : True,
            "isUpdated" : True
            
        },
        {
            "title" : "web-geliştirme kursu",
            "description" : "web-geliştirme kurs açıklaması",
            "imageurl" : "3.jpg",
            "slug" : "web-gelistirme-kursu",
            "date" : datetime.now,
            "isActive" : True,
            "isUpdated" : True
            
        }
    ],
    "categories" : [
        {
            "id" : 1,
            "name": "Programlama",
            "slug" : "programlama"
        },
        {
            "id" : 2,
            "name": "Web geliştirme",
            "slug" : "web-gelistirme"
        },
        {
            "id" : 3,
            "name": "Mobil uygulamalar",
            "slug" : "mobil-uygulamalar"
        }
    ]
}


def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()
    
    #bunun yerine render aracılığıyla dosyadan dianmik veri alıyoruz.
    # for category in category_list:
    #     redirect_url = reverse('courses_by_category', args=[category])
    #     list_items += f"<li><a href = '{redirect_url}'>{category}</a></li>"
    # html = f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"
    
    return render(request, "courses/index.html", {
        'categories' : kategoriler,
        "courses" : kurslar
        })

def details(request,slug):
    # try:
    #     course = Course.objects.get(pk=kurs_id)
    # except:
    #     raise Http404
    
    #try-except yerine kısaltma da kullanabiliriz.
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

#dinamik url tanımlaması yaptık. kullanıcı arama çubuğuna ne yazarsa ona göre yönlendirme yapacak.O yüzden category parametresi kullandık
def getCoursesByCategory(request, category_name):
    try: 
        category_text = data[category_name];
        return render(request, 'courses/kurslar.html', {
            'category' : category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound("yanlış kategori girişi")
    

#yönlendirme yaptım. Responce döndürmek yerine başka bir view'e yönlendirdim. id girdiği sürece text = programlama çalıştıracak. 
def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())  #[programlama,mobil-uygualama,web-gelistirme] şeklinde bir liste oluşturur.
    
    if(category_id > len(category_list)):  #girilen değer liste uzunluğunda büyükse
        return HttpResponseNotFound("yanlış kategori girdiniz")
    
    category_text = category_list[category_id - 1]  #1 girerse 0.index, 2 girerse 1. index 
    redirect_url = reverse('courses_by_category', args = [category_text])
    return redirect(redirect_url) #httpresponseredirect'in kısa yoludur.
        
        
    
# Create your views here.
