from rest_framework import viewsets, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

# Import wszystkich modeli
from .models import (
    Users, Venues, Musicians, Photographers, Florists, Transportvehicles,
    Guests, Budgetitems, Tasks, Timelineevents,
    Budgetcategories, Companyinfo, Contactmessages, Dietarypreferences,
    Faqcategories, Faqitems, Gueststatuses, Guesttables, Homesections,
    Musiciantypes, Musicianstypemap, Newslettersubscribers,
    Photographerstylemap, Photographerstyles, Sociallinks, Staticpages,
    Taskpriorities, Timelinegroups, Transporttypes, Userfavorites,
    Venuefeaturemap, Venuefeatures
)

# Import wszystkich serializerów
from .serializers import (
    UserRegistrationSerializer, UserLoginSerializer,
    VenueSerializer, MusicSerializer, PhotographerSerializer, FloristSerializer, TransportSerializer,
    GuestSerializer, BudgetSerializer, TaskSerializer, TimelineSerializer,
    BudgetCategorySerializer, CompanyInfoSerializer, ContactMessageSerializer,
    DietaryPreferenceSerializer, FaqCategorySerializer, FaqItemSerializer,
    GuestStatusSerializer, GuestTableSerializer, HomeSectionSerializer,
    MusicianTypeSerializer, MusiciansTypeMapSerializer, NewsletterSubscriberSerializer,
    PhotographerStyleMapSerializer, PhotographerStyleSerializer, SocialLinkSerializer,
    StaticPageSerializer, TaskPrioritySerializer, TimelineGroupSerializer,
    TransportTypeSerializer, UserFavoriteSerializer, VenueFeatureMapSerializer,
    VenueFeatureSerializer
)

# --- AUTH VIEWS (Rejestracja i Logowanie) ---
class RegisterView(views.APIView):
    permission_classes = [AllowAny] # Rejestracja musi być publiczna

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Użytkownik utworzony pomyślnie"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                return Response({"error": "Błędny email lub hasło"}, status=status.HTTP_401_UNAUTHORIZED)
            
            if check_password(password, user.password):
                refresh = RefreshToken()
                refresh['user_id'] = user.id
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {'id': user.id, 'email': user.email, 'fullname': user.fullname, 'role': user.role}
                })
            return Response({"error": "Błędny email lub hasło"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Guests.objects.filter(userid=self.request.user)

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)

class GuestTableViewSet(viewsets.ModelViewSet):
    serializer_class = GuestTableSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Guesttables.objects.filter(userid=self.request.user)

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Budgetitems.objects.filter(userid=self.request.user)

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tasks.objects.filter(userid=self.request.user)

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)

class TimelineViewSet(viewsets.ModelViewSet):
    serializer_class = TimelineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Timelineevents.objects.filter(userid=self.request.user)

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)

class UserFavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = UserFavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Userfavorites.objects.filter(userid=self.request.user)

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)

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

class BudgetCategoryViewSet(viewsets.ModelViewSet):
    queryset = Budgetcategories.objects.all()
    serializer_class = BudgetCategorySerializer

class DietaryPreferenceViewSet(viewsets.ModelViewSet):
    queryset = Dietarypreferences.objects.all()
    serializer_class = DietaryPreferenceSerializer

class GuestStatusViewSet(viewsets.ModelViewSet):
    queryset = Gueststatuses.objects.all()
    serializer_class = GuestStatusSerializer

class MusicianTypeViewSet(viewsets.ModelViewSet):
    queryset = Musiciantypes.objects.all()
    serializer_class = MusicianTypeSerializer

class PhotographerStyleViewSet(viewsets.ModelViewSet):
    queryset = Photographerstyles.objects.all()
    serializer_class = PhotographerStyleSerializer

class TaskPriorityViewSet(viewsets.ModelViewSet):
    queryset = Taskpriorities.objects.all()
    serializer_class = TaskPrioritySerializer

class TimelineGroupViewSet(viewsets.ModelViewSet):
    queryset = Timelinegroups.objects.all()
    serializer_class = TimelineGroupSerializer

class TransportTypeViewSet(viewsets.ModelViewSet):
    queryset = Transporttypes.objects.all()
    serializer_class = TransportTypeSerializer

class VenueFeatureViewSet(viewsets.ModelViewSet):
    queryset = Venuefeatures.objects.all()
    serializer_class = VenueFeatureSerializer

class MusiciansTypeMapViewSet(viewsets.ModelViewSet):
    queryset = Musicianstypemap.objects.all()
    serializer_class = MusiciansTypeMapSerializer

class PhotographerStyleMapViewSet(viewsets.ModelViewSet):
    queryset = Photographerstylemap.objects.all()
    serializer_class = PhotographerStyleMapSerializer

class VenueFeatureMapViewSet(viewsets.ModelViewSet):
    queryset = Venuefeaturemap.objects.all()
    serializer_class = VenueFeatureMapSerializer

class CompanyInfoViewSet(viewsets.ModelViewSet):
    queryset = Companyinfo.objects.all()
    serializer_class = CompanyInfoSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = Contactmessages.objects.all()
    serializer_class = ContactMessageSerializer

class FaqCategoryViewSet(viewsets.ModelViewSet):
    queryset = Faqcategories.objects.all()
    serializer_class = FaqCategorySerializer

class FaqItemViewSet(viewsets.ModelViewSet):
    queryset = Faqitems.objects.all()
    serializer_class = FaqItemSerializer

class HomeSectionViewSet(viewsets.ModelViewSet):
    queryset = Homesections.objects.all()
    serializer_class = HomeSectionSerializer

class NewsletterSubscriberViewSet(viewsets.ModelViewSet):
    queryset = Newslettersubscribers.objects.all()
    serializer_class = NewsletterSubscriberSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = Sociallinks.objects.all()
    serializer_class = SocialLinkSerializer

class StaticPageViewSet(viewsets.ModelViewSet):
    queryset = Staticpages.objects.all()
    serializer_class = StaticPageSerializer