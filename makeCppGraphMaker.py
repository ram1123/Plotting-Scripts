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
print '//Define the variables'
print '\tFloat_t %s, %s, %s;'%(VarInTextFile[0],VarInTextFile[1],VarInTextFile[2])
print '\tvector<float> v_%s, v_%s, v_%s;'%(VarInTextFile[0],VarInTextFile[1],VarInTextFile[2])
print ''
print ''
print '\tInt_t nlines = 0;'
print '\tTFile *f = new TFile("%s.root","RECREATE");'%OutPutCodeName
print '\tTNtuple *ntuple = new TNtuple("ntuple","data from ascii file","%s:%s:%s");'%(VarInTextFile[0],VarInTextFile[1],VarInTextFile[2])
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
print '\t\tstringstream(line) >> %s >> %s >> %s;'%(VarInTextFile[0],VarInTextFile[1],VarInTextFile[2])
print '\t\t'
print '\t\tcout<<"===> "<<%s <<"\t "<<%s<<"\t"<<%s<<endl;'%(VarInTextFile[0],VarInTextFile[1],VarInTextFile[2])
print '\t\tv_%s.push_back(%s);'%(VarInTextFile[0],VarInTextFile[0])
print '\t\tv_%s.push_back(%s);'%(VarInTextFile[1],VarInTextFile[1])
print '\t\tv_%s.push_back(%s);'%(VarInTextFile[2],VarInTextFile[2])
print '\t\tntuple->Fill(%s,%s,%s);'%(VarInTextFile[0],VarInTextFile[1],VarInTextFile[2])
print '\t}'

print '\tin.close();'
print '\t'
print '\tTGraphErrors * gr = new TGraphErrors(v_%s.size()); '%VarInTextFile[0]
print '\t    '
print '\tfor (unsigned int i = 0; i<v_%s.size();i++)'%VarInTextFile[0]
print '\t{'
print '\t        gr->SetPoint(i,v_%s[i],v_%s[i]);'%(VarInTextFile[0],VarInTextFile[1])
print '\t        gr->SetPointError(i,0,v_%s[i]);'%VarInTextFile[2]
print '\t}'
 
print '\t'
print '\t'


print '\tgr->SetTitle("");'
print '\t//gr->SetTitle("%s vs %s");'%(VarInTextFile[0],VarInTextFile[1])
print '\tgr->GetXaxis()->SetTitle("%s");'%xlabel
print '\tgr->GetYaxis()->SetTitle("%s");'%ylabel
print '\tgr->GetYaxis()->SetTitleOffset(%i);'%yoffset
print '\tgr->GetXaxis()->SetTitleOffset(%i);'%xoffset
print '\tgr->GetYaxis()->SetTitleSize(0.05);'
print '\tgr->GetXaxis()->SetTitleSize(0.05);'
print '\t//gr->GetXaxis()->SetLabelSize(0.05);'
print '\tgr->GetYaxis()->SetRangeUser(%i,%i);'%(yrange[0],yrange[1])
print '\tgr->SetMarkerSize(1);'
print '\tgr->SetMarkerColor(2);'
print '\tgr->SetMarkerStyle(21);'
print '\t'
print '\tgr->Draw("ALP");'
print '\t'
for leg in range(0,len(legends)):
	print '\tTLatex *text%i = new TLatex(%i,%i,"%s");'%(leg,pos1,pos2-((pos2/100.)*sep*leg),legends[leg])

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
print '\tTLatex *cmsprem = new TLatex(%i,%i,"#it{CMS Preliminary}");'%(cpos1,cpos2)
print ''
print '\tTLatex *gen = new TLatex(%i,%i,"%s");'%(cpos3,cpos2,DetInfo)
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