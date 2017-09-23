import hrmcalcs

def hrmprint(peakvalues, instantHR, brady,tachy):
    # Headers = ['Time (s)','Instant HR','Bradycardia','Tachycardia']
    file = open("hrmoutput.txt", "w")
    file.write('This is a test line')
    for row in list(zip(peakvalues, instantHR, brady, tachy)):
        out = print(str(row))
        for row in out:
            file.write("{}\n".format(row))
    file.close()

if __name__ == "main":
    peakvalues, instantHR, tachy, brady = hrmcalcs.maincalcs()
    hrmprint(peakvalues, instantHR,brady,tachy)
