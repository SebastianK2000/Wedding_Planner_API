from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import (
    Users, Venues, Musicians, Photographers, Florists, Transportvehicles,
    Guests, Budgetitems, Tasks, Timelineevents
)

# --- AUTH ---
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['email', 'fullname', 'password']

    def create(self, validated_data):
        validated_data['passwordhash'] = make_password(validated_data.pop('password'))
        validated_data['role'] = 'User' 
        return super().create(validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

# --- KATALOG USŁUG ---
class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venues
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicians
        fields = '__all__'

class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographers
        fields = '__all__'

class FloristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Florists
        fields = '__all__'

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportvehicles
        fields = '__all__'

# --- PLANER UŻYTKOWNIKA ---
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budgetitems
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timelineevents
        fields = '__all__'