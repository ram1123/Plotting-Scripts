OutPutCodeName="ShiftLinear_Shift_vs_Chi2"
InputData="/home/ramkrishna/PhD_New_Dir_16July2016/GEM/GEM_TB/TB_2014/FNAL-Beam-Test-Scripts_2014_19Aug/ShiftLinear_Shift_vs_Chi2.dat"	# Can give this with full path
xlabel="Intercept"
ylabel="#Chi^{2}"

VarInTextFile=["Intercept","ChiSquare","Err_ChiSquare"]  # Each element of list corresponds to one column of intput text file

GraphTitle="#Chi^2 vs Intercept"	

legends=[
	]

yrange=[0.0000,35.0]	# Y range

xscaleFactor=0.0	# if you don't want to scale x-values then put it = 0.0
yscaleFactor=0.0	# if you don't want to scale y-values then put it = 0.0

pos1=0.15		# Legend x pos
pos2=0.8		# Legend y pos
sep=6.5			# y-distance b/w two legends fraction
cpos1=-9.11		# CMS Prem x pos
cpos2=0.91		# CMS Prem y pos
cpos3=0.85		# DetInfo position
DetInfo="FT2"	# Detector Info


xoffset=1.2		# X-offset
yoffset=0.9		# Y-offset

setMaxdigit=4		# SetMaximumDigit
getstat=0		# GetStats
