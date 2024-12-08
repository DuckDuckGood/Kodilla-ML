from _5_3_base_contact import BaseContact
from _5_3_business_contact import BusinessContact

def create_contacts(*, base_contacts=0, business_contacts=0):
    base_contacts_list = [BaseContact() for _ in range(base_contacts)]
    business_contacts_list = [BusinessContact() for _ in range(business_contacts)]
    return base_contacts_list + business_contacts_list