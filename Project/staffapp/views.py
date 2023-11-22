from django.shortcuts import render
from .models import stafapp

def index(request):
    return render(request, 'staffapp/index.html')

def staffapp(request, orphanage_id):
    staffapp = Staffapp.objects.get(id=staffapp_id)
    return render(request, 'staffapp/orphanage.html', {'stafapp': staffapp})

def staffapp(request):
    staffapp = S    taffapp.objects.all()
    return render(request, 'staffapp/staffapp.html', {'staffapp': staffapp})

def create_orphanage(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        contact = request.POST['contact']

        staffapp.objects.create(name=name, location=location, contact=contact)

        return render(request, 'staffapp/create_orphanage.html')
    else:
        return render(request, 'staffapp/create_orphanage.html')