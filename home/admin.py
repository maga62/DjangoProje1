from django.contrib import admin

# Register your models here.
from home.models import Settings, ContactFormMessage


class ContactFromMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','note','status']
    list_filter = ['status']

admin.site.register(ContactFormMessage, ContactFromMessageAdmin)
admin.site.register(Settings)


# burda kaldiim



