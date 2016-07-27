/* 
 *	This code reads root file using eventwise
 *
 */
void TreeFiller_histo() {

TFile f("egammaEffi.txt_SF2D.root");
TH2F *h = (TH2F*)f.Get("EGamma_SF2D");
 
TFile f1("/tmp/rasharma/eos/cms/store/group/phys_egamma/tnp/80X/Photons_76Xids/elev2/mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root");
TFile f2("mc_DY_madgraph_ele.puTree.root");
TTree *T1 = (TTree*)f1.Get("GsfElectronToEleID/fitter_tree");
TTree *T2 = (TTree*)f2.Get("weights_2016_runB");//->AddFriend("weights_2016_runB","mc_DY_madgraph_ele.puTree.root");

TFile *file = new TFile("DY_Madgraph_80X_histos.root","RECREATE");
 
int event_nPV;
float event_rho;
double totWeight;
double totWeight2;

T1->SetBranchAddress("event_nPV", &event_nPV);
T1->SetBranchAddress("event_rho", &event_rho);
T1->SetBranchAddress("totWeight",&totWeight);
T2->SetBranchAddress("totWeight",&totWeight2);

TH1D *h_probe_eta_bin1 = new TH1D("h_probe_eta_bin1","Probe Eta", 50,-2.5,2.5);
TH1D *h_probe_eta_up_bin1 = new TH1D("h_probe_eta_up_bin1","Probe Eta", 50,-2.5,2.5);
TH1D *h_probe_eta_down_bin1 = new TH1D("h_probe_eta_down_bin1","Probe Eta", 50,-2.5,2.5);

h_probe_eta_bin1->Sumw2();
h_probe_eta_up_bin1->Sumw2();
h_probe_eta_down_bin1->Sumw2();

 int nentries = T1->GetEntries();
cout << "nentries = " << nentries << endl;
 for (unsigned int j = 1; j <= nentries ; j++ ) {
   T1->GetEntry(j);
	T2->GetEntry(j);

if(j%100000 == 0) cout << "Events Processed = " << j << endl;
h_probe_eta_bin1->Fill(event_nPV);
h_probe_eta_up_bin1->Fill(totWeight);
h_probe_eta_down_bin1->Fill(totWeight2);
} //event loop
 file->Write();
}

