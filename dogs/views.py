from django.shortcuts import get_object_or_404, render

from .models import Dog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def dogs(request):
    dogs = Dog.objects.order_by('-created_date')
    paginator = Paginator(dogs, 3)
    page = request.GET.get('page')
    paged_dogs = paginator.get_page(page)
    bread_name_search = Dog.objects.values_list('bread_name',flat=True).distinct()
    age_search = Dog.objects.values_list('age',flat=True).distinct()
    city_search = Dog.objects.values_list('city',flat=True).distinct()
    color_search = Dog.objects.values_list('color',flat=True).distinct()
    Dogs_type_search = Dog.objects.values_list('Dogs_type',flat=True).distinct()
    price_search = Dog.objects.values_list('price',flat=True).distinct()
    KCI_Registerd_search = Dog.objects.values_list('KCI_Registerd',flat=True).distinct()

    data = {
        'dogs' : paged_dogs,
        'bread_name_search': bread_name_search,
        'age_search': age_search,
        'color_search': color_search,
        'price_search': price_search,
        'Dogs_type_search': Dogs_type_search,
        'city_search': city_search,
        'KCI_Registerd_search':KCI_Registerd_search,
    }
    return render(request,'dogs/dogs.html',data)


def dog_detail(request, id):
    single_dog = get_object_or_404(Dog, pk=id )
    data = {
        'single_dog':single_dog,
    }
    return render(request,'dogs/dog_detail.html',data)

def search(request):
    dogs = Dog.objects.order_by('-created_date')
    #for search box in search page template
    bread_name_search = Dog.objects.values_list('bread_name',flat=True).distinct()
    age_search = Dog.objects.values_list('age',flat=True).distinct()
    city_search = Dog.objects.values_list('city',flat=True).distinct()
    color_search = Dog.objects.values_list('color',flat=True).distinct()
    Dogs_type_search = Dog.objects.values_list('Dogs_type',flat=True).distinct()
    price_search = Dog.objects.values_list('price',flat=True).distinct()
    KCI_Registerd_search = Dog.objects.values_list('KCI_Registerd',flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            dogs = dogs.filter(description__icontains=keyword)

    if 'bread_name' in request.GET:
        bread_name = request.GET['bread_name']
        if bread_name:
            dogs = dogs.filter(bread_name__iexact=bread_name)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            dogs = dogs.filter(city__iexact=city)

    if 'Dogs_type' in request.GET:
        Dogs_type = request.GET['Dogs_type']
        if Dogs_type:
            dogs = dogs.filter(Dogs_type__iexact=Dogs_type)

    if 'color' in request.GET:
        color = request.GET['color']
        if color:
            dogs = dogs.filter(color__iexact=color)

    if 'KCI_Registerd' in request.GET:
        KCI_Registerd = request.GET['KCI_Registerd']
        if KCI_Registerd:
            dogs = dogs.filter(KCI_Registerd__iexact=KCI_Registerd)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            dogs = dogs.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'dogs':dogs,
        'bread_name_search': bread_name_search,
        'age_search': age_search,
        'color_search': color_search,
        'price_search': price_search,
        'Dogs_type_search': Dogs_type_search,
        'city_search': city_search,
        'KCI_Registerd_search':KCI_Registerd_search,
    }
    return render(request,'dogs/search.html',data)
