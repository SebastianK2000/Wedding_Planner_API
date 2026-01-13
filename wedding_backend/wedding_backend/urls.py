from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register(r'venues', views.VenueViewSet)
router.register(r'music', views.MusicViewSet)
router.register(r'photographers', views.PhotographerViewSet)
router.register(r'florists', views.FloristViewSet)
router.register(r'transport', views.TransportViewSet)
router.register(r'guests', views.GuestViewSet, basename='guests')
router.register(r'guest-tables', views.GuestTableViewSet, basename='guest-tables')
router.register(r'budget-items', views.BudgetViewSet, basename='budget-items') 
router.register(r'tasks', views.TaskViewSet, basename='tasks')
router.register(r'timeline', views.TimelineViewSet, basename='timeline')
router.register(r'user-favorites', views.UserFavoriteViewSet, basename='user-favorites')
router.register(r'budget-categories', views.BudgetCategoryViewSet, basename='budget-categories') 
router.register(r'dietary-preferences', views.DietaryPreferenceViewSet)
router.register(r'guest-statuses', views.GuestStatusViewSet)
router.register(r'musician-types', views.MusicianTypeViewSet)
router.register(r'photographer-styles', views.PhotographerStyleViewSet)
router.register(r'task-priorities', views.TaskPriorityViewSet)
router.register(r'timeline-groups', views.TimelineGroupViewSet)
router.register(r'transport-types', views.TransportTypeViewSet)
router.register(r'venue-features', views.VenueFeatureViewSet)
router.register(r'musician-type-map', views.MusiciansTypeMapViewSet)
router.register(r'photographer-style-map', views.PhotographerStyleMapViewSet)
router.register(r'venue-feature-map', views.VenueFeatureMapViewSet)
router.register(r'company-info', views.CompanyInfoViewSet)
router.register(r'contact-messages', views.ContactMessageViewSet)
router.register(r'faq-categories', views.FaqCategoryViewSet)
router.register(r'faq-items', views.FaqItemViewSet)
router.register(r'home-sections', views.HomeSectionViewSet)
router.register(r'newsletter', views.NewsletterSubscriberViewSet)
router.register(r'social-links', views.SocialLinkViewSet)
router.register(r'static-pages', views.StaticPageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', views.LoginView.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)