from srand import *

import time
import matplotlib.pyplot as plt

class times:
    def __init__(self, passwd,conf, iter_count, time):
        self.passwd = passwd
        self.conf = conf
        self.iter_count = iter_count
        self.time = time
    
    def __str__(self):
        return("TIME: "+str(self.time)+ "seconds; passwd: "+str(self.passwd)+"; iter count "+str(self.iter_count)+"; conf string: "+str(self.conf))



def get_graphs(values):
    
    values.sort(key=lambda x: x.time)
    time = [i.time for i in values]
    passwd_len = [i.passwd for i in values]
    conf = [i.conf for i in values]
    iter_count = [i.iter_count for i in values]

    x = time
    y1 = passwd_len
    y2 = conf
    y3 = iter_count
    plt.plot(x,y1,'-', label = "Password length")
    plt.plot(x,y2,'-',label="Confusion string length")
    plt.plot(x,y3,'-',label="Iteration count")
    plt.xlabel('Time taken to generate (s)')
    plt.grid(axis='y', linestyle='-') 
    plt.grid(axis='x', linestyle='-') 
    plt.yticks(range(0, 1+max([max(y1), max(y2), max(y3)])))
    
    plt.legend()
    plt.show()
    
    plt.savefig('graphs.png', dpi=100)

    plt.clf()




def write_to_file(tests):
    try:
        report = open(sys.argv[2], 'w')
        report.close()
        report = open(sys.argv[2], "w")
    except:
        report = open(sys.argv[2], "x")
        report.close()
        report = open(sys.argv[2], 'w')
    tests.sort(key=lambda x: x.time)
    longest_time = tests[-1]
    shortest_time = tests[0]
    text = "SHORTEST TIME: \n\t"+str(shortest_time)+"\nLONGEST TIME:\n\t"+str(longest_time)+"\n"
    for i in tests:
        text+="******************"
        text+= "\nPassword length: "+ str(i.passwd)
        text+="\nConfusion string length: "+ str(i.conf)
        text+="\nIteration count used: \n\t"+str(i.iter_count)+"\n"
        text+="\nTime spent generating: "+ str(i.time)+"seconds,\n"
    report.write(text)
    report.close()

if(len(sys.argv)<2):
    print("WRONGFUL USAGE:")
    print("OPTIONS:")
    print("\tpython3 randgen.py speed REPORT_FILE")
    print("\tpython3 randgen.py PASSWORD CONFUSION_STRING ITERATION_COUNT")
    sys.exit()

if(sys.argv[1] == 'speed' and len(sys.argv)==3):

    for_file = ""
    tests = []
    conf_string = ''
    passwd = ''
    try:
        #1 -> 10
        for conf_string_len in range(1,3):
            conf_string += 'a'
            for passwd_len in range(1,3):
                passwd += 'b'
                for it_count in range(1,10):
                    
                    start = time.time()
                    tmp = random_generator(passwd,conf_string,it_count)
                    end = time.time()
                    tests.append(times(passwd_len,conf_string_len,it_count,end-start))
                    
                    write_to_file(tests)

        
        
        write_to_file(tests)
        get_graphs(tests)
    except:
        write_to_file(tests)
        get_graphs(tests)

else:
    try:
        gen = random_generator(sys.argv[1],sys.argv[2], sys.argv[3])
        while(1):
            tmp = gen.get_random_bytes()
            toBuild = ""
            for i in tmp:
                try:
                    toBuild+=chr(i)
                except:
                    pass
            if(toBuild):
                print(toBuild, flush=True)
    except:
        print("WRONGFUL USAGE FOR random MODE OF OPERATION: python3 randgen.py PASSWORD CONFUSION_STRING ITERATION_COUNT")
