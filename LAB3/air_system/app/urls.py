from django.urls import path, include
from rest_framework import routers
from .views import FlightViewSet, PassengerViewSet, BookingViewSet, CommentViewSet,LoginView

router = routers.DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'passengers', PassengerViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'comments', CommentViewSet)
urlpatterns = [
    # ... 其他 URLconf 声明
    path('api/', include(router.urls)),
path('api/login/', LoginView.as_view()),
]
