from django.contrib import admin
from .models import TwoDaysAdStat, TwoDaysBgStat, AdStat, BgStat, HashTable

admin.site.register(TwoDaysBgStat)
admin.site.register(TwoDaysAdStat)
admin.site.register(BgStat)
admin.site.register(AdStat)
admin.site.register(HashTable)
