OutPutCodeName="Current_vs_ClusterSize_2065_2123"
InputData="/home/ramkrishna/PhD_New_Dir_16July2016/GEM/GEM_TB/TB_2014/FNAL-Beam-Test-Scripts_2014_19Aug/Iteration_PostionLC1_inclusive_X_-2540.00.txt"	# Can give this with full path
xlabel="Current Supplied to HV Divider (#mu A)"
ylabel="Cluster Size"

VarInTextFile=["IterNbX","IterNbY","PreShif2X","PreShif2Y","MeanEta5","SigmaEta5","XChi2","YChi2","TotalChi2"]  # Each element of list corresponds to one column of intput text file

VarToPlot=["IterNbX","SigmaEta5"]

GraphTitle="Current Vs Cluster Size"	

legends=[
	"Run Range: 2065-2123",
	"(i#eta,i#phi)=(1,2)",
	"Latency = 17"
	]

yrange=[0.0014,0.00144]	# Y range

xscaleFactor=0.0	# if you don't want to scale x-values then put it = 0.0
yscaleFactor=0.0	# if you don't want to scale y-values then put it = 0.0

pos1=0.15		# Legend x pos
pos2=0.8		# Legend y pos
sep=6.5			# y-distance b/w two legends fraction
cpos1=00.11		# CMS Prem x pos
cpos2=0.999		# CMS Prem y pos
cpos3=0.80		# DetInfo position
DetInfo="GE11-IV"	# Detector Info


xoffset=1.2		# X-offset
yoffset=0.9		# Y-offset

setMaxdigit=4		# SetMaximumDigit
getstat=0		# GetStats
