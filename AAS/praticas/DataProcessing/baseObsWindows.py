import argparse
import numpy as np
import matplotlib.pyplot as plt

def seqObsWindow(data,lengthObsWindow):
    iobs=0
    nSamples,nMetrics=data.shape
    obsData=np.zeros((0,lengthObsWindow,nMetrics))
    for s in np.arange(lengthObsWindow,nSamples,lengthObsWindow):
        subdata=data[s-lengthObsWindow:s,:]
        obsData=np.insert(obsData,iobs,subdata,axis=0)
        iobs+=1
        
        print("\nAt sample: {}\n".format(s-1))
        print(subdata)

    return obsData # 3D arrays (obs, sample, metric)
        
def slidingObsWindow(data,lengthObsWindow,slidingValue):
    iobs=0
    nSamples,nMetrics=data.shape
    obsData=np.zeros((0,lengthObsWindow,nMetrics))
    for s in np.arange(lengthObsWindow,nSamples,slidingValue):
        subdata=data[s-lengthObsWindow:s,:]
        obsData=np.insert(obsData,iobs,subdata,axis=0)
        iobs+=1
        
        print("\nAt sample: {}\n".format(s-1))
        print(subdata)
        
    return obsData # 3D arrays (obs, sample, metric)
        
def slidingMultObsWindow(data,allLengthsObsWindow,slidingValue):
    iobs=0
    nSamples,nMetrics=data.shape
    obsDataList=[]
    for i in range(len(allLengthsObsWindow)):
        obsData=np.zeros((0,allLengthsObsWindow[i],nMetrics))
        obsDataList.append(obsData)
    
    for s in np.arange(max(allLengthsObsWindow),nSamples,slidingValue):
            for i in range(len(allLengthsObsWindow)):
                oW=allLengthsObsWindow[i]
                subdata=data[s-oW:s,:]
                obsDataList[i]=np.insert(obsDataList[i],iobs,subdata,axis=0)
                
                print("\nAt sample: {}\nObservation window size: {}\nSliding value: {}".format(s-1,oW,slidingValue))
                print(subdata)
                
            iobs+=1
    
    return obsDataList  # List of 3D arrays (obs, sample, metric)

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
    
    lengthObsWindow=10
    print("\n\n### SEQUENTIAL Observation Windows with Length {} ###".format(lengthObsWindow))
    obsData=seqObsWindow(data,lengthObsWindow)
    print(obsData)
    
    lengthObsWindow=10
    slidingValue=3
    print("\n\n### SLIDING Observation Windows with Length {} and Sliding {} ###".format(lengthObsWindow,slidingValue))
    obsData=slidingObsWindow(data,lengthObsWindow,slidingValue)
    print(obsData)
    
    allLengthsObsWindow=[5,10]
    slidingValue=3
    print("\n\n### SLIDING Observation Windows with Lengths {} and Sliding {} ###".format(allLengthsObsWindow,slidingValue))    
    obsData=slidingMultObsWindow(data,allLengthsObsWindow,slidingValue)
    print(obsData)
            
        

if __name__ == '__main__':
    main()
