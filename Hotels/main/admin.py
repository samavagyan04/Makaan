from django.contrib import admin
from .models import *



@admin.register(MainInfo)
class MainInfoModelAdmin(admin.ModelAdmin):
    list_display = ['name','address']
    list_display_links = ['name','address']
    search_fields = ['name','address']
admin.site.register(HomeStatus)
admin.site.register(ImageCycle)
admin.site.register(PropertyTypes)
admin.site.register(PropertyTypesJarang)
admin.site.register(MoreInformation)
admin.site.register(PropertyListing)
admin.site.register(ContactAgent)
admin.site.register(PropertyAgent)
admin.site.register(Client)
admin.site.register(Gallery)

#-----------------------------------
admin.site.register(AboutStatus)
