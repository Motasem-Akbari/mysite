from django.contrib import admin
from blog.models import Post

# Register your models here.

# @admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    fields = ("title",)
    list_display = ("title", "counted_like", "status",
                    "published_date", "created_date")
    list_filter = ("status",)
    # ordering = ["-created_date"]
    search_fields = ["content", "title"]

admin.site.register(Post, PostAdmin)
