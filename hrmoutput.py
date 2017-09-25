import hrmcalcs


def hrmprint(peakvalues, instantHR, tachy, brady):
    """
    This function is used to write the output from our cardiac heart rate monitor to a text file. The function inputs
    have been returned from the hrmcalcs.py file and a new text file with the output from the cardiac monitor titled
    "hrmoutput.txt" has been created.

    :param peakvalues: array containing time points at which voltage condition was met to detect a heart beat. All vals
    are in terms of time (s)
    :param instantHR: array of instantaneous heart rate values
    :param tachy: an array containing a '1' at time points where tachycardia was detected
    :param brady: an array containing a '1' at time points where bradycardia was detected
    :return: This function returns a text output file with the desired values from the cardiac monitor. The output has
    been rounded to decimal points for formatting + aesthetic purposes.

    """

    file = open("hrmoutput.txt", "w")
    file.write("'Time (s)','Instant HR','Bradycardia','Tachycardia'\n")
    for row in list(zip(peakvalues, instantHR, brady, tachy)):
        out = print(str(row))
        file.write("{}\n".format(row))
    file.close()

def main():
    """
    This function is run when the hrmoutput.py file is run in the command window. This function uses all the outputs
    from the hrmcalcs function and runs the hrmprint() function described above
    :return: This function returns an output text file with the desired values from the cardiac monitor.

    """

    peakvalues, instantHR, averageHR, tachy, brady = hrmcalcs.maincalcs()
    hrmprint(peakvalues, instantHR, tachy, brady)
    print (peakvalues)
    print (instantHR)

if __name__ == "__main__":
    main()


