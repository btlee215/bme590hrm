import hrmread
import hrmcalcs

def test_read():
	assert hrmread.read_ecg(file='Test_ECG.txt')== (0,0,0)  #Checks file type
	# assert hrmread.find_range([2,"3",4],[2,3,4],peakthresh = 0.7,basethresh = 0.1 ) == "Time values must be floats"
	assert hrmread.find_range([0,0.5,1,1.5,2.0],[10,20,30,40,50],peakthresh = 0.7,basethresh = 0.1 ) == [2.0]

def test_instant():
	# assert hrmcalcs.hrminstant([0.05,2.0,2.5,3.75,"5"])== "Error: Time values must be floats"
	assert hrmcalcs.hrminstant([10,20,30,40,50]) == [6,6,6,6]

# def test_average():
#	assert hrmfunction.hrmaverage()==
#	assert hrmfunction.hrmaverage()==

def test_tachbrady():
	assert hrmcalcs.hrmtb([50,50,50,75,110,110,110]) ==([0,0,0,0,0,0,1],[0,0,1,0,0,0,0])

#def test_inputs():
#	assert hrmfunction.average () == "Please enter an integer input"
 

#brady = [instantHR[i:i+3] for i in range(len(instantHR)-1)]
#tachy = [instantHR[i:i+3] for i in range(len(instantHR)-1)]
#for i in brady:
#	if (all(i <60 for i in brady) ) == 1:
#		"Potential Bradychardia?"
#for i in tachy:

