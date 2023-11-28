from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Post)

admin.site.register(Category)
admin.site.register(Schedule)
admin.site.register(PublishedPost)
admin.site.register(AlmazadiProducts)
admin.site.register(Share)
admin.site.register(Comment)
admin.site.register(Quotes)
