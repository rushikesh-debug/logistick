from django.contrib import admin
from .models import Parcel



class ParcelAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'sender_name', 'receiver_name', 'status')
    list_editable = ('status',)

admin.site.register(Parcel, ParcelAdmin)