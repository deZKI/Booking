from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import AuthComment, BookComment, Users

admin.site.unregister(Group)


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    """ Custom User Admin """
    pass


@admin.register(BookComment)
class BookCommentAdmin(admin.ModelAdmin):
    """ BookComment """
    pass


@admin.register(AuthComment)
class AuthCommentAdmin(admin.ModelAdmin):
    """ AuthComment """
    pass
