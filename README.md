# Graph Maker

## How To Use
1. Modify **Template.py** as per its format
2. Then run command
	
		python makeCppGraphMaker.py

3. It will create a <AcppProgram>.C file. Then run it using

		root -l -b -q <AcppProgram>.C

This step will give you graph in pdf & png form. Also it will give you a root file which contains a canvas with graph and a ntuple having input data.

If you want to modify anything which is not available in **Template.py** then you have to modify it in **makeCppGraphMaker.py**.