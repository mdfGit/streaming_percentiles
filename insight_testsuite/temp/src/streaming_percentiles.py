__author__ = 'maf058'

fh = open("./output/repeat_donors.txt", "w")
lines_of_text = ["C00384516|02895|2018|333|333|1", "C00384516|02895|2018|333|717|2"]
fh.write('\n'.join(lines_of_text))
#fh.writelines(lines_of_text)
fh.close()