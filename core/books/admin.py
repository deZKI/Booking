from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from books.models import Books, Tags


@admin.register(Books)
class BooksAdmin(GuardedModelAdmin):
    pass


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
