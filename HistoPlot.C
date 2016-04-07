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
#include <vector>
#include <iostream>
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

void HistoPlot(string inputfile, string OutputFileName, 	// Input & output files
	int nbins, double hmin, double hmax,			// Histo discription
	double constant, double mean, double sigma, 		// Gauss input parameters
	bool FixPar, double minA, double maxA, double minM, double maxM, // Restrict gauss parameters
	bool getStat						// Show stat or not
	)
{
  if (getStat)
  {
  gStyle->SetOptStat(1111);
  gStyle->SetOptFit(kTRUE);
  }
  else
  gStyle->SetOptStat(0);


  TCanvas *c1= new TCanvas("c1"," ");
  ifstream in (inputfile.c_str(),std::ios_base::in);
  vector<double> data;


 TH1F *h1 = new TH1F("h1","",nbins, hmin, hmax);
 cout<<"nbins = "<<nbins<<"\thmin = "<<hmin<<"\thmax = "<<hmax<<endl;
 h1->GetXaxis()->SetTitle("Time Resolution (ns)");
 h1->GetYaxis()->SetTitle("Counts");
 h1->GetXaxis()->CenterTitle();
 h1->GetYaxis()->CenterTitle();
 h1->GetYaxis()->SetTitleOffset(1.5);
 h1->SetLineColor(1);
 h1->SetLineWidth(2);

float line;
while (in >> line)
	{
	data.push_back(line);
	h1->Fill(line);
	}

h1->Scale(1/h1->Integral());
TF1 *f1 = new TF1("f1","[0]*exp(-((x-[1])*(x-[1]))/((2*([2]*[2]+1.27*1.27))))",hmin, hmax); 
f1->SetParameters(constant, mean, sigma);
if (FixPar)
{
	//f1->SetParLimits(0, minA, maxA);
	//f1->SetParLimits(1, minM, maxM);
	f1->SetParLimits(0, (double)h1->GetBinContent(h1->GetMaximumBin()), h1->GetBinContent(h1->GetMaximumBin())+1.0);
	f1->SetParLimits(1, h1->GetMean()-1.0, h1->GetMean()+1.0);
}
f1->SetParNames("Constant","Mean","Sigma");  
 f1->SetLineWidth(2);
 f1->SetLineColor(6);

  h1->Draw();
h1->Fit(f1,"R");
TLatex *txt1 = new TLatex(1,100,"Text to show");
txt1->SetTextSize(0.03);
txt1->Draw("same");
string OutputFileNamePDF = OutputFileName+".pdf";
string OutputFileNamePNG = OutputFileName+".png";
string OutputFileNameC = OutputFileName+".C";
c1->SaveAs(OutputFileNamePDF.c_str());
c1->SaveAs(OutputFileNamePNG.c_str());
//c1->SaveAs(OutputFileNameC.c_str());
}
