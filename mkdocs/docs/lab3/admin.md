# Admin Configuration

## Overview

Experiment 3 configures the Django admin interface for managing the flight booking system.

## Admin Classes

### Flight Admin

```python
from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'flight_number',
        'airline',
        'departure_time',
        'arrival_time',
        'flight_type',
        'gate_number'
    )
    list_filter = ('airline', 'flight_type')
    search_fields = ('flight_number', 'airline')
    date_hierarchy = 'departure_time'
```

### Passenger Admin

```python
from .models import Passenger

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)
```

### Booking Admin

```python
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('passenger', 'flight', 'seat_number')
    list_filter = ('flight',)
    search_fields = (
        'passenger__username',
        'flight__flight_number',
        'seat_number'
    )
```

### Comment Admin

```python
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'flight',
        'commenter_name',
        'rating',
        'comment_date'
    )
    list_filter = ('rating', 'comment_date')
    search_fields = ('flight__flight_number', 'commenter_name')
    date_hierarchy = 'comment_date'
```

## Admin Features

1. List Display
   - Customized column display
   - Sortable columns
   - Clickable links
   - Date formatting

2. Filtering
   - Filter by fields
   - Date hierarchy
   - Search functionality
   - Advanced filtering

3. Search
   - Field-based search
   - Related field search
   - Case-insensitive search
   - Multiple field search

4. Date Navigation
   - Date hierarchy
   - Date range filtering
   - Date-based navigation

## Admin Interface

1. Model Management
   - Add new records
   - Edit existing records
   - Delete records
   - Bulk actions

2. List Views
   - Pagination
   - Column sorting
   - Filter sidebar
   - Search box

3. Detail Views
   - Form layout
   - Field grouping
   - Related objects
   - Inline editing

4. Actions
   - Built-in actions
   - Custom actions
   - Bulk operations
   - Action confirmation

## Usage Instructions

1. Accessing Admin
   ```
   http://localhost:8000/admin/
   ```

2. Authentication
   - Login required
   - Staff status required
   - Permission checks

3. Managing Records
   - Create records
   - Update records
   - Delete records
   - Search records

4. Filtering Data
   - Use filter sidebar
   - Search functionality
   - Date navigation
   - Advanced filters 