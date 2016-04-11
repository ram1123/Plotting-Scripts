#include "Riostream.h"
#include "vector.h"
#include "TGraphErrors.h"

void basic() {
//  Read data from an ascii file and create a root file with an histogram and an ntuple.
//   see a variant of this macro in basic2.C
//Author: Rene Brun


// read file $ROOTSYS/tutorials/tree/basic.dat
// this file has 3 columns of float data
   TString dir = gSystem->UnixPathName(__FILE__);
   dir.ReplaceAll("basic.C","");
   dir.ReplaceAll("/./","/");
   ifstream in;
   in.open(Form("%sRPC_Eff_Aashi.dat",dir.Data()));

   Float_t voltage, efficiency;
   vector<float> v_voltage, v_efficiency;

   Int_t nlines = 0;
   TFile *f = new TFile("RPC_Eff_Aashi.root","RECREATE");
   TNtuple *ntuple = new TNtuple("ntuple","data from ascii file","Voltage:Efficiency");
   TCanvas *c1 = new TCanvas("c1","Voltage_vs_Efficiency");

string line;
while(getline(in,line))
{
        if(line[0] == '#') continue;

	stringstream(line) >> voltage >> efficiency;
	
	cout<<"===> "<<voltage <<"\t "<<efficiency<<endl;
	v_voltage.push_back(voltage);
	v_efficiency.push_back(efficiency);
	ntuple->Fill(voltage,efficiency);
}
   printf(" found %d points\n",v_voltage.size());
   in.close();

   TGraphErrors * gr = new TGraphErrors(v_voltage.size()); 
    
   for (unsigned int i = 0; i<v_voltage.size();i++)
{
	gr->SetPoint(i,v_voltage[i],v_efficiency[i]);
	gr->SetPointError(i,0,0);
}

   gr->SetTitle("Voltage vs Efficiency");
   gr->GetXaxis()->SetTitle("Voltage (kV)");
   gr->GetYaxis()->SetTitle("Efficiency (%)");
   gr->SetMarkerSize(1);
   gr->SetMarkerColor(2);
   gr->SetMarkerStyle(21);

   gr->Draw("ALP");
   c1->Write();
   c1->SaveAs("Voltage_Vs_Efficiency.pdf");
   c1->SaveAs("Voltage_Vs_Efficiency.eps");
   f->Write();
}
