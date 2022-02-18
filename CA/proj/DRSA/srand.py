import sys
import hashlib
from sympy import *



def good_prime_factors(n, value):
        i = 2
        
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                if i<value:
                    return False

        return True

class generator:
    def shuffle_using_seed(self):
        new_state = []


        for i in range(len(self.state)):
            new_state.append(self.state[self.seed[-i%len(self.seed)]%len(self.state)])
        

        return bytes(new_state)

    def shuffle_using_self(self):

        new_state = []

        for i in range(len(self.state)):
            new_state.append(self.state[self.state[-i]%len(self.state)])
        return bytes(new_state)

    
    def sum_with_seed(self):
        #return bytes([(elem + i)%256 for elem in self.state for i in self.seed])
        
        new_state = []


        for i in range(len(self.state)):
            new_state.append((self.state[i] + self.seed[-i%len(self.seed)])%256)
        return(bytes(new_state))
        

    def subtraction_with_seed(self):
        #return bytes([(elem - i)%256 for elem in self.state for i in self.seed])
        
        new_state = []


        for i in range(len(self.state)):
            new_state.append((self.state[i] - self.seed[-i%len(self.seed)])%256)
        return(bytes(new_state))
        

    def sum_with_self(self):

        #return bytes([(elem + i)%256 for i in self.state for elem in self.state])
        
        new_state = []


        for i in range(len(self.state)):
            new_state.append((self.state[i] + self.state[-i])%256)
        return(bytes(new_state))
        

    def subtraction_with_self(self):
        #return bytes([(elem - i)%256 for elem in self.state for i in self.state])
        
        new_state = []


        for i in range(len(self.state)):
            new_state.append((self.state[i] - self.state[-i])%256)
        return(bytes(new_state))
        

    def xor_with_seed(self):
        #return bytes([(int(elem)^int(other_elem))%256 for elem in self.state for other_elem in self.state])
        
        new_state = []

        for i in range(len(self.state)):
            new_state.append(int(self.state[i]) ^ int(self.seed[-i%len(self.seed)]) )
        return bytes(new_state)
        

    def multiply_with_seed(self):
        #return bytes([ (elem * seed)%256 for elem in self.state for seed in self.seed])
        new_state = []
        for i in range(len(self.state)):
            new_state.append((self.state[i]*self.seed[i%len(self.seed)])%256)
        return bytes(new_state)

    def multiply_with_self(self):
        #return bytes([ (elem * seed)%256 for elem in self.state for seed in self.seed])
        new_state = []
        for i in range(len(self.state)):
            new_state.append((self.state[i]*self.seed[-i%len(self.seed)])%256)
        return bytes(new_state)
        
    def add_with_seed_string_enc(self):
        new_state = []
        for i in range(len(self.state)):
            position = self.positions.pop(0)
            self.positions.append(position)
            enc = self.ENCODINGS.pop(position%len(self.ENCODINGS))
            self.ENCODINGS.append(enc)          
            new_state.append((self.state[i]+ sum(bytes(str(self.seed[i%len(self.seed)]), enc)))%256)


        return bytes(new_state)
    
    def add_with_self_string_enc(self):
        new_state = []
        for i in range(len(self.state)):
            position = self.positions.pop(0)
            self.positions.append(position)
            enc = self.ENCODINGS.pop(position%len(self.ENCODINGS))
            self.ENCODINGS.append(enc)          
            new_state.append((self.state[i]+ sum(bytes(str(self.state[-i]), enc)))%256)

        return bytes(new_state)

    def shuffle_using_positions(self):

        new_state = list(self.state)
        for i in range(0, len(new_state)):
            new_state[i], new_state[self.positions[i%len(self.positions)]] = new_state[self.positions[i%len(self.positions)]], new_state[i]
        return bytes(new_state)

    def hash_self(self):
        new_state = ""
        for i in self.state:
            try:
                position = self.positions.pop(0)
                self.positions.append(position)
                enc = self.ENCODINGS.pop(position%len(self.ENCODINGS))
                self.ENCODINGS.append(enc)    
                    
                new_state+=str((hashlib.md5(chr(i).encode(enc)).digest()))

            except: 
                new_state+=str((hashlib.md5(chr(i).encode('utf-8')).digest()))

        position = self.positions.pop(0)
        self.positions.append(position)
        enc = self.ENCODINGS.pop(position%len(self.ENCODINGS))
        self.ENCODINGS.append(enc)
        try: 
            return bytes(new_state, enc)
        except:
            return bytes(new_state, 'utf-8')
    
    def __init__(self, seed):

        self.ENCODINGS = ['ascii','big5','big5hkscs','cp037','cp273','cp424','cp437','cp500','cp720','cp737','cp775','cp850','cp852','cp855',
        'cp856','cp857','cp858','cp860','cp861','cp862','cp863','cp864','cp865','cp866','cp869','cp874','cp875','cp932','cp949','cp950',
        'cp1006','cp1026','cp1125','cp1140','cp1250','cp1251','cp1252','cp1253','cp1254','cp1255','cp1256','cp1257','cp1258','cp65001',
        'euc_jp','euc_jis_2004','euc_jisx0213','euc_kr','gb2312','gbk','gb18030','hz','iso2022_jp','iso2022_jp_1','iso2022_jp_2',
        'iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext','iso2022_kr','latin_1','iso8859_2','iso8859_3','iso8859_4','iso8859_5',
        'iso8859_6','iso8859_7','iso8859_8','iso8859_9','iso8859_10','iso8859_11','iso8859_13','iso8859_14','iso8859_15',
        'iso8859_16','johab','koi8_r','koi8_t','koi8_u','kz1048','mac_cyrillic','mac_greek','mac_iceland','mac_latin2',
        'mac_roman','mac_turkish','ptcp154','shift_jis','shift_jis_2004','shift_jisx0213', 'utf_7','utf_8']


        self.seed = seed
        self.state = seed

        self.positions = list(range(5))
        print(self.positions)

        self.shufflers = [self.shuffle_using_seed, self.shuffle_using_self, self.shuffle_using_positions]
        
        self.alterers = [self.sum_with_seed, self.subtraction_with_seed, self.sum_with_self, self.subtraction_with_self,
        self.xor_with_seed, self.multiply_with_seed,  self.multiply_with_self, self.add_with_seed_string_enc, 
        self.add_with_self_string_enc, self.hash_self]
    
    def get_random_arr(self):
        position = self.positions.pop(0)
        self.positions.append(position)
        shuffler = self.shufflers.pop(position%len(self.shufflers))
        self.shufflers.append(shuffler)
        self.state = shuffler()
        alterer = self.alterers.pop(position%len(self.alterers))
        self.alterers.append(alterer)
        self.state = alterer()

        return self.state
    
    def get_random_number(self):
        return sum(self.get_random_arr())




def find_pattern(place, pattern):
    #optimal case
    for i in range(len(place) - len(pattern)):
        if place[i:i+len(pattern)] == pattern:
            return True    
    return False
    

def create_seed(str1, str2, it, enc ):
    prev = [bytes(str1+str2, enc)]
    for i in range(it):   
        prev.append(hashlib.md5(prev[0]))
        prev.pop(0)  #to not make prev too beefy
        prev[0] = prev[0].digest()
    
    return prev[0]


class random_generator:
    def __init__(self, passwd, conf_string, it_count):

        self.ENCODINGS = ['ascii','big5','big5hkscs','cp037','cp273','cp424','cp437','cp500','cp720','cp737','cp775','cp850','cp852','cp855',
        'cp856','cp857','cp858','cp860','cp861','cp862','cp863','cp864','cp865','cp866','cp869','cp874','cp875','cp932','cp949','cp950',
        'cp1006','cp1026','cp1125','cp1140','cp1250','cp1251','cp1252','cp1253','cp1254','cp1255','cp1256','cp1257','cp1258','cp65001',
        'euc_jp','euc_jis_2004','euc_jisx0213','euc_kr','gb2312','gbk','gb18030','hz','iso2022_jp','iso2022_jp_1','iso2022_jp_2',
        'iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext','iso2022_kr','latin_1','iso8859_2','iso8859_3','iso8859_4','iso8859_5',
        'iso8859_6','iso8859_7','iso8859_8','iso8859_9','iso8859_10','iso8859_11','iso8859_13','iso8859_14','iso8859_15',
        'iso8859_16','johab','koi8_r','koi8_t','koi8_u','kz1048','mac_cyrillic','mac_greek','mac_iceland','mac_latin2',
        'mac_roman','mac_turkish','ptcp154','shift_jis','shift_jis_2004','shift_jisx0213', 'utf_7','utf_8']



        self.passwd = passwd
        self.confusion_string = conf_string
        self.iteration_count = it_count

        try:
            self.iteration_count = int(self.iteration_count)
        except:
            print("ITERATION_COUNT must be an integer!")
            sys.exit()
        if(self.iteration_count<1):
            print("ITERATION_COUNT should be bigger than 1!")
            sys.exit()

        # Compute a bootstrap seed from the password, the confusion string and the iteration count.
        # Consider, for instance, using the PBKDF2 method;

        enc = self.ENCODINGS.pop(0)
        self.ENCODINGS.append(enc)
        seed = create_seed(self.passwd, self.confusion_string, self.iteration_count, enc)


        # Transform the confusion string into an equal length sequence of bytes (confusion pattern). These
        # resulting bytes should be able to have any value;
        before = len(self.confusion_string)
        current_enc = self.ENCODINGS.pop(0)
        self.confusion_string = bytes(self.confusion_string, current_enc)
        self.ENCODINGS.append(current_enc)

        after = len(self.confusion_string)
        
        assert before == after, "Something went wrong during byte-ification of confusion string."

        # Initialize the generator with the bootstrap seed;


        # Use the generator to produce a pseudo-random stream of bytes, stopping when the confusion
        # pattern is found;

        for i in range(self.iteration_count):
            self.gen = generator(seed)
            stream = self.gen.get_random_arr()
            while(not find_pattern(stream, self.confusion_string)):
                new_stream = list(stream[len(stream)-len(seed):])
                for j in self.gen.get_random_arr():
                    new_stream.append(j)
                        
                stream = bytes(new_stream)
            enc = self.ENCODINGS.pop(0)
            self.ENCODINGS.append(enc)
            try:
                seed = create_seed(str(stream, enc),"", self.iteration_count-i,enc )
            except:
                seed = stream

    def get_random_bytes(self):
        return self.gen.get_random_arr()    


    
