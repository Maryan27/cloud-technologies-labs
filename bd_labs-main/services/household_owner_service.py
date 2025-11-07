from dao.household_owner_dao import HouseholdOwnerDAO

class HouseholdOwnerService:
    def __init__(self, mysql):
        self.dao = HouseholdOwnerDAO(mysql)

    def get_household_owners(self):
        return self.dao.get_all_household_owners()

    def get_household_owners_by_owner(self, owner_id):
        return self.dao.get_household_owners_by_owner(owner_id)

    def add_household_owner(self, household_owner):
        return self.dao.insert_household_owner(household_owner)

    def modify_household_owner(self, household_owner_id, household_owner):
        return self.dao.update_household_owner(household_owner_id, household_owner)

    def remove_household_owner(self, household_owner_id):
        return self.dao.delete_household_owner(household_owner_id)


