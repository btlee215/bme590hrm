import hrmcalcs

def hrmprint(peakvalues, instantHR, brady,tachy):
    # Headers = ['Time (s)','Instant HR','Bradycardia','Tachycardia']
    with open("hrmoutput.txt", "w") as file:
        file.write('This is a test line')
        for row in list(zip(peakvalues, instantHR, brady, tachy)):
            out = print(str(row))
            for row in out:
                file.write("{}\n".format(row))
        file.close()


if __name__ == "__main__":
    peakvalues, instantHR, tachy, brady = hrmcalcs.maincalcs()
    print(hrmprint(peakvalues, instantHR,brady,tachy))
    file = open("hrmoutput.txt", "r")
    print(file.read())
