from readHR import EcgReader
from hrmcalcs2oo import hrmcalcs
from hrmtb import TachyBrady


class HrmOutput:

    def __init__(self, file='Test_ECG.csv', average_window=20,
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
        self.average_window = average_window
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
            self.time = read_ecg.time
            timebeat = np.diff(read_ecg.peak_vector)
            calc_ecg = hrmcalcs(self.time, timebeat, read_ecg.peak_vector,
                                self.average_window)
            calc_ecg.hrm_instant()
            self.instant_hr = calc_ecg.instant_hr
            calc_ecg.hrm_average()
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
            f.write("Time of Heartbeat (s), Instant HR, Average HR, Bradycardia (true/false), "
                    "Tachycardia (true/false)\n")
            for row in list(zip(self.peak_vector, self.instant_hr, self.average_hr,
                                self.brady, self.tachy)):
                f.write("{},{},{},{}\n".format(np.round(row[0], 2),
                                               np.round(row[1], 2),
                                               np.round(row[2], 2),
                                               np.round(row[3], 2)),
                                               np.round(row[4], 2))
    