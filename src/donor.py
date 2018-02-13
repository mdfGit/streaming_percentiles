__author__ = 'maf058'

class Donor:
    def __init__(self):
        self.name_zip_dict = {}
        self.year_recipient_dict = {}

    def isRepeat(self, name_zip):
        if name_zip not in self.name_zip_dict:
            self.name_zip_dict[name_zip]="value"
            return False
        else:
            return True

