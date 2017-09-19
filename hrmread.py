# this file should read in the csv file, sort into time and voltage
# should also output vector of times of each heartbeat
import csv
def main(file):
    read_ecg(file)
    find_range(time,voltage)

time = []
voltage = []
peak_times = []
toggle_peak_status = 0
count_peaks = 0

def read_ecg(file):
    with open (file) as ecg_Data_File
        ecg_Reader = csv.reader(ecg_Data_File)
        for row in ecg_Reader:
            time.append(row[0])
            voltage.append(row[1])

def find_range(time,voltage):
    import statistics
    baseline = statistics.median(voltage)
    pos_range = max(voltage)-baseline
    for i in voltage:
        if toggle_peak_status == 0:
            if (voltage[i] > (baseline + 0.7 * pos_range)):
                peak_times[count_peaks] = time[i]
                toggle_peak_status = 1
        if toggle_peak_status == 1:
            if (voltage[i] < (baseline + 0.1 * pos_range)):
                toggle_peak_status = 0

if __name__ == "main":
    main(file)
