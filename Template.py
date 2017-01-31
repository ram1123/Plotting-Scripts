OutPutCodeName="aQGC_Plots_31Jan_FT1_12p5em12_WPlepWMhad"

datapath="/home/ramkrishna/PhD_New_Dir_16July2016/PhysicsAnalysis/aQGC_Analysis/AnalyzeLHEFiles/GraphPlot_1D/InputFiles/"

InputData=[ "FM0_par_31Jan_FT1_12p5em12_WPlepWMhad.dat", "FM1_par_31Jan_FT1_12p5em12_WPlepWMhad.dat", 
	    "FM6_par_31Jan_FT1_12p5em12_WPlepWMhad.dat", "FM7_par_31Jan_FT1_12p5em12_WPlepWMhad.dat", 
	    "FS0_par_31Jan_FT1_12p5em12_WPlepWMhad.dat", "FS1_par_31Jan_FT1_12p5em12_WPlepWMhad.dat", 
	    "FT0_par_31Jan_FT1_12p5em12_WPlepWMhad.dat", "FT1_par_31Jan_FT1_12p5em12_WPlepWMhad.dat", 
	    "FT2_par_31Jan_FT1_12p5em12_WPlepWMhad.dat" ]

xlabel="aQGC Parameter (#times 10^{-12} GeV^{-4})"
ylabel="Cross-Section (pb)"


VarInTextFile=["aQGC_par","CrossSec","ErrCrossSec"]  # Each element of list corresponds to one column of intput text file

VarToPlot=[]

GraphTitle="aQGC parameter Vs Cross-Section"

tlatexx = [
	]

legends = [
	"FM0",	"FM1",
	"FM6",	"FM7",
	"FS0",  "FS1",
	"FT0",  "FT1",
	"FT2"
	]
	
iffit = 0
fitfunction = "pol3"
fitXrange = [-4.0,4.0]

yrange=[0.0,0.0]	# Y range; For auto range set yrange[0] = yrange[1]

xscaleFactor=0.0	# if you don't want to scale x-values then put it = 0.0
yscaleFactor=0.0	# if you don't want to scale y-values then put it = 0.0

pos1=0.15		# Legend x pos
pos2=0.83		# Legend y pos
sep=6.5			# y-distance b/w two legends fraction
cpos1=00.11		# CMS Prem x pos
cpos2=0.91		# CMS Prem y pos
cpos3=0.85		# DetInfo position
DetInfo="FT1"	# Detector Info


xoffset=1.2		# X-offset
yoffset=1.0		# Y-offset

setMaxdigit=4		# SetMaximumDigit
getstat=0		# GetStats
