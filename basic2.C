void basic2() {
//   example of macro to create can ntuple reading data from an ascii file.
//   This macro is a variant of basic.C
//Author: Rene Brun


   TFile *f = new TFile("basic2.root","RECREATE");

   TH2F *h1 = new TH2F("h1","x distribution",100,0,12,100,0,100);

   TTree *T = new TTree("ntuple","data from ascii file");

   Long64_t nlines = T->ReadFile("RPC_Eff_Aashi.dat","x:y");
   printf(" found %lld points\n",nlines);
   T->Draw("x:y>h1");
   T->Write();
}
