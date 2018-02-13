import sys
from __builtin__ import str
from __builtin__ import int
from binary_search_tree import *
from publisher import Publisher
from data_processing import *
from donor import *
from recipient import *

__author__ = 'maf058'


donor = Donor()
recipient = Recipient()
publisher = Publisher("./output/repeat_donors.txt")
percentile_value = getPercentileInput()


with open('./input/itcont.txt', 'r') as input_file:

    for line in input_file:
        try:

            fields = line.split('|')

            if isValidPreProcessing(fields) is False:
                continue

            CMTE_ID = fields[0]
            NAME = fields[7]
            ZIP_CODE = fields[10]
            TRANSACTION_DT = fields[13]
            TRANSACTION_AMT = fields[14]
            OTHER_ID = fields[15]

            if donor.isRepeat(str(NAME) + str(ZIP_CODE[:5])):
                results = recipient.calculateRunningPercentile(str(CMTE_ID), str(ZIP_CODE[:5]), str(TRANSACTION_DT[4:]), TRANSACTION_AMT, percentile_value)
                publisher.publish(results)

        except BaseException as e:

            print str(e)
            continue

        else:
            continue


input_file.closed
