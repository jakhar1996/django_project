from django.contrib import admin

# Register your models here.
from .models import posts

class PostsModeAdmin(admin.ModelAdmin):
	list_display_link = ["update"]
	list_display = ["title","update", "timestamp"]
	list_filter = ["update", "timestamp"]
	search_fields = ["title", "content"]
	class Meta:
		model = posts

admin.site.register(posts, PostsModeAdmin)