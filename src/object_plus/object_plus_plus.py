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
                 counter: int = 2):
        """
        Creates a new link to the given target object (optionally as qualified connection).

        :param role_name: str
        :param reverse_role_name: str
        :param target_object: ObjectPlusPlus
        :param qualifier: Optional. If specified, qualified connection will be created
        :exception ValueError: if the specified role is not expected for the object
        or the upper limit of linked object has been reached
        """

        if counter < 1:
            return

        if qualifier is None:
            qualifier = target_object

        if counter == 2:
            self.check_limits(role_name)
            target_object.check_limits(reverse_role_name)

        object_links = self._links.get(role_name, dict())
        self._links[role_name] = object_links

        if object_links.get(qualifier) is None:
            object_links[qualifier] = target_object
            target_object.add_link(reverse_role_name, role_name, self, self, counter - 1)

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
        :exception ValueError: if role is not defined in the class
        """
        if self.get_role_constraints().get(role_name) is None:
            raise ValueError("No links for the role: " + role_name)

        links = self._links.get(role_name)
        if links is None:
            return ()

        return tuple(links)

    def print_links(self, role_name: str = None):
        """
        Prints links for the given role.
        :param role_name: str [optional] (if empty, method prints links for all existing roles)
        :exception ValueError: if no links exist for the given role
        """

        if role_name is None:
            print_dict(self._links)
            return

        object_links = self._links.get(role_name)
        if object_links is None:
            raise ValueError("No links for the role: " + role_name)

        print(self.__class__.__name__ + " links, role '" + role_name + "':")
        for obj in object_links.values():
            print(obj)

    def check_limits(self, role_name):
        role_constraints = self.get_role_constraints()

        limit = role_constraints.get(role_name)

        if limit is None:
            raise ValueError(f"Role {role_name} not defined in the class {self.__class__.__name__}")

        limit = role_constraints[role_name]
        existing_links = len(self.get_links(role_name))

        if existing_links == limit:
            raise ValueError(f"Limit {limit} links reached for the role {role_name} in the class {self.__class__.__name__}")

    @classmethod
    def get_role_constraints(cls):
        return dict()

# 	/**
# 	 * Gets an object for the given qualifier (a qualified association).
# 	 * @param roleName
# 	 * @param qualifier
# 	 * @return
# 	 * @throws Exception
# 	 */
# 	public ObjectPlusPlus getLinkedObject(String roleName, Object qualifier) throws Exception {
# 		Map<Object, ObjectPlusPlus> objectLinks;
#
# 		if(!links.containsKey(roleName)) {
# 			// No links
# 			throw new Exception("No links for the role: " + roleName);
# 		}
#
# 		objectLinks = links.get(roleName);
# 		if(!objectLinks.containsKey(qualifier)) {
# 			// No link for the qualifer
# 			throw new Exception("No link for the qualifer: " + qualifier);
# 		}
#
# 		return objectLinks.get(qualifier);
# 	}
#
# 	/**
# 	 * Checks if there are any links for the given role name.
# 	 * @param nazwaRoli
# 	 * @return
# 	 */
# 	public boolean anyLink(String nazwaRoli) {
# 		if(!links.containsKey(nazwaRoli)) {
# 			return false;
# 		}
#
# 		Map<Object, ObjectPlusPlus> links = this.links.get(nazwaRoli);
# 		return links.size() > 0;
# 	}
#
# 	/**
# 	 * Checks if there is a link to a given object as a given role.
# 	 * @param roleName
# 	 * @param targetObject
# 	 * @return
# 	 */
# 	public boolean isLink(String roleName, ObjectPlusPlus targetObject) {
# 		Map<Object, ObjectPlusPlus> objectLink;
#
# 		if(!links.containsKey(roleName)) {
# 			// No links for the role
# 			return false;
# 		}
#
# 		objectLink = links.get(roleName);
#
# 		return objectLink.containsValue(targetObject);
# 	}
# }
