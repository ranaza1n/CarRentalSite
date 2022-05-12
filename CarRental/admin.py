from django.contrib import admin
from CarRental.models import Contact
from CarRental.models import Location_Pref_Report
from CarRental.models import Revenue_Report
from CarRental.models import Frequent_User_Report
# Register your models here.
admin.site.register(Contact)
admin.site.register(Location_Pref_Report)
admin.site.register(Revenue_Report)
admin.site.register(Frequent_User_Report)