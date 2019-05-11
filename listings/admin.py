from django.contrib import admin
from .models import Listing



class ListingAdmin(admin.ModelAdmin):

    list_display = ('id','title','is_published','price','list_date','realtor')   # which fields should display
    list_display_links =('id','title')                                           # which fields should clickable
    list_filter = ('realtor',)                                                   # which fields can be used as filter
    list_editable = ('is_published',)                                            # which fields can be changed in displaying
    search_fields = ('title','discription','address', 'city','state', 'zipcode','price')

    list_per_page = 25    # for admin area




admin.site.register(Listing,ListingAdmin)
