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

print '#include "TGraphErrors.h"'
print '#include "setTDRStyle.C"'

print 'void %s(){'%OutPutCodeName
print 'ifstream in;'
print 'in.open("%s");'%InputData
print 'TGaxis::SetMaxDigits(%i);'%setMaxdigit
print 'gStyle->SetOptStat(%i);'%getstat
print '// Set TDR Style'
print 'setTDRStyle();'

print 'Float_t var1, var2, var3;'
print 'vector<float> v_var1, v_var2, v_var3;'

print 'Int_t nlines = 0;'
print 'TFile *f = new TFile("%s.root","RECREATE");'%OutPutCodeName
print 'TNtuple *ntuple = new TNtuple("ntuple","data from ascii file","%s:%s:%s");'%(VarInTextFile[0],VarInTextFile[1],VarInTextFile[2])
print 'TCanvas* c1 = new TCanvas("c1","",1);'
print 'c1->Range(0,0,1,1);'
print 'TPad *pad = new TPad("pad","",0,0,1,1);'
print 'pad->SetGrid();'
print 'pad->Draw();'
print 'pad->cd();'

print 'string line;'
print 'while(getline(in,line))'
print '{'
print "        if(line[0] == '#') continue;"
print ''
print '        stringstream(line) >> var1 >> var2 >> var3;'
print '        '
print '        cout<<"===> "<<var1 <<"\t "<<var2<<"\t"<<var3<<endl;'
print '        v_var1.push_back(var1);'
print '        v_var2.push_back(var2);'
print '        v_var3.push_back(var3);'
print '        ntuple->Fill(var1,var2,var3);'
print '}'

print '   in.close();'
print ''
print '   TGraphErrors * gr = new TGraphErrors(v_var1.size()); '
print '    '
print '   for (unsigned int i = 0; i<v_var1.size();i++)'
print '{'
print '        gr->SetPoint(i,v_var1[i],v_var2[i]);'
print '        gr->SetPointError(i,0,v_var3[i]);'
print '}'



print '   gr->SetTitle("");'
print '   //gr->SetTitle("var1 vs var2");'
print '   gr->GetXaxis()->SetTitle("%s");'%xlabel
print '   gr->GetYaxis()->SetTitle("%s");'%ylabel
print '   gr->GetYaxis()->SetTitleOffset(%i);'%yoffset
print '   gr->GetXaxis()->SetTitleOffset(%i);'%xoffset
print '   gr->GetYaxis()->SetTitleSize(0.05);'
print '   gr->GetXaxis()->SetTitleSize(0.05);'
print '   //gr->GetXaxis()->SetLabelSize(0.05);'
print '   gr->GetYaxis()->SetRangeUser(%i,%i);'%(yrange[0],yrange[1])
print '   gr->SetMarkerSize(1);'
print '   gr->SetMarkerColor(2);'
print '   gr->SetMarkerStyle(21);'
print ''
print '   gr->Draw("ALP");'
print ''
for leg in range(0,len(legends)):
	print 'TLatex *text%i = new TLatex(%i,%i,"%s");'%(leg,pos1,pos2-((pos2/100.)*sep*leg),legends[leg])

print ''
for leg in range(0,len(legends)):
	print 'text%i->SetTextFont(42);'%leg
print ''
for leg in range(0,len(legends)):
	print 'text%i->SetTextSize(0.05);'%leg
print ''
for leg in range(0,len(legends)):
	print 'text%i->Draw("same");'%leg
print ''
print ''
print ''
print '   TLatex *cmsprem = new TLatex(%i,%i,"#it{CMS Preliminary}");'%(cpos1,cpos2)
print ''
print '   TLatex *gen = new TLatex(%i,%i,"GE1/1");'%(cpos3,cpos2)
print ''
print '   cmsprem->Draw("same");'
print '   gen->Draw("same");'
print ''
print ''
print ''
print '   c1->Write();'
print '   c1->SaveAs("HighVoltage_Vs_SpaceResolution.pdf");'
print '   c1->SaveAs("HighVoltage_Vs_SpaceResolution.png");'
print '   c1->SaveAs("HighVoltage_Vs_SpaceResolution.root");'
print '   c1->SaveAs("HighVoltage_Vs_SpaceResolution.C");'
print '   f->Write();'

print '}'

################
#  Close file  #
################
