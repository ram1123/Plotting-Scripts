OutPutCodeName="SpaceResolution_vs_HV"
InputData="SpaceResolutionInfo.txt"
xlabel="Current Supplied To HV Divider (#mu A)"
ylabel="Space Resolution (#mu rad)"

VarInTextFile=["CurrentSuppliedToHVDivider","Space_Resolution","Err_SpaceResolution"]  # Each element of list corresponds to one column of intput text file

GraphTitle="Space Resolution Vs Current Supplied to HV Divider"	

legends=[
	"Threshold = 1.2 fC"
	,"Beam: Muon"
	,"Gap Config: 3/1/2/1 mm"
	,"Gas: Ar/CO2/CF4 (45/15/40)"
	,"Run Range: 1592-1646"
	,"(i#eta,i#phi)=(5,2)"
	]

pos1=770		# Legend x pos
pos2=1280		# Legend y pos
sep=1.5			# y-distance b/w two legends fraction
cpos1=734		# CMS Prem x pos
cpos2=1385		# CMS Prem y pos
cpos3=798		# DetInfo position
DetInfo="GE11_IV"	# Detector Info

yrange=[1140,1380]	# Y range

xoffset=1.2		# X-offset
yoffset=1.9		# Y-offset

setMaxdigit=4		# SetMaximumDigit
getstat=0		# GetStats
