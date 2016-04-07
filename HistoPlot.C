/*
 * =====================================================================================
 *
 *       Filename:  HistoPlot.C
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Thursday 07 April 2016 12:17:55  IST
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ram Krishna Sharma (), ramkrishna.sharma71@gmail.com
 *   Organization:  University of Delhi
 *
 * =====================================================================================
 */

#include <iostream>
#include <vector>
#include <string>
#include "TROOT.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TLatex.h"
#include "TMarker.h"
#include "TString.h"
#include "TFile.h"
#include "TTree.h"
#include "TMath.h"
#include "TH1.h"
#include "TF1.h"

void HistoPlot(	/* bool FixPar, bool getStat	*/					// Show stat or not
		)
{
  TFile *file = new TFile("Timing_Data_07042016.root","RECREATE");
  //TDirectory *cditof = file->mkdir("tof");


  //if (getStat)
  if (1)
  {
  //gStyle->SetOptStat(1111);
  gStyle->SetOptFit(kTRUE);
  }
  else
  gStyle->SetOptStat(0);

  string InputFileName, TreeName, OutPutFileName;
  int Nbins, min, max;
  vector<string> v_InputFileName, v_TreeName, v_OutPutFileName;
  vector<int> v_Nbins, v_min, v_max;

  ifstream infile;
  infile.open ("Template.txt");
  string line; 
  int count_Dir = 0;
  string Temp_Dir;
  vector<string> Dir_Names;
  int i = 0;
  
  while(getline(infile,line))
	{
	line.erase(line.begin(), find_if(line.begin(), line.end(), not1(ptr_fun<int, int>(isspace)))); 

        if(line[0] == '#') continue;

	stringstream(line) >> InputFileName >> TreeName >> OutPutFileName >> Nbins >> min >> max;

	v_InputFileName.push_back(InputFileName);
	v_TreeName.push_back(TreeName);
	v_OutPutFileName.push_back(OutPutFileName);
	v_Nbins.push_back(Nbins);
	v_min.push_back(min);
	v_max.push_back(max);
        
	if (i==0)	
	{
	Temp_Dir = TreeName;
	Dir_Names.push_back(TreeName);
	}
	if (i>0)
	{
		if (Temp_Dir != TreeName)
			{
			count_Dir++;
			Temp_Dir = TreeName;
			Dir_Names.push_back(TreeName);
			}
	}
	//cout<<"Temp_Dir = "<<Temp_Dir<<endl;
	//cout<<"InputFileName = "<< InputFileName <<"\tTreeName = "<<TreeName<<"\tOutPutFileName = "<<OutPutFileName<<"\tNbins = "<<Nbins<<"\t min = "<<min<<"\tmax = "<<max<<endl;
	i++;
	} 
  infile.close();

  TDirectory **TD = new TDirectory*[Dir_Names.size()];
  TNtuple **ntuple = new TNtuple*[v_InputFileName.size()];
  TH1F **th = new TH1F*[v_InputFileName.size()];
//  TCanvas *c1 = new TCanvas("test");
//  TCanvas ** tc = new TCanvas*[v_InputFileName.size()];

  for (int dirn = 0; dirn<Dir_Names.size(); dirn++)
		TD[dirn] = file->mkdir(Dir_Names[dirn].c_str());
//	cout<<"=============================== Dir Name = "<<Dir_Names[dirn]<<endl;

  
  int countDir = 0;
  string treeName;
  for (int fileNum = 0; fileNum<v_InputFileName.size(); fileNum++)
  {
//	c1->cd();
	//cout<<"v_InputFileName : "<<v_InputFileName[fileNum]<<endl;
	ntuple[fileNum] = new TNtuple(v_OutPutFileName[fileNum].c_str(),v_OutPutFileName[fileNum].c_str(),v_OutPutFileName[fileNum].c_str());
	th[fileNum] = new TH1F(Form("th%i",fileNum),v_OutPutFileName[fileNum].c_str(),25,0,40);

	if (fileNum == 0) 
	{
		treeName = v_TreeName[fileNum];		TD[fileNum]->cd();
	}
	if ( treeName != v_TreeName[fileNum] ) {
		countDir++;		TD[countDir]->cd();		treeName = v_TreeName[fileNum];
		cout<<"Tree Name = "<<treeName<<endl;
	}
	
		cout<<"Outside loop Tree Name = "<<treeName<<endl;
		
	ifstream in (v_InputFileName[fileNum].c_str(),std::ios_base::in);	// Read new data file
	while (in >> line)							// loop over all the entries in the loaded data file
	{
	double temp = ::atof(line.c_str());
	ntuple[fileNum]->Fill(temp);	th[fileNum]->Fill(temp);
	}						// while loop ends
	in.close();					// close the loded data file
//	ntuple[fileNum]->Write();			// write the ntuple in the root file

	TF1 *f1 = new TF1("f1","[0]*exp(-((x-[1])*(x-[1]))/((2*([2]*[2]+1.27*1.27))))",10,30); 
	f1->SetParameters((double)th[fileNum]->GetBinContent(th[fileNum]->GetMaximumBin()), th[fileNum]->GetMean(), 1.0);
	bool FixPar = 1;
	if (FixPar)
	{
		f1->SetParLimits(0, (double)th[fileNum]->GetBinContent(th[fileNum]->GetMaximumBin()), th[fileNum]->GetBinContent(th[fileNum]->GetMaximumBin())+2.0);
		f1->SetParLimits(1, th[fileNum]->GetMean()-2.0, th[fileNum]->GetMean()+2.0);
	}
	f1->SetParNames("Constant","Mean","Sigma");  
	f1->SetLineWidth(2);
 	f1->SetLineColor(6);

	th[fileNum]->Draw();
	th[fileNum]->Fit(f1,"RQ");
//	c1->Write();
//	c1->Clear();
  }
  file->Write();
  delete file;
}
