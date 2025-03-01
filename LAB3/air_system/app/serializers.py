from rest_framework import serializers
from .models import Flight, Passenger, Booking, Comment


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(read_only=True)
    passenger_id = serializers.PrimaryKeyRelatedField(
        source='passenger',
        queryset=Passenger.objects.all(),
        write_only=True
    )
    class Meta:
        model = Booking
        fields = ['id', 'passenger', 'passenger_id', 'flight', 'seat_number']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
