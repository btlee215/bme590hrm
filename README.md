# bme590hrm
Welcome to Ben, Sameer, and Alice's HRM!

This program is designed to output the instantaneous heart rate at time values given by auser-input .CSV file. The program also outputs a "1" when Bradycardia (HR under 60 beats per minute) or Tachycardia (HR above 100 beats per minute) is detected over three consecutive time points. 

To run this file, follow the instructions below: 

1.) Open the hrmread.py file and enter the name of the .CSV file being run (Line 8)
2.) Open the hrmcalcs.py file and enter the start and end time over which the average HR should be calculated as inputs to the hrmaverage function (Line 13)
3.) Run the hrmoutput.py file by typing "python hrmoutput.py" in the terminal window. The program will output a text file titled "hrmoutput.txt" which will contain values at each time point and the average HR over the minutes specified. 


