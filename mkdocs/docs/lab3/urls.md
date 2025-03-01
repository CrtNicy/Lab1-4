# URL Configuration

## Overview

Experiment 3 uses Django REST Framework's router system to automatically generate API URLs for the flight booking system.

## Main URL Configuration

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'flights', views.FlightViewSet)
router.register(r'passengers', views.PassengerViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

## API Endpoints

### Flight Endpoints
- `GET /api/flights/`: List all flights
- `POST /api/flights/`: Create new flight
- `GET /api/flights/{id}/`: Retrieve flight details
- `PUT /api/flights/{id}/`: Update flight information
- `PATCH /api/flights/{id}/`: Partially update flight
- `DELETE /api/flights/{id}/`: Delete flight

### Passenger Endpoints
- `GET /api/passengers/`: List all passengers
- `POST /api/passengers/`: Register new passenger
- `GET /api/passengers/{id}/`: Retrieve passenger details
- `PUT /api/passengers/{id}/`: Update passenger information
- `PATCH /api/passengers/{id}/`: Partially update passenger
- `DELETE /api/passengers/{id}/`: Delete passenger

### Booking Endpoints
- `GET /api/bookings/`: List all bookings
- `POST /api/bookings/`: Create new booking
- `GET /api/bookings/{id}/`: Retrieve booking details
- `PUT /api/bookings/{id}/`: Update booking
- `PATCH /api/bookings/{id}/`: Partially update booking
- `DELETE /api/bookings/{id}/`: Delete booking

### Comment Endpoints
- `GET /api/comments/`: List all comments
- `POST /api/comments/`: Create new comment
- `GET /api/comments/{id}/`: Retrieve comment details
- `PUT /api/comments/{id}/`: Update comment
- `PATCH /api/comments/{id}/`: Partially update comment
- `DELETE /api/comments/{id}/`: Delete comment

## Usage Examples

### HTTP Request Examples

1. List Flights
```http
GET /api/flights/
Accept: application/json
```

2. Create Booking
```http
POST /api/bookings/
Content-Type: application/json

{
    "passenger": 1,
    "flight": 2,
    "seat_number": "12A"
}
```

3. Update Flight Information
```http
PUT /api/flights/1/
Content-Type: application/json

{
    "flight_number": "CA123",
    "departure": "Beijing",
    "destination": "Shanghai",
    "departure_time": "2024-03-20T10:00:00Z",
    "arrival_time": "2024-03-20T12:00:00Z",
    "price": "599.99"
}
```

4. Delete Booking
```http
DELETE /api/bookings/1/
```

## CORS Configuration

To support cross-origin requests, add the following settings in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

# Allow all origins in development
CORS_ALLOW_ALL_ORIGINS = True 