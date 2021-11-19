from Crypto.Cipher import AES
import math
import ctypes
import random

c_saes = ctypes.CDLL("./saes_c.so")
#TODO: 
#   criar decipher first, decipher normal, decipher special e decipher last

def prepareKeys(key, sk = None, side = 4):
    # by default, side =  16 
    idx = 0
    toRetKey = []
    toRetSKey = [] if sk!= None else None
    try:
        while(len(toRetKey)< side*side):
            toRetKey.append(int(key[idx:idx+2],16))
            if(toRetSKey!=None):
                toRetSKey.append(int(sk[idx:idx+2],16))
            idx+=2
            
        return (toRetKey, toRetSKey)
    except:
        print("key is not a readable number")
        exit()


def xor(x,y):
    return [a^b for a,b in zip(x, y)]

def prepareInput(input, side = 4):
    # by default, side =  16 
    i = 0
    j = 0
    padding =  int(str(int((math.pow(side,2)*2 - len(input))/2)),16)
    while(len(input)< math.pow(side, 2)*2):
        input+=str(padding)
        # if the message isn't long enough, it will be padded by the distance (can't use 0s, as it would leave the key clear)
    idx=0
    toRetInp = []
    
    try:
        toRetInp.append([])
        while(i< side):
            toRetInp[i].append(int(input[idx:idx+2],16)) 
            
            idx+=2
            if(len(toRetInp[i]) == side):
                i +=1
                toRetInp.append([])
        return toRetInp[:-1]
    except:
        print("Input or key is not a readable number")
        return -1

def stringify(input):
    return [input[i][j] for i in range(0,4) for j in range (0,4)]

def squarify(input, Nb = 4):
    toRet = [[None for j in range(Nb)] for i in range(Nb)]
    i = 0
    j = 0
    for a in input:
        toRet[i][j]=a
        j+=1
        if(j==4):
            j=0
            i+=1
    return toRet

class saes:
    
    def invert(self, sbox):
        toRet = []
        while(len(toRet)!= len(sbox)):
            toRet.append(0);
        for idx, val in enumerate(sbox): 
            toRet[val] = idx
        return toRet

    def generates_box(self):
        box = [i for i in self.s_box]
        current = 0
        idx = 0
 
        for i in range(0, 256):
            current = self.sk[i%len(self.sk)]
            box[current], box[i] = box[i], box[current]


        return box

    def mixoffsets(self):
        self.offsets = [0,1,2,3]
        for i in self.offsets:
            current = self.sk[i]%4
            self.offsets[i], self.offsets[current] = self.offsets[current], self.offsets[i]
        return self.offsets

    def sub_word(self,word):
        return (self.s_box[b] for b in word)
    def rot_word(self, word):
        return word[1:] + word[:1]

    def expandKey(self):
        expanded = []
        expanded+= self.key
        for i in range(4, 4 * (10 + 1)):
            t = expanded[(i-1)*4:i*4]
            if i % 4 == 0:
                t = xor( self.sub_word( self.rot_word(t) ), (self.rcon[i // 4],0,0,0) )
            elif 4 > 6 and i % 4 == 4:
                t = self.sub_word(t)
            expanded.extend( xor(t, expanded[(i-4)*4:(i-4+1)*4]))

        return expanded

    def __init__(self, key, sk=None):
        #constants
        self.s_box = [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
                    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
                    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
                    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
                    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
                    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
                    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
                    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
                    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
                    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
                    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
                    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
                    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
                    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
                    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
                    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
                    ]
        
        self.rev_s_box = [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
            0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
            0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
            0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
            0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
            0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
            0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
            0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
            0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
            0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
            0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
            0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
            0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
            0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
            0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]
        self.rcon=Rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a]

        #not constants
        self.key, self.sk = prepareKeys(key,sk)
        self.key = self.expandKey()

        self.currentLoop = 0
        
        if (self.sk!= None):
            self.shuffled_s_box = self.generates_box()
            self.rev_shuffled_s_box = self.invert(self.shuffled_s_box)
            self.offsets = self.mixoffsets()

            sum = 0
            for i in self.sk:
                sum+=i
            self.special_round_time = sum%9 + 1 #value goes from 0 to 8, but we want it from 1 to 9 
        else:
            self.special_round_time = 10000

    def addRoundKey (self, txt):
        Nb = len(txt)
        new_state = [[None for j in range(Nb)] for i in range(Nb)]
        offset = self.sk[self.currentLoop]%16
        key = self.key[self.currentLoop*16:]
        idx = 0
        for i in range(Nb):
            for j in range(Nb):
                idx+=offset
                idx=idx%(len(key)+1)
                new_state[i][j] = txt[i][j] ^ key[idx]
                idx+=1


        return new_state

    def reg_addRoundKey (self, txt):
        Nb = len(txt)
        new_state = [[None for j in range(Nb)] for i in range(Nb)]
        key = self.key[self.currentLoop*16:]
        #print(key)
        idx = 0
        for i in range(Nb):
            for j in range(Nb):
                new_state[i][j] = txt[i][j] ^ key[idx]
                idx+=1

        return new_state
    
    def gmul(self, a,b):
        p = 0
        for c in range(8):
            if b & 1:
                p ^= a
            a <<= 1
            if a & 0x100:
                a ^= 0x11b
            b >>= 1
        return p

    def reg_subBytes(self, txt, Nb=4):
        new_state = [[None for j in range(Nb)] for i in range(Nb)]
        for i in range(Nb):
            for j in range(Nb):
                new_state[i][j] = self.s_box[txt[i][j]]
        return new_state

    def inv_reg_sub_bytes(self,txt,Nb=4):
        new_state = [[None for j in range(Nb)] for i in range(Nb)]
        for i in range(Nb):
            for j in range(Nb):
                new_state[i][j] = self.rev_s_box[txt[i][j]]
        return new_state

    def subBytes(self, txt, Nb=4):
        new_state = [[None for j in range(Nb)] for i in range(Nb)]
        for i in range(Nb):
            for j in range(Nb):
                new_state[i][j] = self.shuffled_s_box[txt[i][j]]
        return new_state

    def inv_sub_bytes(self,txt,Nb=4):
        new_state = [[None for j in range(Nb)] for i in range(Nb)]
        for i in range(Nb):
            for j in range(Nb):
                new_state[i][j] = self.rev_shuffled_s_box[txt[i][j]]
        return new_state


    def reg_shift_rows(self,txt, Nb=4):
        new_state=[]
        offsets =[i for i in range(0, Nb)]
        for r in range(4):
            currentoffset = offsets[r]
            new_state.append( txt[r] )
            new_state[r] = new_state[r][currentoffset:] + new_state[r][:currentoffset] 
        return new_state
    
    def inv_reg_shift_rows(self, txt, Nb=4):
        new_state=[]
        offsets =[i for i in range(0, Nb)]
        for r in range(4):
            currentoffset = 4 - offsets[r]
            new_state.append( txt[r] )
            new_state[r] = new_state[r][currentoffset:] + new_state[r][:currentoffset]
        return new_state

    def inv_shift_rows(self,txt, Nb=4):
        new_state=[]
        for r in range(4):
            currentoffset = 4 - self.offsets[r]
            new_state.append( txt[r] )
            new_state[r] = new_state[r][currentoffset:] + new_state[r][:currentoffset]
        return new_state


    def shift_rows(self,txt, Nb=4):
        new_state=[]
        for r in range(4):
            currentoffset = self.offsets[r]
            new_state.append( txt[r] )
            new_state[r] = new_state[r][currentoffset:] + new_state[r][:currentoffset] 
        return new_state

    def mix_columns(self,txt, Nb=4):
        new_state = [[None for j in range(Nb)] for i in range(Nb)]
        offset = self.sk[self.currentLoop]%Nb
        ss = []
        for i in range(0,Nb):
            col = [txt[k][(i+offset)%Nb] for k in range(0,Nb)]

            ss=[
                        self.gmul(0x02,col[0]) ^ self.gmul(0x03,col[1]) ^                col[2]  ^                col[3] ,
                                       col[0]  ^ self.gmul(0x02,col[1]) ^ self.gmul(0x03,col[2]) ^                col[3] ,
                                       col[0]  ^                col[1]  ^ self.gmul(0x02,col[2]) ^ self.gmul(0x03,col[3]),
                        self.gmul(0x03,col[0]) ^                col[1]  ^                col[2]  ^ self.gmul(0x02,col[3]),
                    ]
            for k in range(0,Nb):
                new_state[k][i] = ss[k]

        return new_state
    
    def reg_mix_columns(self,txt, Nb=4):
        new_state = [[None for j in range(Nb)] for i in range(Nb)]
        ss = []
        for i in range(0,Nb):
            col = [txt[k][i%Nb] for k in range(0,Nb)]

            ss=[
                        self.gmul(0x02,col[0]) ^ self.gmul(0x03,col[1]) ^                col[2]  ^                col[3] ,
                                       col[0]  ^ self.gmul(0x02,col[1]) ^ self.gmul(0x03,col[2]) ^                col[3] ,
                                       col[0]  ^                col[1]  ^ self.gmul(0x02,col[2]) ^ self.gmul(0x03,col[3]),
                        self.gmul(0x03,col[0]) ^                col[1]  ^                col[2]  ^ self.gmul(0x02,col[3]),
                    ]
            for k in range(0,Nb):
                new_state[k][i] = ss[k]

        return new_state
    
    def inv_reg_mix_columns(self, txt, Nb=4):
        new_state = [[None for j in range(Nb)] for i in range(Nb)]
        ss = []
        for i in range(0,Nb):
            col = [txt[k][i%Nb] for k in range(0,Nb)]

            ss=[
                        self.gmul(0x0e,col[0]) ^ self.gmul(0x0b,col[1]) ^ self.gmul(0x0d,col[2]) ^ self.gmul(0x09,col[3]),
                        self.gmul(0x09,col[0]) ^ self.gmul(0x0e,col[1]) ^ self.gmul(0x0b,col[2]) ^ self.gmul(0x0d,col[3]),
                        self.gmul(0x0d,col[0]) ^ self.gmul(0x09,col[1]) ^ self.gmul(0x0e,col[2]) ^ self.gmul(0x0b,col[3]),
                        self.gmul(0x0b,col[0]) ^ self.gmul(0x0d,col[1]) ^ self.gmul(0x09,col[2]) ^ self.gmul(0x0e,col[3])
                    ]
            for k in range(0,Nb):
                new_state[k][i] = ss[k]

        return new_state

    def inv_mix_columns(self,txt, Nb=4):
        new_state = [[None for j in range(Nb)] for i in range(Nb)]
        offset = self.sk[self.currentLoop]%Nb
        ss = []
        for i in range(0,Nb):
            col = [txt[k][(i+offset)%Nb] for k in range(0,Nb)]

            ss=[
                        self.gmul(0x0e,col[0]) ^ self.gmul(0x0b,col[1]) ^ self.gmul(0x0d,col[2]) ^ self.gmul(0x09,col[3]),
                        self.gmul(0x09,col[0]) ^ self.gmul(0x0e,col[1]) ^ self.gmul(0x0b,col[2]) ^ self.gmul(0x0d,col[3]),
                        self.gmul(0x0d,col[0]) ^ self.gmul(0x09,col[1]) ^ self.gmul(0x0e,col[2]) ^ self.gmul(0x0b,col[3]),
                        self.gmul(0x0b,col[0]) ^ self.gmul(0x0d,col[1]) ^ self.gmul(0x09,col[2]) ^ self.gmul(0x0e,col[3])
                    ]
            for k in range(0,Nb):
                new_state[k][i] = ss[k]

        return new_state

    def cipher_round_special(self):
        tmp = self.addRoundKey(self.mix_columns(self.shift_rows(self.subBytes(self.input))))
        return tmp
    
    
    def cipher_round(self):
        return self.reg_addRoundKey(self.reg_mix_columns(self.reg_shift_rows(self.reg_subBytes(self.input))))

    def cipher_last_round(self):
        self.currentLoop = 10
        return stringify(self.reg_addRoundKey(self.reg_shift_rows(self.reg_subBytes(self.input))))
        

    def cipher_first_round(self, Nb = 4):
        self.currentLoop = 0
        return self.reg_addRoundKey(self.input)

    def cipher(self, input):
        result = []
        while input!= []:
            #creating several blocks if the input is too big
            if(len(input)>32):
                tmp = input[0:32]
                input = input[32:]

            else:
                tmp=input
                input=[]

            self.input = prepareInput(tmp)
            

            self.input = self.cipher_first_round()
            for i in range(1,10):
                self.currentLoop = i
                if(i==self.special_round_time):
                    self.input = self.cipher_round_special()
                else:
                    self.input = self.cipher_round()

            result += self.cipher_last_round()
        
        return ''.join("%02x"%my_int for my_int in result)


    def decipher_first_round(self):
        self.currentLoop = 10
        return self.reg_addRoundKey(self.input)

    def decipher_round(self):
        #this is wrong!!!
        return self.inv_reg_mix_columns(self.reg_addRoundKey(self.inv_reg_sub_bytes(self.inv_reg_shift_rows(self.input))))

    def decipher_special(self):
        #this is wrong!!!
        """
        AddRoundKey(InvMixColumns(InvSubBytes(InvShiftRows(x)))
        """
        return self.inv_mix_columns(self.addRoundKey(self.inv_sub_bytes(self.inv_shift_rows(self.input))))

    def decipher_last_round(self):
        self.currentLoop = 0
        return stringify(self.reg_addRoundKey(self.inv_reg_sub_bytes(self.inv_reg_shift_rows(self.input))))


    def decipher(self, input):
        result = []
        while input!= []:
            #creating several blocks if the input is too big
            if(len(input)>32):
                tmp = input[0:32]
                input = input[32:]

            else:
                tmp=input
                input=[]

            self.input = prepareInput(tmp)

            self.input = self.decipher_first_round()
            for i in range(9,0,-1):
                self.currentLoop = i
                if(i == self.special_round_time):
                    self.input = self.decipher_special()
                else:
                    self.input = self.decipher_round()
            result+=self.decipher_last_round()
        return ''.join("%02x"%my_int for my_int in result)
            
    
    




s = saes("1b1113973213927309213283182381231321238329237983721", "A234213AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

print(prepareInput("123123213211331231123"))

tmp = s.reg_addRoundKey(prepareInput("123123213211331231123"))

print(s.reg_addRoundKey(tmp))



