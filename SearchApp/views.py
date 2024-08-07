from django.shortcuts import render
from .models import CarDetails
from django.db.models import Q


def Home(request):
    car_details = CarDetails.objects.all()
    if request.method == "POST":
        search = request.POST.get('search')
        if search:
            car_details = car_details.filter(Q(name__icontains=search) | Q(model__icontains=search))
        sort_data = request.POST.get('sort')
        if sort_data == 'price_asc':
            car_details = car_details.order_by('price')
        else :
            car_details = car_details.order_by('-price')
             
    return render(request,"home.html",{"car_details":car_details})
