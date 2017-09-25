import hrmcalcs
import numpy as np

def hrmprint(peakvalues, instantHR, averageHR, tachy, brady):
    file = open("hrmoutput.txt", "w")
    file.write("Average HR in Interval: {} \n".format(np.round(averageHR,2)))
    file.write("Time of Heartbeat (s), Instant HR, Bradycardia (0/1), Tachycardia (0/1)\n")
    for row in list(zip(peakvalues, instantHR, brady, tachy)):
        file.write("{},{},{},{}\n".format(np.round(row[0],2),np.round(row[1],2),np.round(row[2],2),np.round(row[3],2)))
    file.close()


def main():
    peakvalues, instantHR, averageHR, tachy, brady = hrmcalcs.maincalcs()
    hrmprint(peakvalues, instantHR, averageHR, tachy, brady)


if __name__ == "__main__":
    main()

