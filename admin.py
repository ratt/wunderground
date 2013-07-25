from django.contrib import admin
from wunderground.models import Feed

class FeedAdmin(admin.ModelAdmin):
    list_display    = ('location', 'country_code', 'default')

admin.site.register(Feed, FeedAdmin)