# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Budgetcategories(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Polish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BudgetCategories'


class Budgetitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Budgetcategories, models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, db_collation='Polish_CI_AS')  # Field name made lowercase.
    plannedamount = models.DecimalField(db_column='PlannedAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    actualamount = models.DecimalField(db_column='ActualAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ispaid = models.BooleanField(db_column='IsPaid', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BudgetItems'


class Companyinfo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    workinghours = models.CharField(db_column='WorkingHours', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    workmode = models.CharField(db_column='WorkMode', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyInfo'


class Contactmessages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sendername = models.CharField(db_column='SenderName', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    senderemail = models.CharField(db_column='SenderEmail', max_length=200, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    topic = models.CharField(db_column='Topic', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField(db_column='Message', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isread = models.BooleanField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.
    sentat = models.DateTimeField(db_column='SentAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactMessages'


class Dietarypreferences(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Polish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DietaryPreferences'


class Faqcategories(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FaqCategories'


class Faqitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Faqcategories, models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=300, db_collation='Polish_CI_AS')  # Field name made lowercase.
    answer = models.TextField(db_column='Answer', db_collation='Polish_CI_AS')  # Field name made lowercase.
    isvisible = models.BooleanField(db_column='IsVisible', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FaqItems'


class Florists(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=200, db_collation='Polish_CI_AS')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricefrom = models.DecimalField(db_column='PriceFrom', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Florists'


class Gueststatuses(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Polish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GuestStatuses'


class Guesttables(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=50, db_collation='Polish_CI_AS')  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GuestTables'


class Guests(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=200, db_collation='Polish_CI_AS')  # Field name made lowercase.
    side = models.CharField(db_column='Side', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    statusid = models.ForeignKey(Gueststatuses, models.DO_NOTHING, db_column='StatusId', blank=True, null=True)  # Field name made lowercase.
    tableid = models.ForeignKey(Guesttables, models.DO_NOTHING, db_column='TableId', blank=True, null=True)  # Field name made lowercase.
    dietid = models.ForeignKey(Dietarypreferences, models.DO_NOTHING, db_column='DietId', blank=True, null=True)  # Field name made lowercase.
    plusone = models.BooleanField(db_column='PlusOne', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Guests'


class Homesections(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sectionkey = models.CharField(db_column='SectionKey', unique=True, max_length=50, db_collation='Polish_CI_AS')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    subtitle = models.CharField(db_column='Subtitle', max_length=500, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    buttontext = models.CharField(db_column='ButtonText', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HomeSections'


class Musiciantypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MusicianTypes'


class Musicians(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, db_collation='Polish_CI_AS')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricefrom = models.DecimalField(db_column='PriceFrom', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rating = models.DecimalField(db_column='Rating', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

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
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255, db_collation='Polish_CI_AS')  # Field name made lowercase.
    subscribedat = models.DateTimeField(db_column='SubscribedAt', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.

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
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhotographerStyles'


class Photographers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, db_collation='Polish_CI_AS')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricefrom = models.DecimalField(db_column='PriceFrom', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Photographers'


class Sociallinks(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    platformname = models.CharField(db_column='PlatformName', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=255, db_collation='Polish_CI_AS')  # Field name made lowercase.
    iconname = models.CharField(db_column='IconName', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SocialLinks'


class Staticpages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    pagekey = models.CharField(db_column='PageKey', unique=True, max_length=50, db_collation='Polish_CI_AS')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, db_collation='Polish_CI_AS')  # Field name made lowercase.
    content = models.TextField(db_column='Content', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaticPages'


class Taskpriorities(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Polish_CI_AS')  # Field name made lowercase.
    colorcode = models.CharField(db_column='ColorCode', max_length=20, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskPriorities'


class Tasks(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, db_collation='Polish_CI_AS')  # Field name made lowercase.
    categoryid = models.ForeignKey(Budgetcategories, models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    priorityid = models.ForeignKey(Taskpriorities, models.DO_NOTHING, db_column='PriorityId', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tasks'


class Timelineevents(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    groupid = models.ForeignKey('Timelinegroups', models.DO_NOTHING, db_column='GroupId', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, db_collation='Polish_CI_AS')  # Field name made lowercase.
    details = models.TextField(db_column='Details', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    iscompleted = models.BooleanField(db_column='IsCompleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimelineEvents'


class Timelinegroups(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')  # Field name made lowercase.
    orderindex = models.IntegerField(db_column='OrderIndex')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimelineGroups'


class Transporttypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransportTypes'


class Transportvehicles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    typeid = models.ForeignKey(Transporttypes, models.DO_NOTHING, db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, db_collation='Polish_CI_AS')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.
    pricefrom = models.DecimalField(db_column='PriceFrom', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransportVehicles'


class Userfavorites(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    serviceid = models.IntegerField(db_column='ServiceId')  # Field name made lowercase.
    servicetype = models.CharField(db_column='ServiceType', max_length=50, db_collation='Polish_CI_AS')  # Field name made lowercase.
    savedat = models.DateTimeField(db_column='SavedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserFavorites'


class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255, db_collation='Polish_CI_AS')  # Field name made lowercase.
    passwordhash = models.TextField(db_column='PasswordHash', db_collation='Polish_CI_AS')  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=20, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    weddingdate = models.DateField(db_column='WeddingDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.

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
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Polish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VenueFeatures'


class Venues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, db_collation='Polish_CI_AS')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, db_collation='Polish_CI_AS')  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity')  # Field name made lowercase.
    priceperperson = models.DecimalField(db_column='PricePerPerson', max_digits=10, decimal_places=2)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rating = models.DecimalField(db_column='Rating', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Venues'
