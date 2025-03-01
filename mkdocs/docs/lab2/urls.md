# URL Configuration - Car Ownership System

## Overview

Experiment 2 implements URL routing for the car ownership management system, defining patterns for various views and operations.

## URL Configuration

### Main URL Configuration

```python
from django.urls import path
from . import views

urlpatterns = [
    # Owner URLs
    path('', views.owner_list, name='owner_list'),
    path('<int:owner_id>/', views.owner_detail, name='owner_detail'),
    path('create/', views.owner_create, name='owner_create'),
    path('<int:owner_id>/update/', views.owner_update, name='owner_update'),
    path('<int:owner_id>/delete/', views.owner_delete, name='owner_delete'),
    
    # Car URLs
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('cars/create/', views.car_create, name='car_create'),
    path('cars/<int:car_id>/update/', views.car_update, name='car_update'),
    path('cars/<int:car_id>/delete/', views.car_delete, name='car_delete'),
    
    # DrivingLicense URLs
    path('licenses/', views.license_list, name='license_list'),
    path('licenses/<int:license_id>/', views.license_detail, name='license_detail'),
    path('licenses/create/', views.license_create, name='license_create'),
    path('licenses/<int:license_id>/update/', views.license_update, name='license_update'),
    path('licenses/<int:license_id>/delete/', views.license_delete, name='license_delete'),
    
    # Ownership URLs
    path('ownerships/', views.ownership_list, name='ownership_list'),
    path('ownerships/create/', views.ownership_create, name='ownership_create'),
    path('ownerships/<int:ownership_id>/update/', views.ownership_update, name='ownership_update'),
    path('ownerships/<int:ownership_id>/delete/', views.ownership_delete, name='ownership_delete'),
]
```

## URL Patterns

### Owner Management

1. List View
   - URL: `/`
   - Name: `owner_list`
   - View: `owner_list`
   - Method: GET

2. Detail View
   - URL: `/<owner_id>/`
   - Name: `owner_detail`
   - View: `owner_detail`
   - Method: GET

3. Create View
   - URL: `/create/`
   - Name: `owner_create`
   - View: `owner_create`
   - Methods: GET, POST

4. Update View
   - URL: `/<owner_id>/update/`
   - Name: `owner_update`
   - View: `owner_update`
   - Methods: GET, POST

5. Delete View
   - URL: `/<owner_id>/delete/`
   - Name: `owner_delete`
   - View: `owner_delete`
   - Method: POST

### Car Management

1. List View
   - URL: `/cars/`
   - Name: `car_list`
   - View: `car_list`
   - Method: GET

2. Detail View
   - URL: `/cars/<car_id>/`
   - Name: `car_detail`
   - View: `car_detail`
   - Method: GET

3. Create View
   - URL: `/cars/create/`
   - Name: `car_create`
   - View: `car_create`
   - Methods: GET, POST

4. Update View
   - URL: `/cars/<car_id>/update/`
   - Name: `car_update`
   - View: `car_update`
   - Methods: GET, POST

5. Delete View
   - URL: `/cars/<car_id>/delete/`
   - Name: `car_delete`
   - View: `car_delete`
   - Method: POST

### DrivingLicense Management

1. List View
   - URL: `/licenses/`
   - Name: `license_list`
   - View: `license_list`
   - Method: GET

2. Detail View
   - URL: `/licenses/<license_id>/`
   - Name: `license_detail`
   - View: `license_detail`
   - Method: GET

3. Create View
   - URL: `/licenses/create/`
   - Name: `license_create`
   - View: `license_create`
   - Methods: GET, POST

4. Update View
   - URL: `/licenses/<license_id>/update/`
   - Name: `license_update`
   - View: `license_update`
   - Methods: GET, POST

5. Delete View
   - URL: `/licenses/<license_id>/delete/`
   - Name: `license_delete`
   - View: `license_delete`
   - Method: POST

### Ownership Management

1. List View
   - URL: `/ownerships/`
   - Name: `ownership_list`
   - View: `ownership_list`
   - Method: GET

2. Create View
   - URL: `/ownerships/create/`
   - Name: `ownership_create`
   - View: `ownership_create`
   - Methods: GET, POST

3. Update View
   - URL: `/ownerships/<ownership_id>/update/`
   - Name: `ownership_update`
   - View: `ownership_update`
   - Methods: GET, POST

4. Delete View
   - URL: `/ownerships/<ownership_id>/delete/`
   - Name: `ownership_delete`
   - View: `ownership_delete`
   - Method: POST

## URL Features

1. Pattern Types
   - Basic patterns (`/cars/`, `/owners/`)
   - Dynamic segments (`<int:owner_id>`)
   - Named URLs for reverse lookup

2. View Mapping
   - Function-based views
   - CRUD operations
   - List and detail views

3. URL Organization
   - Resource-based grouping
   - Consistent naming
   - RESTful structure

4. URL Names
   - Descriptive naming
   - Reverse URL resolution
   - Template URL references

## Usage Examples

### Template URL Tags

```html
<!-- Link to owner list -->
<a href="{% url 'owner_list' %}">All Owners</a>

<!-- Link to owner detail -->
<a href="{% url 'owner_detail' owner.id %}">View Owner</a>

<!-- Form action URL -->
<form action="{% url 'owner_create' %}" method="post">
```

### View URL Resolution

```python
from django.shortcuts import redirect
from django.urls import reverse

# Redirect to owner detail
return redirect('owner_detail', owner_id=owner.id)

# Get URL by name
url = reverse('owner_list')
``` 