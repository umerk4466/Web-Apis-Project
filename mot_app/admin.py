from django.contrib import admin


# Register your models here.
from mot_app.models import User
from mot_app.models import Vehicle
from mot_app.models import Reminder


# Register your models to admin site
admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(Reminder)
