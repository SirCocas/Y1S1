import argparse
import scipy.stats as stats
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
import scalogram
from baseObsWindows import slidingMultObsWindow

def plotPeriodogram(data):
    # fft=np.fft.fft(data)
    # psd=abs(fft)**2
    # plt.plot(psd[:50])
    
    f,psd=signal.periodogram(data)
    plt.plot(1/f[:50],psd[:50])
    plt.show()
    
def plotScalogram(data):
    scales=np.arange(1,50)
    S,scales=scalogram.scalogramCWT(data,scales)
    plt.plot(scales,S)
    plt.show()

def plotPeriodicityFeatures(obsData):
    if type(obsData) is list:
        nLengthsObsWindow=len(obsData)
        nObs,nSamples,nMetrics=obsData[0].shape
    else:
        nLengthsObsWindow=1
        nObs,nSamples,nMetrics=obsData.shape


    for o in range(0,nObs):
        for n in range(0,nLengthsObsWindow):
            if type(obsData) is not list:
                subdata=obsData[o,:,1]   # feature on column 1
            else:
                print(n,o)
                subdata=obsData[n][o,:,1]
    
            plt.title("Observation {}, feature in column 1".format(o))
            #plotPeriodogram(subdata)
            plotScalogram(subdata)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='?',required=True, help='input file')
    args=parser.parse_args()
    
    fileInput=args.input
        
    data=np.loadtxt(fileInput,dtype=int)
    
    # plt.subplot(2,1,1)
    # plt.plot(data[:,0],data[:,1],data[:,0],data[:,3])
    # plt.subplot(2,1,2)
    # plt.plot(data[:,0],data[:,2],data[:,0],data[:,4])
    # plt.show()
            
    obsWindows=[128]
    slidingValue=32
    obsData=slidingMultObsWindow(data[:,:2],obsWindows,slidingValue)
    plotPeriodicityFeatures(obsData)
        

if __name__ == '__main__':
    main()
