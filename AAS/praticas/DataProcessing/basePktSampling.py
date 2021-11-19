import sys
import argparse
import datetime
from netaddr import IPNetwork, IPAddress, IPSet
import pyshark

def pktHandler(timestamp,srcIP,dstIP,lengthIP,sampDelta=1):
    global scnets
    global ssnets
    global npkts
    global T0
    global outc
    global last_ks
    
    if (IPAddress(srcIP) in scnets and IPAddress(dstIP) in ssnets) or (IPAddress(srcIP) in ssnets and IPAddress(dstIP) in scnets):
        if npkts==0:
            T0=float(timestamp)
            last_ks=0
            
        ks=int((float(timestamp)-T0)/sampDelta)
        
        if ks>last_ks:
            print('{} {} {} {} {}'.format(last_ks,*outc))
            outc=[0,0,0,0]  
            
        if ks>last_ks+1:
            for j in range(last_ks+1,ks):
                print('{} {} {} {} {}'.format(j,*outc))
                  
        
        if IPAddress(srcIP) in scnets: #Upload
            outc[0]=outc[0]+1
            outc[1]=outc[1]+int(lengthIP)

        if IPAddress(dstIP) in scnets: #Download
            outc[2]=outc[2]+1
            outc[3]=outc[3]+int(lengthIP)
        
        last_ks=ks
        npkts=npkts+1


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='?',required=True, help='input file')
    parser.add_argument('-f', '--format', nargs='?',required=True, help='format',default=1)
    parser.add_argument('-c', '--cnet', nargs='+',required=True, help='client network(s)')
    parser.add_argument('-s', '--snet', nargs='+',required=True, help='service network(s)')
    
    args=parser.parse_args()
    
    cnets=[]
    for n in args.cnet:
        try:
            nn=IPNetwork(n)
            cnets.append(nn)
        except:
            print('{} is not a network prefix'.format(n))
    #print(cnets)
    if len(cnets)==0:
        print("No valid client network prefixes.")
        sys.exit()
    global scnets
    scnets=IPSet(cnets)

    snets=[]
    for n in args.snet:
        try:
            nn=IPNetwork(n)
            snets.append(nn)
        except:
            print('{} is not a network prefix'.format(n))
    #print(snets)
    if len(snets)==0:
        print("No valid service network prefixes.")
        sys.exit()
        
    global ssnets
    ssnets=IPSet(snets)
        
    fileInput=args.input
    fileFormat=int(args.format)
        
    global npkts
    global T0
    global outc
    global last_ks

    npkts=0
    outc=[0,0,0,0]
    sampDelta=1
    #print('Sampling interval: {} second'.format(sampDelta))

    if fileFormat in [1,2]:
        file = open(fileInput,'r') 
        for line in file: 
            pktData=line.split()
            if fileFormat==1 and len(pktData)==9: #script format
                timestamp,srcIP,dstIP,lengthIP=pktData[0],pktData[4],pktData[6],pktData[8]
                pktHandler(timestamp,srcIP,dstIP,lengthIP,sampDelta)
            elif fileFormat==2 and len(pktData)==4: #tshark format "-T fileds -e frame.time_relative -e ip.src -e ip.dst -e ip.len"
                timestamp,srcIP,dstIP,lengthIP=pktData[0],pktData[1],pktData[2],pktData[3]
                pktHandler(timestamp,srcIP,dstIP,lengthIP,sampDelta)
        file.close()
    elif fileFormat==3: #pcap format
        capture = pyshark.FileCapture(fileInput)
        for pkt in capture:
            try:
                timestamp,srcIP,dstIP,lengthIP=pkt.sniff_timestamp,pkt.ip.src,pkt.ip.dst,pkt.ip.len
                pktHandler(timestamp,srcIP,dstIP,lengthIP,sampDelta)
            except:
                pass
        capture.close()
    


if __name__ == '__main__':
    main()
