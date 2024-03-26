import serial
import heartpy as hp
import numpy as np
import matplotlib.pyplot as plt

currSample = 0 # this is an index variable, the np array should have arr[currSample] = currentIntesnity
sampleRate = 1/(.02)  # samples every 2ms, this is the sample rate in hz
samplingTime = 50 
totalNeededSamples = samplingTime * sampleRate  # amount needed for analysis

baud = 9600
arduino = serial.Serial(port="/dev/ttyACM0",baudrate=baud,timeout=1)

bad_beatList = [0, 5, 779, 784, 788, 792, 795, 798, 800, 800, 801, 800, 799, 797, 795, 792, 789, 788, 785, 783, 783, 781, 779, 778, 776, 774, 773, 802, 800, 799, 798, 798, 798, 798, 799, 798, 798, 799, 800, 802, 804, 806, 808, 812, 815, 817, 822, 825, 827, 830, 832, 833, 834, 834, 832, 832, 830, 828, 827, 827, 822, 819, 817, 815, 813, 813, 812, 811, 811, 811, 811, 812, 812, 813, 815, 816, 816, 817, 818, 818, 819, 817, 817, 818, 817, 817, 816, 814, 813, 813, 813, 814, 815, 817, 820, 825, 828, 832, 835, 838, 840, 842, 845, 846, 848, 849, 849, 849, 850, 852, 856, 864, 872, 886, 901, 919, 939, 962, 983, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 979, 960, 939, 918, 895, 874, 853, 835, 817, 804, 794, 786, 781, 779, 779, 780, 785, 791, 798, 807, 816, 827, 838, 852, 865, 878, 890, 900, 910, 917, 921, 925, 926, 923, 920, 915, 908, 900, 893, 884, 876, 868, 858, 849, 840, 830, 822, 814, 807, 801, 796, 792, 791, 790, 787, 787, 785, 785, 785, 786, 787, 787, 788, 788, 788, 789, 789, 789, 792, 793, 793, 795, 796, 796, 797, 798, 798, 799, 799, 798, 797, 795, 793, 791, 789, 787, 787, 787, 786, 786, 787, 788, 790, 792, 794, 798, 801, 803, 804, 805, 803, 803, 802, 800, 800, 799, 797, 795, 793, 789, 786, 785, 783, 780, 779, 777, 777, 776, 777, 779, 781, 782, 784, 786, 787, 789, 791, 793, 794, 794, 794, 794, 794, 793, 793, 792, 792, 790, 790, 790, 789, 789, 789, 789, 789, 790, 791, 794, 798, 802, 810, 822, 835, 853, 873, 895, 919, 944, 968, 990, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 994, 987, 969, 951, 933, 915, 900, 885, 871, 860, 851, 843, 837, 832, 827, 823, 818, 813, 808, 806, 804, 803, 803, 804, 806, 808, 811, 815, 821, 827, 835, 843, 851, 858, 864, 869, 873, 878, 882, 884, 888, 889, 889, 888, 886, 881, 877, 872, 865, 860, 854, 847, 842, 836, 830, 825, 820, 814, 810, 805, 801, 796, 792, 786, 781, 778, 773, 769, 766, 761, 757, 753, 748, 744, 741, 738, 736, 736, 736, 738, 740, 743, 745, 747, 749, 751, 753, 755, 756, 758, 760, 761, 763, 765, 766, 768, 769, 770, 772, 773, 775, 776, 777, 777, 778, 780, 780, 782, 783, 784, 783, 783, 782, 781, 779, 778, 778, 780, 782, 784, 788, 791, 793, 796, 797, 798, 800, 801, 801, 801, 800, 799, 798, 799, 798, 797, 796, 793, 790, 787, 782, 778, 775, 771, 768, 766, 764, 763, 763, 761, 761, 760, 759, 759, 761, 762, 764, 767, 769, 772, 775, 777, 779, 784, 789, 797]


def clean(currString):
	reconstructedInt = ""
	for char in currString:
		if char.isdigit():
			reconstructedInt += char
	if reconstructedInt == "":
		return 0
	return int(reconstructedInt)
	

#use heartrate analysis, needs a np.array and the sampling rate
def sample():
	print("place hand on hrm")
	currSample = 0
	beatList=[]
	while len(beatList) < totalNeededSamples:
		
		currString = str(arduino.readline())
		# the readline is dirty, just extract the number.
		currIntensity = clean(currString)
		#add in a the intesntiy and the currSample to the hr analysis (read the docs)
		currSample+=1
		if (currSample % 100 == 0):
			print("sampling " + str(100*currSample/totalNeededSamples) +"% done")
		beatList.append(currIntensity)
	return beatList
'''
dataAverage = np.average(np.asarray(beatList))
minimum = np.min(np.asarray(beatList))
maximum = np.max(np.asarray(beatList))
for n in np.asarray(beatList):
	factor = 1.0
	ku = np.log(maximum) - np.log(minimum)
	kd = maximum - minimum
	k = ku / kd
	b = 0.2 * np.exp(-k * minimum)
	factor = b * np.exp(k * n)
	n *= factor
'''
#make this into a 2d numpy array
beatList=sample()
print(beatList)

beatArray = np.asarray(beatList)
beatList2= []
for point in beatList:
	if not(point < 200 or point > 800):
		beatList2.append(point)



indexList = [i for i in range(1, len(beatList2) + 1)]
indexArray = np.asarray(indexList)
plt.plot(indexArray, np.asarray(beatList2))

try:
	wd, m = hp.process(np.asarray(beatList2), sample_rate = sampleRate)

	#display measures computed
	for measure in m.keys():
	    print('%s: %f' %(measure, m[measure]))
except:
	print("Couldnt analyze!")
	pass
plt.show()

