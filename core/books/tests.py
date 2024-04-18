from django.test import TestCase

from services.permissions.books import BookPermissionsService

from books.factory import BooksFactory
from users.factory import UsersFactory


class BooksPermissionTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UsersFactory()

    def test_books_assign_permission(self):
        book = BooksFactory()
        BookPermissionsService.assign_permission(book, self.user, 'view')
        self.assertTrue(BookPermissionsService.has_permission(book, self.user, 'view'))
