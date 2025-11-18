from rest_framework import viewsets, status, views
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import (
    Users, Venues, Musicians, Photographers, Florists, Transportvehicles,
    Guests, Budgetitems, Tasks, Timelineevents
)
from .serializers import (
    UserRegistrationSerializer, UserLoginSerializer,
    VenueSerializer, MusicSerializer, PhotographerSerializer, FloristSerializer, TransportSerializer,
    GuestSerializer, BudgetSerializer, TaskSerializer, TimelineSerializer
)

# --- AUTH VIEWS ---
class RegisterView(views.APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Użytkownik utworzony pomyślnie"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                return Response({"error": "Błędny email lub hasło"}, status=status.HTTP_401_UNAUTHORIZED)
            
            if check_password(password, user.passwordhash):
                refresh = RefreshToken()
                refresh['user_id'] = user.id
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {'id': user.id, 'email': user.email, 'fullname': user.fullname, 'role': user.role}
                })
            return Response({"error": "Błędny email lub hasło"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- VIEWSETS (KATALOG & PLANER) ---
class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venues.objects.all()
    serializer_class = VenueSerializer

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Musicians.objects.all()
    serializer_class = MusicSerializer

class PhotographerViewSet(viewsets.ModelViewSet):
    queryset = Photographers.objects.all()
    serializer_class = PhotographerSerializer

class FloristViewSet(viewsets.ModelViewSet):
    queryset = Florists.objects.all()
    serializer_class = FloristSerializer

class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transportvehicles.objects.all()
    serializer_class = TransportSerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guests.objects.all()
    serializer_class = GuestSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budgetitems.objects.all()
    serializer_class = BudgetSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class TimelineViewSet(viewsets.ModelViewSet):
    queryset = Timelineevents.objects.all()
    serializer_class = TimelineSerializer