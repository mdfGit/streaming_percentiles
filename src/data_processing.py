from __builtin__ import str

__author__ = 'maf058'

def isValidPreProcessing(inputFields):

    CMTE_ID = inputFields[0]
    NAME = inputFields[7]
    ZIP_CODE = inputFields[10]
    TRANSACTION_DT = inputFields[13]
    TRANSACTION_AMT = inputFields[14]
    OTHER_ID = inputFields[15]

    if isValidTxnAmt(TRANSACTION_AMT) is False:
        return False

    if isValidRecord(OTHER_ID) is False:
        return False



def isValidTxnAmt(txnAmt):
    if txnAmt <= 0:
        print "Transaction Amt invalid: " + str(txnAmt)
        return False
    else:
        return True



def isValidRecord(otherId):
    if otherId != "":
        print "OtherId disqualification: " + str(otherId)
        return False
    else:
        return True


def getPercentileInput():
    f = open('./input/percentile.txt', 'r')
    return f.readline()
