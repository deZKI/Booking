from django.db import models

from authors.models import Authors


class Tags(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    thumbnail = models.ImageField(upload_to='images/books/thumbnail/', null=False, blank=False)
    file = models.FileField(upload_to='books/', null=True, blank=True)
    authors = models.ManyToManyField(to=Authors, related_name='books')
    tags = models.ManyToManyField(to=Tags, related_name='books')
    release_date = models.DateField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, default=0, decimal_places=2)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        permissions = (
            ('view', 'User can view file of book'),
        )

    def __str__(self):
        return f"{self.title} {self.release_date}"
