import hrmcalcs


def hrmprint(peakvalues, instantHR, tachy, brady):
    file = open("hrmoutput.txt", "w")
    for row in list(zip(peakvalues, instantHR, brady, tachy)):
        out = print(str(row))
        file.write("{}\n".format(row))
    file.close()


def main():
    peakvalues, instantHR, averageHR, tachy, brady = hrmcalcs.maincalcs()
    hrmprint(peakvalues, instantHR, tachy, brady)


if __name__ == "__main__":
    main()
