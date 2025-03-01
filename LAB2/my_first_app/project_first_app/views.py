from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Owner, Car, DrivingLicense, Ownership
from .forms import OwnerForm
from rest_framework import generics
from rest_framework.response import Response
from random import randint

from .serializers import OwnerSerializer


class CarOwnerCreateAndListView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        # # Создаем 6-7 владельцев автомобилей
        # owner1 = Owner.objects.create(last_name='Ivanov', first_name='Ivan', birth_date=timezone.now())
        # owner2 = Owner.objects.create(last_name='Petrov', first_name='Petr', birth_date=timezone.now())
        # owner3 = Owner.objects.create(last_name='Sidorov', first_name='Sidor', birth_date=timezone.now())
        # owner4 = Owner.objects.create(last_name='Kuznetsov', first_name='Sergey', birth_date=timezone.now())
        # owner5 = Owner.objects.create(last_name='Popov', first_name='Andrey', birth_date=timezone.now())
        # owner6 = Owner.objects.create(last_name='Semenov', first_name='Dmitry', birth_date=timezone.now())
        #
        # # Создаем удостоверения для каждого владельца
        # DrivingLicense.objects.create(owner=owner1, license_number='111', document_number='1', type='A',
        #                               issue_date=timezone.now())
        # DrivingLicense.objects.create(owner=owner2, license_number='222', document_number='2', type='B',
        #                               issue_date=timezone.now())
        # DrivingLicense.objects.create(owner=owner3, license_number='333', document_number='3', type='C',
        #                               issue_date=timezone.now())
        # DrivingLicense.objects.create(owner=owner4, license_number='444', document_number='4',
        #                               type='A,B', issue_date=timezone.now())
        # DrivingLicense.objects.create(owner=owner5, license_number='555', document_number='5',
        #                               type='B,C', issue_date=timezone.now())
        # DrivingLicense.objects.create(owner=owner6, license_number='666', document_number='6', type='C',
        #                                                  issue_date=timezone.now())
        #
        # # Создаем 5-6 автомобилей
        # car1 = Car.objects.create(license_plate='AA1111', make='Honda', model='Civic', color='black')
        # car2 = Car.objects.create(license_plate='BB2222', make='Toyota', model='Corolla', color='white')
        # car3 = Car.objects.create(license_plate='CC3333', make='BMW', model='X5', color='blue')
        # car4 = Car.objects.create(license_plate='DD4444', make='Audi', model='A4', color='silver')
        # car5 = Car.objects.create(license_plate='EE5555', make='Mercedes', model='C-Class', color='red')
        # car6 = Car.objects.create(license_plate='FF6666', make='Volkswagen', model='Golf', color='green')
        #
        # # Привязываем автомобили к владельцам через Ownership
        # Ownership.objects.create(owner=owner1, car=car1, start_date=timezone.now())
        # Ownership.objects.create(owner=owner2, car=car2, start_date=timezone.now())
        # Ownership.objects.create(owner=owner3, car=car3, start_date=timezone.now())
        # Ownership.objects.create(owner=owner4, car=car4, start_date=timezone.now())
        # Ownership.objects.create(owner=owner5, car=car5, start_date=timezone.now())
        # Ownership.objects.create(owner=owner6, car=car6, start_date=timezone.now())
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data)
# Owner 列表视图
def owner_list(request):
    owners = Owner.objects.all()


    return render(request, 'owner_list.html', {'owners': owners})

# Owner 详细信息视图
def owner_detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'owner_detail.html', {'owner': owner})

# Owner 创建视图
def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_detail', owner_id=owner.pk)
    else:
        form = OwnerForm()
    return render(request, 'owner_form.html', {'form': form})

# Owner 更新视图
def owner_update(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_detail', owner_id=owner.pk)
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'owner_form.html', {'form': form})

# Owner 删除视图
@require_POST
def owner_delete(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    owner.delete()
    return redirect('owner_list')

def ownership_list(request):
    ownerships = Ownership.objects.all()
    return render(request, 'ownership_list.html', {'ownerships': ownerships})
