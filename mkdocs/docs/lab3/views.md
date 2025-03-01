# Views Configuration

## Overview

Experiment 3 implements API views using Django REST Framework's ViewSets and APIViews for the flight booking system.

## ViewSet Classes

### Flight ViewSet

```python
from rest_framework import viewsets
from .models import Flight
from .serializers import FlightSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
```

### Passenger ViewSet

```python
from .models import Passenger
from .serializers import PassengerSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
```

### Booking ViewSet

```python
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
```

### Comment ViewSet

```python
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
```

## API Views

### Login View

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            passenger = Passenger.objects.get(
                username=username,
                password=password
            )
            serializer = PassengerSerializer(passenger)
            return Response(serializer.data)
        except Passenger.DoesNotExist:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
```

## ViewSet Features

1. CRUD Operations
   - List objects (GET)
   - Create objects (POST)
   - Retrieve objects (GET)
   - Update objects (PUT/PATCH)
   - Delete objects (DELETE)

2. Serializer Integration
   - Automatic serialization
   - Deserialization
   - Validation

3. Query Set Management
   - Filtering
   - Ordering
   - Pagination

4. Response Handling
   - JSON responses
   - Status codes
   - Error messages

## API Authentication

1. Login Process
   - Username/password validation
   - Error handling
   - Response formatting

2. Session Management
   - Session creation
   - Session validation
   - Session cleanup

## Response Examples

### Successful Response

```json
{
    "id": 1,
    "flight_number": "CA123",
    "airline": "Air China",
    "departure_time": "2024-02-28T10:00:00Z",
    "arrival_time": "2024-02-28T12:00:00Z",
    "flight_type": "DEP",
    "gate_number": "A1"
}
```

### Error Response

```json
{
    "error": "Please provide both username and password"
}
``` 