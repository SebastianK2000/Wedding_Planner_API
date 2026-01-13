from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import (
    Users, Venues, Musicians, Photographers, Florists, Transportvehicles,
    Guests, Budgetitems, Tasks, Timelineevents,
    Budgetcategories, Companyinfo, Contactmessages, Dietarypreferences,
    Faqcategories, Faqitems, Gueststatuses, Guesttables, Homesections,
    Musiciantypes, Musicians, Musicianstypemap, Newslettersubscribers,
    Photographerstylemap, Photographerstyles, Sociallinks, Staticpages,
    Taskpriorities, Timelinegroups, Transporttypes, Userfavorites,
    Venuefeaturemap, Venuefeatures
)

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


class BudgetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Budgetcategories
        fields = '__all__'


class DietaryPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dietarypreferences
        fields = '__all__'


class GuestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gueststatuses
        fields = '__all__'


class MusicianTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musiciantypes
        fields = '__all__'


class PhotographerStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographerstyles
        fields = '__all__'


class TaskPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskpriorities
        fields = '__all__'


class TimelineGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timelinegroups
        fields = '__all__'


class TransportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporttypes
        fields = '__all__'


class VenueFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venuefeatures
        fields = '__all__'


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


class MusiciansTypeMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicianstypemap
        fields = '__all__'


class PhotographerStyleMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographerstylemap
        fields = '__all__'


class VenueFeatureMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venuefeaturemap
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = '__all__'


class GuestTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guesttables
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


class UserFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userfavorites
        fields = '__all__'


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companyinfo
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactmessages
        fields = '__all__'


class FaqCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqcategories
        fields = '__all__'


class FaqItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqitems
        fields = '__all__'


class HomeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homesections
        fields = '__all__'


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newslettersubscribers
        fields = '__all__'


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sociallinks
        fields = '__all__'


class StaticPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staticpages
        fields = '__all__'