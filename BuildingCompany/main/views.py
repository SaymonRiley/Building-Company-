from django.shortcuts import render
from .models import BuildingCompany,Service

def index(request):
    company = BuildingCompany.objects.first()  # Получаем первую запись о компании из базы данных
    services = Service.objects.all()

    context = {
        'company': company,
        'services': services
    }
    return render(request, 'index.html', context)
