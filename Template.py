OutPutCodeName="SpaceResolution_vs_HV"
InputData="SpaceResolutionInfo.txt"
xlabel="Current Supplied To HV Divider (#mu A)"
ylabel="Space Resolution (#mu rad)"

VarInTextFile=["CurrentSuppliedToHVDivider","Space_Resolution","Err_SpaceResolution"]

GraphTitle="Space Resolution Vs Current Supplied to HV Divider"

legends=[
	"Threshold = 1.2 fC"
	,"Beam: Muon"
	,"Gap Config: 3/1/2/1 mm"
	,"Gas: Ar/CO2/CF4 (45/15/40)"
	,"Run Range: 1592-1646"
	,"(i#eta,i#phi)=(5,2)"
	]

pos1=770	
pos2=1280
sep=1.5
cpos1=734
cpos2=1385
cpos3=798

yrange=[1140,1380]

xoffset=1.2
yoffset=1.9

setMaxdigit=4
getstat=0
