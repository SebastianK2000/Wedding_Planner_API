from django.db import models
from django.contrib.auth.models import BaseUserManager


class Budgetcategories(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'BudgetCategories'


class Budgetitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)
    categoryid = models.ForeignKey(Budgetcategories, models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=200, db_collation='Polish_CI_AS')
    plannedamount = models.DecimalField(db_column='PlannedAmount', max_digits=10, decimal_places=2, blank=True, null=True)
    actualamount = models.DecimalField(db_column='ActualAmount', max_digits=10, decimal_places=2, blank=True, null=True)
    ispaid = models.BooleanField(db_column='IsPaid', blank=True, null=True)
    notes = models.TextField(db_column='Notes', db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BudgetItems'


class Companyinfo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    email = models.CharField(db_column='Email', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)
    phone = models.CharField(db_column='Phone', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)
    workinghours = models.CharField(db_column='WorkingHours', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)
    workmode = models.CharField(db_column='WorkMode', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CompanyInfo'


class Contactmessages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    sendername = models.CharField(db_column='SenderName', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)
    senderemail = models.CharField(db_column='SenderEmail', max_length=200, db_collation='Polish_CI_AS', blank=True, null=True)
    topic = models.CharField(db_column='Topic', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)
    message = models.TextField(db_column='Message', db_collation='Polish_CI_AS', blank=True, null=True)
    isread = models.BooleanField(db_column='IsRead', blank=True, null=True)
    sentat = models.DateTimeField(db_column='SentAt', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ContactMessages'


class Dietarypreferences(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'DietaryPreferences'


class Faqcategories(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FaqCategories'


class Faqitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    categoryid = models.ForeignKey(Faqcategories, models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)
    question = models.CharField(db_column='Question', max_length=300, db_collation='Polish_CI_AS')
    answer = models.TextField(db_column='Answer', db_collation='Polish_CI_AS')
    isvisible = models.BooleanField(db_column='IsVisible', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FaqItems'


class Florists(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    companyname = models.CharField(db_column='CompanyName', max_length=200, db_collation='Polish_CI_AS')
    title = models.CharField(db_column='Title', max_length=200, db_collation='Polish_CI_AS', blank=True, null=True)
    city = models.CharField(db_column='City', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)
    pricefrom = models.DecimalField(db_column='PriceFrom', max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(db_column='Description', db_collation='Polish_CI_AS', blank=True, null=True)
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Florists'


class Gueststatuses(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'GuestStatuses'


class Guesttables(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)
    tablename = models.CharField(db_column='TableName', max_length=50, db_collation='Polish_CI_AS')
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GuestTables'


class Guests(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)
    fullname = models.CharField(db_column='FullName', max_length=200, db_collation='Polish_CI_AS')
    side = models.CharField(db_column='Side', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)
    statusid = models.ForeignKey(Gueststatuses, models.DO_NOTHING, db_column='StatusId', blank=True, null=True)
    tableid = models.ForeignKey(Guesttables, models.DO_NOTHING, db_column='TableId', blank=True, null=True)
    dietid = models.ForeignKey(Dietarypreferences, models.DO_NOTHING, db_column='DietId', blank=True, null=True)
    plusone = models.BooleanField(db_column='PlusOne', blank=True, null=True)
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='Polish_CI_AS', blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=200, db_collation='Polish_CI_AS', blank=True, null=True)
    notes = models.TextField(db_column='Notes', db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Guests'


class Homesections(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    sectionkey = models.CharField(db_column='SectionKey', unique=True, max_length=50, db_collation='Polish_CI_AS')
    title = models.CharField(db_column='Title', max_length=200, db_collation='Polish_CI_AS', blank=True, null=True)
    subtitle = models.CharField(db_column='Subtitle', max_length=500, db_collation='Polish_CI_AS', blank=True, null=True)
    buttontext = models.CharField(db_column='ButtonText', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HomeSections'


class Musiciantypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'MusicianTypes'


class Musicians(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=200, db_collation='Polish_CI_AS')
    city = models.CharField(db_column='City', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)
    pricefrom = models.DecimalField(db_column='PriceFrom', max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(db_column='Description', db_collation='Polish_CI_AS', blank=True, null=True)
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)
    rating = models.DecimalField(db_column='Rating', max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Musicians'


class Musicianstypemap(models.Model):
    musicianid = models.ForeignKey(Musicians, models.DO_NOTHING, db_column='MusicianId', primary_key=True)
    typeid = models.ForeignKey(Musiciantypes, models.DO_NOTHING, db_column='TypeId')

    class Meta:
        managed = False
        db_table = 'MusiciansTypeMap'
        unique_together = (('musicianid', 'typeid'),)


class Newslettersubscribers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    email = models.CharField(db_column='Email', unique=True, max_length=255, db_collation='Polish_CI_AS')
    subscribedat = models.DateTimeField(db_column='SubscribedAt', blank=True, null=True)
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NewsletterSubscribers'


class Photographerstylemap(models.Model):
    photographerid = models.ForeignKey('Photographers', models.DO_NOTHING, db_column='PhotographerId', primary_key=True)
    styleid = models.ForeignKey('Photographerstyles', models.DO_NOTHING, db_column='StyleId')

    class Meta:
        managed = False
        db_table = 'PhotographerStyleMap'
        unique_together = (('photographerid', 'styleid'),)


class Photographerstyles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'PhotographerStyles'


class Photographers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=200, db_collation='Polish_CI_AS')
    city = models.CharField(db_column='City', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)
    pricefrom = models.DecimalField(db_column='PriceFrom', max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(db_column='Description', db_collation='Polish_CI_AS', blank=True, null=True)
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Photographers'


class Sociallinks(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    platformname = models.CharField(db_column='PlatformName', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)
    url = models.CharField(db_column='Url', max_length=255, db_collation='Polish_CI_AS')
    iconname = models.CharField(db_column='IconName', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SocialLinks'


class Staticpages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    pagekey = models.CharField(db_column='PageKey', unique=True, max_length=50, db_collation='Polish_CI_AS')
    title = models.CharField(db_column='Title', max_length=200, db_collation='Polish_CI_AS')
    content = models.TextField(db_column='Content', db_collation='Polish_CI_AS', blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StaticPages'


class Taskpriorities(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50, db_collation='Polish_CI_AS')
    colorcode = models.CharField(db_column='ColorCode', max_length=20, db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskPriorities'


class Tasks(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=255, db_collation='Polish_CI_AS')
    categoryid = models.ForeignKey(Budgetcategories, models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)
    priorityid = models.ForeignKey(Taskpriorities, models.DO_NOTHING, db_column='PriorityId', blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=20, db_collation='Polish_CI_AS', blank=True, null=True)
    duedate = models.DateField(db_column='DueDate', blank=True, null=True)
    notes = models.TextField(db_column='Notes', db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tasks'


class Timelineevents(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)
    groupid = models.ForeignKey('Timelinegroups', models.DO_NOTHING, db_column='GroupId', blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=200, db_collation='Polish_CI_AS')
    details = models.TextField(db_column='Details', db_collation='Polish_CI_AS', blank=True, null=True)
    iscompleted = models.BooleanField(db_column='IsCompleted', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TimelineEvents'


class Timelinegroups(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')
    orderindex = models.IntegerField(db_column='OrderIndex')

    class Meta:
        managed = False
        db_table = 'TimelineGroups'


class Transporttypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'TransportTypes'


class Transportvehicles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    typeid = models.ForeignKey(Transporttypes, models.DO_NOTHING, db_column='TypeId', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=200, db_collation='Polish_CI_AS')
    city = models.CharField(db_column='City', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)
    pricefrom = models.DecimalField(db_column='PriceFrom', max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(db_column='Description', db_collation='Polish_CI_AS', blank=True, null=True)
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TransportVehicles'


class Userfavorites(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)
    serviceid = models.IntegerField(db_column='ServiceId')
    servicetype = models.CharField(db_column='ServiceType', max_length=50, db_collation='Polish_CI_AS')
    savedat = models.DateTimeField(db_column='SavedAt', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserFavorites'

class UsersManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email jest wymagany')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'Admin')
        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)


class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    email = models.CharField(db_column='Email', unique=True, max_length=255, db_collation='Polish_CI_AS')
    password = models.TextField(db_column='PasswordHash', db_collation='Polish_CI_AS') 
    fullname = models.CharField(db_column='FullName', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)
    role = models.CharField(db_column='Role', max_length=20, db_collation='Polish_CI_AS', blank=True, null=True)
    weddingdate = models.DateField(db_column='WeddingDate', blank=True, null=True)
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)

    objects = UsersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname'] 

    def set_password(self, raw_password):
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    @property
    def is_anonymous(self): return False
    @property
    def is_authenticated(self): return True
    @property
    def is_active(self): return True
    @property
    def is_staff(self): return self.role == 'Admin'
    @property
    def is_superuser(self): return self.role == 'Admin'

    def has_perm(self, perm, obj=None): return self.is_staff
    def has_module_perms(self, app_label): return self.is_staff
    @property
    def last_login(self): return None

    class Meta:
        managed = False
        db_table = 'Users'


class Venuefeaturemap(models.Model):
    venueid = models.ForeignKey('Venues', models.DO_NOTHING, db_column='VenueId', primary_key=True)
    featureid = models.ForeignKey('Venuefeatures', models.DO_NOTHING, db_column='FeatureId')

    class Meta:
        managed = False
        db_table = 'VenueFeatureMap'
        unique_together = (('venueid', 'featureid'),)


class Venuefeatures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'VenueFeatures'


class Venues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=200, db_collation='Polish_CI_AS')
    city = models.CharField(db_column='City', max_length=100, db_collation='Polish_CI_AS')
    capacity = models.IntegerField(db_column='Capacity')
    priceperperson = models.DecimalField(db_column='PricePerPerson', max_digits=10, decimal_places=2)
    description = models.TextField(db_column='Description', db_collation='Polish_CI_AS', blank=True, null=True)
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)
    rating = models.DecimalField(db_column='Rating', max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Venues'