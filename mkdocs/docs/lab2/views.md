# Django Views Configuration

## Overview

Experiment 2 implements various views for the car ownership management system, providing CRUD operations for owners, cars, and ownership records.

## View Classes and Functions

### Owner Views

#### List View
```python
def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'owner_list.html', {'owners': owners})
```

#### Detail View
```python
def owner_detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'owner_detail.html', {'owner': owner})
```

#### Create View
```python
def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_detail', owner_id=owner.id)
    else:
        form = OwnerForm()
    return render(request, 'owner_form.html', {'form': form})
```

#### Update View
```python
def owner_update(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_detail', owner_id=owner.id)
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'owner_form.html', {'form': form})
```

#### Delete View
```python
@require_POST
def owner_delete(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    owner.delete()
    return redirect('owner_list')
```

### Car Owner Create and List View
```python
class CarOwnerCreateAndListView(View):
    def get(self, request):
        owners = Owner.objects.all()
        return JsonResponse({'owners': [
            {'id': owner.id, 'name': str(owner)}
            for owner in owners
        ]})

    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
            last_name=data['last_name'],
            first_name=data['first_name'],
            birth_date=data['birth_date']
        )
        return JsonResponse({
            'id': owner.id,
            'name': str(owner)
        }, status=201)
```

## View Features

1. CRUD Operations
   - Create: Form handling and data validation
   - Read: List and detail views
   - Update: Form pre-population and validation
   - Delete: Object removal with confirmation

2. Response Types
   - HTML Templates
   - JSON Responses (API)
   - Redirects

3. Error Handling
   - 404 for missing objects
   - Form validation errors
   - Exception handling

4. HTTP Methods
   - GET for retrieving data
   - POST for creating/updating
   - DELETE for removing records

## Template Integration

1. Template Context
   - Object lists
   - Single objects
   - Form instances
   - Error messages

2. Template Files
   - `owner_list.html`
   - `owner_detail.html`
   - `owner_form.html`

## URL Patterns

```python
urlpatterns = [
    path('', owner_list, name='owner_list'),
    path('<int:owner_id>/', owner_detail, name='owner_detail'),
    path('create/', owner_create, name='owner_create'),
    path('<int:owner_id>/update/', owner_update, name='owner_update'),
    path('<int:owner_id>/delete/', owner_delete, name='owner_delete'),
    path('api/owners/', CarOwnerCreateAndListView.as_view(), name='api_owners'),
]
``` 