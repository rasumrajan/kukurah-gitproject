from django.forms import model_to_dict
from django.shortcuts import render
from pages.models import Farm_bread
from .models import Farm_bread, dog_slider
from dogs.models import Dog

# Create your views here.

def home(request):
    farm_breads = Farm_bread.objects.all()
    dog_sliders = dog_slider.objects.all()
    featured_dog =  Dog.objects.order_by('-created_date').filter(is_featured=True)
    all_dog = Dog.objects.order_by('-created_date') 
    #search_fields = Dog.objects.values('bread_name','age','city','color','Dogs_type','price')
    bread_name_search = Dog.objects.values_list('bread_name',flat=True).distinct()
    age_search = Dog.objects.values_list('age',flat=True).distinct()
    city_search = Dog.objects.values_list('city',flat=True).distinct()
    color_search = Dog.objects.values_list('color',flat=True).distinct()
    Dogs_type_search = Dog.objects.values_list('Dogs_type',flat=True).distinct()
    price_search = Dog.objects.values_list('price',flat=True).distinct()
    KCI_Registerd_search = Dog.objects.values_list('KCI_Registerd',flat=True).distinct()

    data = {
        'dog_sliders': dog_sliders,
        'farm_breads': farm_breads,
        'featured_dog': featured_dog,
        'all_dog':all_dog,
        #'search_fields': search_fields,
        'bread_name_search': bread_name_search,
        'age_search': age_search,
        'color_search': color_search,
        'price_search': price_search,
        'Dogs_type_search': Dogs_type_search,
        'city_search': city_search,
        'KCI_Registerd_search':KCI_Registerd_search,
    }
    return render(request,'pages/home.html',data)

def about(request):
    return render(request,'pages/about.html')

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')

def dogs(request):
    return render(request,'pages/dogs.html')
