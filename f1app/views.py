from django.shortcuts import render, get_object_or_404

from f1app.models import Constructor, Driver


# Create your views here.
def index(request):
    constructors=Constructor.objects.all()
    return render(request,'index.html',{'constructors':constructors})
def details(request, constructor_id):
    constructor = get_object_or_404(Constructor, pk=constructor_id)
    drivers = Driver.objects.filter(constructor=constructor).all()
    for driver in drivers:
        print(driver)
    return render(request, 'details.html', {
        'constructor': constructor,
        'drivers': drivers,
    })

def all_drivers(request):
    drivers = Driver.objects.select_related('constructor').all()
    return render(request, 'drivers.html', {'drivers': drivers})
