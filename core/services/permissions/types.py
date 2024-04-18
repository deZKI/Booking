from typing import Literal, TypeVar

from django.db.models import Model

PermissionType = Literal['view', 'edit', 'delete']
DjModel = TypeVar('DjModel', bound=Model)
