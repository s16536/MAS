from object_plus.object_plus import ObjectPlus
from utils import print_dict


class ObjectPlusPlus(ObjectPlus):
    """
    Class to manage connections between Objects
    """

    _all_parts = list()

    def __init__(self):
        self._links = dict()
        super().__init__()

    def add_link(self, role_name: str, reverse_role_name: str, target_object, qualifier=None,
                 reverse_qualifier=None, counter: int = 2):
        """
        Creates a new link to the given target object (optionally as qualified connection).

        :param role_name: str
        :param reverse_role_name: str
        :param target_object: ObjectPlusPlus
        :param qualifier: Optional. If specified, qualified connection will be created
        :param reverse_qualifier: Optional. If specified, qualified reverse connection will be created
        :exception DuplicateQualifierError: if the role with given qualifier already exists in the class
        :exception RoleNotDefinedError: if role is not defined in the class
        :exception RoleLimitReachedError : if the upper limit of linked object for the role has been reached
        """

        if counter < 1:
            return

        if qualifier is None:
            qualifier = target_object

        if reverse_qualifier is None:
            reverse_qualifier = self

        if counter == 2:
            self.check_limits(role_name)
            target_object.check_limits(reverse_role_name)

        object_links = self._links.get(role_name, dict())
        self._links[role_name] = object_links

        if object_links.get(qualifier) is not None:
            raise DuplicateQualifierError(role_name, self.__class__.__name__, qualifier)

        object_links[qualifier] = target_object
        target_object.add_link(reverse_role_name, role_name, self, reverse_qualifier, None, counter - 1)

    def add_part(self, role_name: str, reverse_role_name: str, part_object):
        """
        Adds an information about a connection (using a "semi" composition)

        :param role_name: str
        :param reverse_role_name: str
        :param part_object: ObjectPlusPlus
        :exception ValueError: if the part_object is already connected to other object
        """

        if part_object in self._all_parts:
            raise ValueError("The part is already connected to a whole!")

        self.add_link(role_name, reverse_role_name, part_object)
        self._all_parts.append(part_object)

    def get_links(self, role_name: str):
        """
        Gets a tuple of connected objects for the given role name.

        :param role_name: str
        :exception RoleNotDefinedError: if role is not defined in the class
        """
        if self.get_role_constraints().get(role_name) is None:
            raise RoleNotDefinedError(role_name, self.__class__.__name__)

        links = self._links.get(role_name)
        if links is None:
            return ()

        return tuple(links)

    def print_links(self, role_name: str = None):
        """
        Prints links for the given role.
        :param role_name: str [optional] (if empty, method prints links for all existing roles)
        :exception RoleNotDefinedError: if no links exist for the given role
        """

        if role_name is None:
            print(f"{self} all links :")
            print_dict(self._links)
            return

        object_links = self._links.get(role_name)
        if object_links is None:
            raise RoleNotDefinedError(role_name, self.__class__.__name__)

        print(f"{self} links, role ' {role_name} ':")
        for obj in object_links.values():
            print(obj)

    def check_limits(self, role_name):
        role_constraints = self.get_role_constraints()

        limit = role_constraints.get(role_name)

        if limit is None:
            raise RoleNotDefinedError(role_name, self.__class__.__name__)

        limit = role_constraints[role_name]
        existing_links = len(self.get_links(role_name))

        if existing_links == limit:
            raise RoleLimitReachedError(role_name, self.__class__.__name__, limit)

    @classmethod
    def get_role_constraints(cls):
        return dict()


class RoleNotDefinedError(Exception):
    def __init__(self, role_name, class_name):
        super().__init__(f"Role {role_name} not defined in the class {class_name}")


class RoleLimitReachedError(Exception):
    def __init__(self, role_name, class_name, limit):
        super().__init__(f"Limit {limit} links reached for the role {role_name} in the class {class_name}")


class DuplicateQualifierError(Exception):
    def __init__(self, role_name, class_name, qualifier):
        super().__init__(
            f"Link for the role {role_name} with qualifier = {qualifier} already exists in the class {class_name}")
