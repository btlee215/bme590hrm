from readHR import EcgReader
from hrmcalcs2oo import hrmcalcs
from hrmtb import TachyBrady


class HrmOutput:

    def __init__(self, file='Test_ECG.csv', start_min=3, end_min=5,
                 brady_limit=60, tachy_limit=100):
        """

        :param file: String representing ECG file used to make heart rate
        calculations

        :param start_min: User-inputted value for the "starting minute" of
        average heart rate calculations, in minutes.

        :param end_min: User-inputted value for the "ending minute" of average
        heart rate calculations, in minutes.

        :param brady_limit: The threshold value for bradycardia, with the
        default set at 60 bpm

        :param tachy_limit: The threshold value for tachycardia, with the
        default set at 100 bpm
        """
        self.file = file
        self.start_min = start_min
        self.end_min = end_min
        self.brady_limit = brady_limit
        self.tachy_limit = tachy_limit
        self.valid_file = False
        self.peak_vector = []
        self.instant_hr = []
        self.average_hr = None
        self.tachy = []
        self.brady = []
        self.extract_vals()
        if self.valid_file:
            self.print_hrm_output()

    def extract_vals(self):
        """
        This method extracts the main vectors to be used towards calculations,
        using the imported classes

        :return: This method returns many main vectors, which are the
        following. Timebeat, the time between heart beats, the instantaneous
        heart rate, the average heart rate, along with the tachy and brady
        vectors, which marks the occurrences of tachycardia and bradycardia
        respectively through vectors of 0s and 1s (1 marking an event
        detection).
        """
        read_ecg = EcgReader(self.file)
        if read_ecg.csv_check and read_ecg.data_check:
            self.valid_file = True
            self.peak_vector = read_ecg.peak_vector
            timebeat = np.diff(read_ecg.peak_vector)
            calc_ecg = hrmcalcs(timebeat, read_ecg.peak_vector,
                                self.start_min, self.end_min)
            calc_ecg.hrminstant()
            self.instant_hr = calc_ecg.instant_hr
            calc_ecg.hrmaverage()
            self.average_hr = calc_ecg.average_hr
            tb_ecg = TachyBrady(self.instant_hr, self.brady_limit,
                                self.tachy_limit)
            tb_ecg.tb()
            self.tachy = tb_ecg.tachy
            self.brady = tb_ecg.brady

    def print_hrm_output(self):
        """
        :return: This method returns a printed output file of the heartbeat
        occurrence time, the instantaneous heart rate, and the occurrence
        of tachycardia or bradycardia.
        """
        save_name = self.file.replace(".csv", "_HRoutput.txt")
        with open(save_name, "w") as f:
            f.write("Average HR in Interval: {} \n".
                    format(np.round(self.average_hr)))
            f.write("Time of Heartbeat (s), Instant HR, Bradycardia (0/1), "
                    "Tachycardia (0/1)\n")
            for row in list(zip(self.peak_vector, self.instant_hr,
                                self.brady, self.tachy)):
                f.write("{},{},{},{}\n".format(np.round(row[0], 2),
                                               np.round(row[1], 2),
                                               np.round(row[2], 2),
                                               np.round(row[3], 2)))


