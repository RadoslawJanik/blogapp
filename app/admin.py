from django.contrib import admin

# Register your models here.
from app.models import Post, Tag, Comments,Profile,WebsiteMeta

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Profile)
admin.site.register(WebsiteMeta)