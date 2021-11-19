import argparse
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from baseObsWindows import slidingMultObsWindow

   
def extractStats(data):
    nSamp,nCols=data.shape

    M1=np.mean(data,axis=0)
    Md1=np.median(data,axis=0)
    Std1=np.std(data,axis=0)
    S1=stats.skew(data)
    #K1=stats.kurtosis(data)
    p=[75,90,95,98]
    Pr1=np.array(np.percentile(data,p,axis=0)).T.flatten()
        
    features=np.hstack((M1,Md1,Std1,S1,Pr1))
    return(features)

def extratctSilenceActivity(data,threshold=0):
    if(data[0]<=threshold):
        s=[1]
        a=[]
    else:
        s=[]
        a=[1]
    for i in range(1,len(data)):
        if(data[i-1]>threshold and data[i]<=threshold):
            s.append(1)
        elif(data[i-1]<=threshold and data[i]>threshold):
            a.append(1)
        elif (data[i-1]<=threshold and data[i]<=threshold):
            s[-1]+=1
        else:
            a[-1]+=1
    return(s,a)
    
def extractStatsSilenceActivity(data):
    features=[]
    nSamples,nMetrics=data.shape
    silence_features=np.array([])
    activity_features=np.array([])
    for c in range(nMetrics):
        silence,activity=extratctSilenceActivity(data[:,c],threshold=0)
        
        if len(silence)>0:
            silence_faux=np.array([len(silence),np.mean(silence),np.std(silence)])
        else:
            silence_faux=np.zeros(3)
        silence_features=np.hstack((silence_features,silence_faux))
        
        if len(activity)>0:
            activity_faux=np.array([len(activity),np.mean(activity),np.std(activity)])
        else:
            activity_faux=np.zeros(3)
        activity_features=np.hstack((activity_features,activity_faux))       
            
    features=np.hstack((silence_features,activity_features))
        
    return(features)

def extractFeatures(obsData):
    if type(obsData) is list:
        nLengthsObsWindow=len(obsData)
        nObs,nSamples,nMetrics=obsData[0].shape
    else:
        nLengthsObsWindow=1
        nObs,nSamples,nMetrics=obsData.shape

    obsFeatures=np.zeros((0,140))
    
    for o in range(0,nObs):
        features=np.array([])
        for n in range(0,nLengthsObsWindow):
            if type(obsData) is not list:
                subdata=obsData[0]
            else:
                subdata=obsData[n][o]
                
            faux=extractStats(subdata)
            faux2=extractStatsSilenceActivity(subdata)

            features=np.hstack((features,faux,faux2))
        if o==0:
            obsFeatures=features
        else:
            obsFeatures=np.vstack((obsFeatures,features))

    return obsFeatures

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
            
    allLengthsObsWindow=[5,10]
    slidingValue=3
    obsData=slidingMultObsWindow(data,allLengthsObsWindow,slidingValue)
    features=extractFeatures(obsData)
    
    print(features)
        

if __name__ == '__main__':
    main()
