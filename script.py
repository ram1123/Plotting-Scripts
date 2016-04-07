import sys
import os
import datetime
import argparse
import string

if __name__ == '__main__':
    parser = argparse.ArgumentParser (description = 'Make RPC plots')
    parser.add_argument ('-i'	, '--InputFile'  , default = 'output1.txt'	, help='put input file name with or without path')
    parser.add_argument ('-o'	, '--OutputFile' , default = 'Ankit'		, help='put output file name without extension')
    parser.add_argument ('-n'	, '--Nbins'      , default = '25'		, help='put number of bins')
    parser.add_argument ('-min'	, '--HMin'      , default = '7'           	, help='put bins for HMax')
    parser.add_argument ('-max'	, '--HMax'      , default = '40'        	, help='put bins for Hmin')
    parser.add_argument ('-c'	, '--Constant'      , default = '1'	        , help='put the value of constant')
    parser.add_argument ('-m'	, '--Mean'      , default = '1'	                , help='put the value of mean')
    parser.add_argument ('-s'	, '--Sigma'      , default = '1'	        , help='put the value of sigma0')
    parser.add_argument ('-p'	, '--FixPar'      , default = '0'	        , help='put the value of sigma0')
    parser.add_argument ('-mA'	, '--minArea'      , default = '0.20'	        , help='put the value of sigma0')
    parser.add_argument ('-MA'	, '--maxArea'      , default = '0.22'	        , help='put the value of sigma0')
    parser.add_argument ('-mM'	, '--minMean'      , default = '19'	        , help='put the value of sigma0')
    parser.add_argument ('-MM'	, '--maxMean'      , default = '20'	        , help='put the value of sigma0')
    parser.add_argument ('-stat', '--GetStat'   , default = '1'                 , help='show stat box or not')
    args = parser.parse_args ()



print '========================================================================='
print 'Start Running HistoPlot.C...'

#print('root -l -b -q SelectTrackerEvents.C\(\\"'+args.InputFile+'\\",'+args.RunNumber+',\\"'+args.Det+'\\"\)')

print('root -l -b -q HistoPlot.C\(\\"'+args.InputFile+'\\",\\"'+args.OutputFile+'\\",'+args.Nbins+','+args.HMin+','+args.HMax+','+args.Constant+','+args.Mean+','+args.Sigma+'\)')
os.system('root -l -b -q HistoPlot.C\(\\"'+args.InputFile+'\\",\\"'+args.OutputFile+'\\",'+args.Nbins+','+args.HMin+','+args.HMax+','+args.Constant+','+args.Mean+','+args.Sigma+','+args.FixPar+','+args.minArea+','+args.maxArea+','+args.minMean+','+args.maxMean+'\)')

print '\n\nHistoPlot.C... DONE...\n\n'
