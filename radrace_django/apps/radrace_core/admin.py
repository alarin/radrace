from django.contrib import admin
from django.contrib.auth.models import User,Group

from radrace_core.models import *


class FieldInline(admin.TabularInline):
	model=EventField
	extra=5
	
class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
	inlines=[FieldInline]

class ProfileInline(admin.StackedInline):
	model=Profile
	
class UserAdmin(admin.ModelAdmin):
	inlines=[ProfileInline]
	extra=0
	
admin.site.unregister([User, Group])

admin.site.register(User, UserAdmin)
admin.site.register(Place)
admin.site.register(Event, EventAdmin)