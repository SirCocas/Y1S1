import sys
import hashlib

def create_seed(str1, str2, it, enc ):
    prev = [bytes(str1+str2, enc)]
    for i in range(it):   
        prev.append(hashlib.md5(prev[0]))
        prev.pop(0)  #to not make prev too beefy
        prev[0] = prev[0].digest()
    return prev[0]


ENCODINGS = ['ascii','big5','big5hkscs','cp037','cp273','cp424','cp437','cp500','cp720','cp737','cp775','cp850','cp852','cp855',
 'cp856','cp857','cp858','cp860','cp861','cp862','cp863','cp864','cp865','cp866','cp869','cp874','cp875','cp932','cp949','cp950',
 'cp1006','cp1026','cp1125','cp1140','cp1250','cp1251','cp1252','cp1253','cp1254','cp1255','cp1256','cp1257','cp1258','cp65001',
 'euc_jp','euc_jis_2004','euc_jisx0213','euc_kr','gb2312','gbk','gb18030','hz','iso2022_jp','iso2022_jp_1','iso2022_jp_2',
 'iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext','iso2022_kr','latin_1','iso8859_2','iso8859_3','iso8859_4','iso8859_5',
 'iso8859_6','iso8859_7','iso8859_8','iso8859_9','iso8859_10','iso8859_11','iso8859_13','iso8859_14','iso8859_15',
 'iso8859_16','johab','koi8_r','koi8_t','koi8_u','kz1048','mac_cyrillic','mac_greek','mac_iceland','mac_latin2',
 'mac_roman','mac_turkish','ptcp154','shift_jis','shift_jis_2004','shift_jisx0213', 'utf_7','utf_8']

CURRENT_ENCODING = 0



if(len(sys.argv)!=4):
    print("WRONGFUL USAGE: python3 srand.py PASSWORD CONFUSION_STRING ITERATION_COUNT")
    sys.exit()

passwd = sys.argv[1]
confusion_string = sys.argv[2]
iteration_count = sys.argv[3]

try:
    iteration_count = int(iteration_count)
except:
    print("ITERATION_COUNT must be an integer!")
    sys.exit()
if(iteration_count<1):
    print("ITERATION_COUNT should be bigger than 1!")
    sys.exit()

# Compute a bootstrap seed from the password, the confusion string and the iteration count.
# Consider, for instance, using the PBKDF2 method;

enc = ENCODINGS.pop(0)
ENCODINGS.append(enc)
seed = create_seed(passwd, confusion_string, iteration_count, enc)


# Transform the confusion string into an equal length sequence of bytes (confusion pattern). These
# resulting bytes should be able to have any value;
before = len(confusion_string)
current_enc = ENCODINGS.pop(0)
confusion_string = bytes(confusion_string, current_enc)
ENCODINGS.append(current_enc)

after = len(confusion_string)

assert before == after, "Something went wrong during byte-ification of confusion string."

# Initialize the generator with the bootstrap seed;



# Use the generator to produce a pseudo-random stream of bytes, stopping when the confusion
# pattern is found;



# Use the generator to produce a new seed and use that seed to re-initialize the generator; 



# Repeat the last two steps as many times as the number of iterations defined by the user.




