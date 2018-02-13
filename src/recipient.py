from decimal import Decimal
from locale import str
from binary_search_tree import *
import numpy as np

__author__ = 'maf058'

class Calculations:
    def __init__(self):
        self.total_received_from_repeat = Decimal(0.00)
        self.total_number_from_repeat = 0
        self.contributions_root_node = None

class Recipient:
    def __init__(self):
        self.year_recipient_zip_dict = {}

    def calculateRunningPercentile(self, recipient, zip, year, contribution, percentile):
        total_repeat_contributions_count = 0
        total_repeat_contributions = 0
        current_calculations = None
        year_recipient_zip = year + recipient + zip

        if year_recipient_zip not in self.year_recipient_zip_dict:

            # new
            current_calculations = Calculations()

            # initialize top node of binary tree if it is not set
            if current_calculations.contributions_root_node is None:
                current_calculations.contributions_root_node = Node(contribution)

        else:

            # existing
            current_calculations = self.year_recipient_zip_dict[year_recipient_zip]

            # add a contribution to the tree
            binary_insert(current_calculations.contributions_root_node, Node(contribution))

        # update totals as records are added
        current_calculations.total_number_from_repeat += 1
        current_calculations.total_received_from_repeat += Decimal(contribution)

        # update the reference to calculations for this recipient year/zip
        self.year_recipient_zip_dict[year_recipient_zip]=current_calculations
        total_repeat_contributions_count = current_calculations.total_number_from_repeat
        total_repeat_contributions = current_calculations.total_received_from_repeat

        index = np.ceil((float(percentile) / float(100)) * float(total_repeat_contributions_count))

        index_value = get_value_at_index(current_calculations.contributions_root_node, index)

        returnList = [recipient, zip, year, str(index_value),str(total_repeat_contributions),str(total_repeat_contributions_count)]

        returnDelimited = "|".join(returnList)

        return returnDelimited