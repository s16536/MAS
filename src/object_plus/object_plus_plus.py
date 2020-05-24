from typing import Dict

from object_plus.object_plus import ObjectPlus
from object_plus.roles import Role, RoleConstraint
from utils import print_dict


class ObjectPlusPlus(ObjectPlus):
    """
    Class to manage connections between Objects
    """

    _all_parts = list()

    def __init__(self):
        self._links = dict()
        super().__init__()

    def add_link(self, role: Role, target_object, qualifier=None,
                 reverse_qualifier=None, add_reverse_role: bool=True):
        """
        Creates a new link (with reverse link) to the given target object (optionally as qualified connection).

        :param role: Role
        :param target_object: ObjectPlusPlus
        :param qualifier: Optional. if specified, qualified connection will be created
        :param reverse_qualifier: Optional. if specified, qualified reverse connection will be created
        :exception DuplicateQualifierError: if the role with given qualifier already exists in the class
        :exception RoleNotDefinedError: if role is not defined in the class
        :exception RoleLimitReachedError : if the upper limit of linked object for the role has been reached
        """

        if qualifier is None:
            qualifier = target_object

        if reverse_qualifier is None:
            reverse_qualifier = self

        role_constraints = self.get_role_constraints().get(role)
        if role_constraints is None:
            raise RoleNotDefinedError(role, self.__class__.__name__)
        self.check_limits(role, role_constraints)

        object_links = self._links.get(role, dict())
        self._links[role] = object_links

        if object_links.get(qualifier) is not None:
            raise DuplicateQualifierError(role, self.__class__.__name__, qualifier)

        object_links[qualifier] = target_object

        if add_reverse_role:
            reverse_role = role_constraints.reverse_role_name
            target_object.add_link(reverse_role, self, reverse_qualifier, None, False)

    def add_part(self, role: Role, reverse_role: Role, part_object):
        """
        Adds an information about a connection

        :param role: Role
        :param reverse_role: Role
        :param part_object: ObjectPlusPlus
        :exception CompositionError: if the part_object is already connected to other object
        """

        if part_object in self._all_parts:
            raise CompositionError(part_object)

        self.add_link(role, part_object)
        self._all_parts.append(part_object)

    def get_links(self, role: Role):
        """
        Gets a tuple of connected objects for the given role name.

        :param role: Role
        :exception RoleNotDefinedError: if role is not defined in the class
        """
        if self.get_role_constraints().get(role) is None:
            raise RoleNotDefinedError(role, self.__class__.__name__)

        links = self._links.get(role)
        if links is None:
            return ()

        return tuple(links)

    def print_links(self, role: Role = None):
        """
        Prints links for the given role.
        :param role: Role [optional] (if empty, method prints links for all existing roles)
        :exception RoleNotDefinedError: if no links exist for the given role
        """

        if role is None:
            print(f"{self} all links :")
            print_dict(self._links)
            return

        object_links = self._links.get(role)
        if object_links is None:
            raise RoleNotDefinedError(role, self.__class__.__name__)

        print(f"{self} links, role ' {role} ':")
        for obj in object_links.values():
            print(obj)

    def get_linked_object(self, role: Role, qualifier):
        """
        Gets an object for the given qualifier (a qualified association).
        :param role: Role
        :param qualifier: Object
        :return:
        """

        role_links = self._links.get(role)

        if role_links is None:
            raise RoleNotDefinedError(role, self.__class__.__name__)

        result = role_links.get(qualifier)
        if result is None:
            raise InvalidQualifierError(role, self.__class__.__name__, qualifier)

        return result

    def check_limits(self, role: Role, role_constraints: RoleConstraint):
        limit = role_constraints.limit
        existing_links = len(self.get_links(role))

        if existing_links == limit:
            raise RoleLimitReachedError(role, self.__class__.__name__, limit)

    def remove_link(self, role: Role, target_object):
        """
        Removes the existing link for the given object.

        :param role: Role
        :param target_object: ObjectPlusPlus
        """
        links = self._links.get(role)
        if links is None:
            return

        links.pop(target_object, None)

    @classmethod
    def get_role_constraints(cls) -> Dict[Role, RoleConstraint]:
        return dict()

    @classmethod
    def get_constraints_for_role(cls, role: Role) -> RoleConstraint:
        return cls.get_role_constraints().get(role)


class RoleNotDefinedError(Exception):
    def __init__(self, role, class_name):
        super().__init__(f"Role {role} not defined in the class {class_name}")


class RoleLimitReachedError(Exception):
    def __init__(self, role_name, class_name, limit):
        super().__init__(f"Limit {limit} links reached for the role '{role_name}' in the class {class_name}")


class DuplicateQualifierError(Exception):
    def __init__(self, role_name, class_name, qualifier):
        super().__init__(
            f"Link for the role '{role_name}' with qualifier = '{qualifier}' already exists in the class {class_name}")


class InvalidQualifierError(Exception):
    def __init__(self, role_name, class_name, qualifier):
        super().__init__(
            f"Link for the role '{role_name}' with qualifier = '{qualifier}' does not exist in the class {class_name}")


class CompositionError(Exception):
    def __init__(self, composite):
        super().__init__(
            f"Cannot create the link - composite: '{composite}' already has its owner")
