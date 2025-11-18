from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views  # <--- Ważna zmiana importu

router = DefaultRouter()
# Katalog
router.register(r'venues', views.VenueViewSet)
router.register(r'music', views.MusicViewSet)
router.register(r'photographers', views.PhotographerViewSet)
router.register(r'florists', views.FloristViewSet)
router.register(r'transport', views.TransportViewSet)
# Planer
router.register(r'guests', views.GuestViewSet)
router.register(r'budget', views.BudgetViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'timeline', views.TimelineViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', views.LoginView.as_view(), name='login'),
]