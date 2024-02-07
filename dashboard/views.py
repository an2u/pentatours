from django.shortcuts import render
from .models import Gallery,TravelPartner,TripDetail,Destination,garage


# Create your views here.
def dashboard(request):
    context={}
    return render(request,'dashboard/index.html',context=context)

def home(request):
    context={}
    return render(request,'dashboard/home.html',context=context)

def packages(request):
    destinationdetails=Destination.objects.all()
    context={
        'destinationdetails':destinationdetails
        }
    return render(request,'dashboard/packages.html',context=context)

def events(request):
    vehicledetails=garage.objects.all()
    context={
        'vehicledetails':vehicledetails
    }
    return render(request,'dashboard/events.html',context=context)

def partners(request):
    partnerdetails=TravelPartner.objects.all()
    context={
        'partnerdetails':partnerdetails
    }
    return render(request,'dashboard/partners.html',context=context)


def trips(request):
    tripsdetails=TripDetail.objects.all()
    context={
        'tripsdetails':tripsdetails
    }
    return render(request,'dashboard/trips.html',context=context)


def gallery(request):
    images=Gallery.objects.all()
    context={
        'images':images,
    }
    return render(request,'dashboard/gallery.html',context=context)
