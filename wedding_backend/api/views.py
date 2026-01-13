from rest_framework import viewsets, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

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

from .serializers import (
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


class RegisterView(views.APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        try:
            data = request.data
            email = data.get('email')
            password = data.get('password')
            fullname = data.get('fullname')
            role = data.get('role', 'User')

            if not email or not password:
                return Response({'error': 'Email i hasło są wymagane'}, status=status.HTTP_400_BAD_REQUEST)

            if Users.objects.filter(email=email).exists():
                return Response({'error': 'Użytkownik o takim adresie email już istnieje'}, status=status.HTTP_400_BAD_REQUEST)

            user = Users.objects.create_user(
                email=email,
                password=password,
                fullname=fullname,
                role=role
            )

            return Response({
                "message": "Użytkownik utworzony pomyślnie", 
                "id": user.id
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(f"BŁĄD REJESTRACJI: {str(e)}")
            return Response({'error': 'Wystąpił błąd serwera podczas rejestracji.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
             return Response({'error': 'Podaj email i hasło'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Users.objects.get(email=email)
            
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                
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
                return Response({"error": "Błędne hasło"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Users.DoesNotExist:
            return Response({"error": "Użytkownik o podanym emailu nie istnieje"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"BŁĄD LOGOWANIA: {str(e)}")
            return Response({'error': 'Błąd serwera logowania'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venues.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [AllowAny]


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Musicians.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [AllowAny]


class PhotographerViewSet(viewsets.ModelViewSet):
    queryset = Photographers.objects.all()
    serializer_class = PhotographerSerializer
    permission_classes = [AllowAny]


class FloristViewSet(viewsets.ModelViewSet):
    queryset = Florists.objects.all()
    serializer_class = FloristSerializer
    permission_classes = [AllowAny]


class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transportvehicles.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [AllowAny]


class TimelineGroupViewSet(viewsets.ModelViewSet):
    queryset = Timelinegroups.objects.all()
    serializer_class = TimelineGroupSerializer
    permission_classes = [AllowAny]


class TimelineViewSet(viewsets.ModelViewSet):
    serializer_class = TimelineSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):

        return Timelineevents.objects.all()

    def perform_create(self, serializer):

        if self.request.user.is_authenticated:
            serializer.save(userid=self.request.user)
        else:
            first_user = Users.objects.first()

            if first_user:
                serializer.save(userid=first_user)
            else:
                serializer.save()


class GuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): return Guests.objects.filter(userid=self.request.user)

    def perform_create(self, serializer): serializer.save(userid=self.request.user)


class GuestTableViewSet(viewsets.ModelViewSet):
    serializer_class = GuestTableSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): return Guesttables.objects.filter(userid=self.request.user)

    def perform_create(self, serializer): serializer.save(userid=self.request.user)


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

    def get_queryset(self): return Tasks.objects.filter(userid=self.request.user)

    def perform_create(self, serializer): serializer.save(userid=self.request.user)


class UserFavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = UserFavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): return Userfavorites.objects.filter(userid=self.request.user)

    def perform_create(self, serializer): serializer.save(userid=self.request.user)


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