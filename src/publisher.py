import sys

__author__ = 'maf058'

class Publisher:
    def __init__(self, destination):
        self.destination = destination
        self.filehandler = open(self.destination, "w")

    def __del__(self):
        print 'filehandler destructor'
        self.filehandler.close()

    def publish(self, string_to_publish):
        self.filehandler.write(string_to_publish + '\n')


