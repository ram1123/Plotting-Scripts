#! /usr/bin/env python2.6

import sys
import ROOT as rt

from Template import *

######################
#  Print C++ header  #
######################


sys.stdout = open(OutPutCodeName+".C",'w')

print "// ############################################################"
print "// # Usage                                                    #"
print "// #                                                          #"
print "// ############################################################"
print ''
print '#include "TGraphErrors.h"'
print '#include "setTDRStyle.C"'
print ''
print ''

print 'void %s(){'%OutPutCodeName
print '\tifstream in;'
print '\tin.open("%s");'%InputData
print ''
print '\tTGaxis::SetMaxDigits(%i);'%setMaxdigit
print '\tgStyle->SetOptStat(%i);'%getstat
print ''
print '\t// Set TDR Style'
print '\tsetTDRStyle();'
print ''
print '\t//Define the variables'
print '\tFloat_t ',', '.join(VarInTextFile),' ;'
pre = "v_"
Pre_VarInTextFile = [pre + x for x in VarInTextFile ]
#print Pre_VarInTextFile
Pre_VarToPlot = [pre + x for x in VarToPlot ]
#print "\n\n",Pre_VarToPlot,"\n\n"
print '\tvector<Float_t> ',', '.join(Pre_VarInTextFile),' ;'
print ''
print ''
print '\tInt_t nlines = 0;'
print '\tTFile *f = new TFile("%s.root","RECREATE");'%OutPutCodeName
print '\tTNtuple *ntuple = new TNtuple("ntuple","data from ascii file","',':'.join(VarInTextFile),'");'
print ''
print ''
print '\tTCanvas* c1 = new TCanvas("c1","",1);'
print '\tc1->Range(0,0,1,1);'
print '\tTPad *pad = new TPad("pad","",0,0,1,1);'
print '\tpad->SetGrid();'
print '\tpad->Draw();'
print '\tpad->cd();'
print ''
print ''

print '\tstring line;'
print '\twhile(getline(in,line))'
print '\t{'
print "\t\tif(line[0] == '#') continue;"
print '\t\t'
print '\t\tstringstream(line) >>',' >> '.join(VarInTextFile),';'
print '\t\t'
#print '\t\tcout<<"===> "<<',' <<"\\t" <<  '.join(VarInTextFile),'<<endl;'
print ''
for var in range(0,len(VarInTextFile)):
	if (xscaleFactor != 0.0 and yscaleFactor != 0.0):
		if (var == 0):
			print '\t\t%s.push_back(%s/%0.15f);'%(Pre_VarInTextFile[var],VarInTextFile[var],xscaleFactor)
		else:
			print '\t\t%s.push_back(%s/%0.15f);'%(Pre_VarInTextFile[var],VarInTextFile[var],yscaleFactor)
	else:
		if (xscaleFactor != 0.0 ):
			if (var == 0):
				print '\t\t%s.push_back(%s/%0.15f);'%(Pre_VarInTextFile[var],VarInTextFile[var],xscaleFactor)
			else:
				print '\t\t%s.push_back(%s);'%(Pre_VarInTextFile[var],VarInTextFile[var])
		else:
			if (yscaleFactor != 0.0 ):
				if (var == 0):
					print '\t\t%s.push_back(%s);'%(Pre_VarInTextFile[var],VarInTextFile[var])
				else:
					print '\t\t%s.push_back(%s/%0.15f);'%(Pre_VarInTextFile[var],VarInTextFile[var],yscaleFactor)
			else:
				print '\t\t%s.push_back(%s);'%(Pre_VarInTextFile[var],VarInTextFile[var])
print '\t\tntuple->Fill(',' , '.join(VarInTextFile),');'
print '\t}'

print '\tin.close();'
print '\t'
print '\tTGraphErrors * gr = new TGraphErrors(%s.size()); '%Pre_VarInTextFile[0]
print '\t    '
print '\tfor (unsigned int i = 0; i<%s.size();i++)'%Pre_VarInTextFile[0]
print '\t{'
#print '\t        gr->SetPoint(i,%s[i],%s[i]);'%(Pre_VarInTextFile[0],Pre_VarInTextFile[1])
print '\t        gr->SetPoint(i,%s[i],%s[i]);'%(Pre_VarToPlot[0],Pre_VarToPlot[1])
if (len(Pre_VarToPlot)==3):
	print '\t        gr->SetPointError(i,0,%s[i]);'%Pre_VarToPlot[2]
else:
	print '\t        gr->SetPointError(i,0,0);'
print '\t}'
print '\t'
print '\t'
print '\tgr->SetTitle("");'
print '\t//gr->SetTitle("%s vs %s");'%(VarInTextFile[0],VarInTextFile[1])
print '\tgr->GetXaxis()->SetTitle("%s");'%xlabel
print '\tgr->GetYaxis()->SetTitle("%s");'%ylabel
print '\tgr->GetYaxis()->SetTitleOffset(%f);'%yoffset
print '\tgr->GetXaxis()->SetTitleOffset(%f);'%xoffset
print '\tgr->GetYaxis()->SetTitleSize(0.05);'
print '\tgr->GetXaxis()->SetTitleSize(0.05);'
print '\t//gr->GetXaxis()->SetLabelSize(0.05);'
print '\tgr->GetYaxis()->SetRangeUser(%f,%f);'%(yrange[0],yrange[1])
print '\tgr->SetMarkerSize(1);'
print '\tgr->SetMarkerColor(2);'
print '\tgr->SetMarkerStyle(21);'
print '\t'
print '\tgr->Draw("ACP");'
#print '\tgr->Draw("ALP");'
print '\t'
for leg in range(0,len(legends)):
	print '\tTLatex *text%i = new TLatex(%f,%f,"%s");'%(leg,pos1,pos2-((pos2/100.)*sep*leg),legends[leg])

print ''
for leg in range(0,len(legends)):
	print '\ttext%i->SetNDC();'%leg
print ''
for leg in range(0,len(legends)):
	print '\ttext%i->SetTextFont(42);'%leg
print ''
for leg in range(0,len(legends)):
	print '\ttext%i->SetTextSize(0.05);'%leg
print ''
for leg in range(0,len(legends)):
	print '\ttext%i->Draw("same");'%leg
print ''
print ''
print ''
print '\tTLatex *cmsprem = new TLatex(%f,%f,"#it{CMS Preliminary}");'%(cpos1,cpos2)
print '\tcmsprem->SetNDC();'
print ''
print '\tTLatex *gen = new TLatex(%f,%f,"%s");'%(cpos3,cpos2,DetInfo)
print '\tgen->SetNDC();'
print ''
print '\tcmsprem->Draw("same");'
print '\tgen->Draw("same");'
print ''
print ''
print ''
print '\tc1->Write();'
print '\tc1->SaveAs("%s.pdf");'%OutPutCodeName
print '\tc1->SaveAs("%s.png");'%OutPutCodeName
print '\tc1->SaveAs("%s.root");'%OutPutCodeName
print '\tf->Write();'

print '}'

################
#  Close file  #
################
