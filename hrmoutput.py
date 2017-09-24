import hrmcalcs
import numpy as np

def hrmprint(peakvalues, instantHR, tachy, brady):
    file = open("hrmoutput.txt", "w")
    for row in list(zip(peakvalues, instantHR, brady, tachy)):
        out = print(str(row))
        file.write("{},{},{},{}\n".format(np.round(row[0],2),np.round(row[1],2),np.round(row[2],2),np.round(row[3],2)))
    file.close()


def main():
    peakvalues, instantHR, averageHR, tachy, brady = hrmcalcs.maincalcs()
    hrmprint(peakvalues, instantHR, tachy, brady)


if __name__ == "__main__":
    main()

