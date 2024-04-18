from abc import ABC, abstractmethod

from users.models import Users

from .types import DjModel, PermissionType


class AbstractPermissionsService(ABC):

    @staticmethod
    @abstractmethod
    def has_permission(obj: DjModel, user: Users, perm: PermissionType):
        pass

    @staticmethod
    @abstractmethod
    def assign_permission(obj: DjModel, user: Users, perm: PermissionType):
        pass

    @staticmethod
    @abstractmethod
    def remove_permission(obj: DjModel, user: Users, perm: PermissionType):
        pass
