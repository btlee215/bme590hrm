import hrmread
import hrmcalcs

def hrmprint(peakvalues, instantHR, brady,tachy):
    # Headers = ['Time (s)','Instant HR','Bradycardia','Tachycardia']
    for row in list(zip(peakvalues, instantHR, brady, tachy)):
        out = print(str(row))
        file = open("hrmoutput.txt", "w")
        for row in out:
            file.write("{}\n".format(row))
            file.close()
    return file

if __name__ == "main":
    peakvalues, instantHR, tachy, brady = hrmcalcs.maincalcs()
    hrmprint(peakvalues, instantHR,brady,tachy)