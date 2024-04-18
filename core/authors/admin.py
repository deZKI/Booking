from django.contrib import admin

from authors.models import Authors


@admin.register(Authors)
class AuthorAdmin(admin.ModelAdmin):
    pass
