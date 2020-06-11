from models.user import EscapeRoomOwnerPerson, Address, Person


def create_person_owner() -> EscapeRoomOwnerPerson:
    address = Address("city", "postcode", "street", 1)
    person = Person(first_name="first", last_name="last")
    return EscapeRoomOwnerPerson(username="us", password="ps", address=address, er_owner_person=person)


def assert_owner_details(test, owner):
    test.assertEqual(owner.username, "us")
    test.assertEqual(owner.password, "ps")
    test.assertEqual(owner.address_street, "street")
    test.assertEqual(owner.address_postcode, "postcode")
    test.assertEqual(owner.address_city, "city")
    test.assertEqual(owner.address_house_no, 1)
    test.assertIsNone(owner.address_apartment_no)
    test.assertEqual(owner.er_owner_person.first_name, "first")
    test.assertEqual(owner.er_owner_person.last_name, "last")