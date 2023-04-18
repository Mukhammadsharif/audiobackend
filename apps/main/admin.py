from django.contrib import admin

# Register your models here.
from main.models import Author, Composition, Liked, Deferred, Catalog

admin.site.register(Author)
admin.site.register(Composition)
admin.site.register(Liked)
admin.site.register(Deferred)
admin.site.register(Catalog)
