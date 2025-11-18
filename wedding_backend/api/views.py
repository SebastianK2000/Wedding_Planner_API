from django.shortcuts import render
from rest_framework import viewsets, status, views
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Users
from .serializers import UserRegistrationSerializer, UserLoginSerializer
# ... (Twoje poprzednie importy i ViewSety dla Venues, Music itd. zostaw bez zmian)

# --- AUTH VIEWS ---

class RegisterView(views.APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # To wywoła create() z serializera i zapisze w SQL
            return Response({"message": "Użytkownik utworzony pomyślnie"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Szukamy użytkownika w Twojej tabeli Users
            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                return Response({"error": "Błędny email lub hasło"}, status=status.HTTP_401_UNAUTHORIZED)

            # Sprawdzamy hasło (porównujemy jawne z hashem w bazie)
            if check_password(password, user.passwordhash):
                # Generujemy token ręcznie dla Twojego niestandardowego modelu
                refresh = RefreshToken()
                refresh['user_id'] = user.id # Wrzucamy ID użytkownika do tokena
                refresh['role'] = user.role  # Możemy też wrzucić rolę!

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'fullname': user.fullname,
                        'role': user.role
                    }
                })
            else:
                return Response({"error": "Błędny email lub hasło"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)