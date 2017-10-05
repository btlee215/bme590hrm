import hrmcalcs
import numpy as np


def hrmprint(file, peakvalues, instant_hr, average_hr, tachy, brady):
    """
       This function is used to write the output from our cardiac heart rate
       monitor to a text file. The function inputs have been returned from the
       hrmcalcs.py file and a new text file with the output from the cardiac
       monitor titled "hrmoutput.txt" has been created.

       :param peakvalues: array containing time points at which voltage
       condition was met to detect a heart beat. All values are in terms of
       time (s)
       :param instantHR: array of instantaneous heart rate values
       :param tachy: an array containing a '1' at time points where
       tachycardia was detected
       :param brady: an array containing a '1' at time points where
       bradycardia was detected
       :return: This function returns a text output file with the desired
       values from the cardiac monitor. The output has been rounded to decimal
       points for formatting + aesthetic purposes.

       """
    save_name = file.replace(".csv","_HRoutput.txt")
    with open(save_name, "w") as f:
        f.write("Average HR in Interval: {} \n".format(np.round(average_hr, 2)))
        f.write("Time of Heartbeat (s), Instant HR, Bradycardia (0/1), "
                "Tachycardia (0/1)\n")
        for row in list(zip(peakvalues, instant_hr, brady, tachy)):
            f.write("{},{},{},{}\n".format(np.round(row[0], 2),
                                           np.round(row[1], 2),
                                           np.round(row[2], 2),
                                           np.round(row[3], 2)))
        f.close()


def main(file='Test_ECG.csv'):
    """
    This function is run when the hrmoutput.py file is run in the command
    window. This function uses all the outputs from the hrmcalcs function
    and runs the hrmprint() function described above
    :return: This function returns an output text file with the desired values
    from the cardiac monitor.

    """

    peakvalues, instant_hr, average_hr, tachy, brady = hrmcalcs.maincalcs(file)
    hrmprint(file, peakvalues, instant_hr, average_hr, tachy, brady)


if __name__ == "__main__":
    main()
