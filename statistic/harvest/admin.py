from django.contrib import admin
from .models import HwInfo, NetworkConfig, AudioDevice

admin.site.register(HwInfo)
admin.site.register(NetworkConfig)
admin.site.register(AudioDevice)
