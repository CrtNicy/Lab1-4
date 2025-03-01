# Django Admin Interface Configuration

## Overview

Experiment 2 configures the Django admin interface for the car ownership management system, allowing administrators to easily manage owners, cars, driving licenses, and ownership information.

## Admin Class Configuration

### Owner Admin

```python
from django.contrib import admin
from .models import Owner, Car, DrivingLicense, Ownership

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date')
    search_fields = ('last_name', 'first_name')
    ordering = ('last_name', 'first_name')
```

### Car Admin

```python
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'make', 'model', 'color')
    list_filter = ('make', 'model')
    search_fields = ('license_plate', 'make', 'model')
```

### DrivingLicense Admin

```python
@admin.register(DrivingLicense)
class DrivingLicenseAdmin(admin.ModelAdmin):
    list_display = ('owner', 'license_number', 'type', 'issue_date')
    list_filter = ('type', 'issue_date')
    search_fields = ('owner__last_name', 'license_number')
    date_hierarchy = 'issue_date'
```

### Ownership Admin

```python
@admin.register(Ownership)
class OwnershipAdmin(admin.ModelAdmin):
    list_display = ('owner', 'car', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('owner__last_name', 'car__license_plate')
    date_hierarchy = 'start_date'
```

## Feature Description

1. Owner Management
   - Display name and birth date
   - Support name search
   - Sort by last name and first name

2. Car Management
   - Display license plate, make, model, and color
   - Filter by make and model
   - Support license plate and car model search

3. DrivingLicense Management
   - Display owner, license number, type, and issue date
   - Filter by type and issue date
   - Support owner name and license number search
   - Date hierarchy navigation

4. Ownership Management
   - Display owner, car, and ownership dates
   - Filter by dates
   - Support owner and license plate search
   - Date hierarchy navigation

## Admin Interface Features

1. List Display
   - Custom display fields
   - Sorting functionality
   - Pagination

2. Filtering
   - Sidebar filters
   - Date hierarchy navigation
   - Search box

3. Editing
   - Add new records
   - Modify existing records
   - Delete records
   - Batch operations

4. Permission Control
   - User group-based permissions
   - Operation control
   - Field-level permissions

## Usage Instructions

1. Access Admin Interface
   ```
   http://your-domain/admin/
   ```

2. Login as Administrator
   - Use superuser account
   - Or use account with admin privileges

3. Select Model to Manage
   - Owner Management
   - Car Management
   - DrivingLicense Management
   - Ownership Management

4. Perform Operations
   - View lists
   - Add records
   - Modify records
   - Delete records
   - Batch operations 