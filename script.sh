echo -n "Enter Input File name : "
read InputFileName

echo -n "Enter Outfile file name without extension : "
read OutPutFileName

echo "Enter histo details Nbins, Min Range and Max Range : "
echo -n "Nbins = "
read Nbins
echo -n "Histo min range = "
read hmin
echo -n "Histo max range = "
read hmax

root -l HistoPlot.C\(\"$InputFileName\",\"$OutPutFileName\",$Nbins,$hmin,$hmax,1,1,1\)
