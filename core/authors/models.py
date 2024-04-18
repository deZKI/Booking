from django.db import models


class Authors(models.Model):
    """ Model for authors """
    name = models.CharField(max_length=124, blank=True, null=True)
    surname = models.CharField(max_length=124, blank=True, null=True)
    last_name = models.CharField(max_length=124, blank=True, null=True)
    birth_date = models.DateField(blank=False, null=False)
    biography = models.TextField(blank=False, null=False)

    def get_author_tags(self) -> list[str]:
        return self.books.prefetch_related('tags').order_by('tags__name').values_list(
            'tags__name')

    class Meta:
        unique_together = ('name', 'surname', 'last_name', 'birth_date')
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f'{self.name} {self.surname} {self.last_name}'
