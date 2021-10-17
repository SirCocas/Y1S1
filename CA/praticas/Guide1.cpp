#include <iostream>
#include <string>
#include <fstream>
#include <iosfwd>
#include <sstream>

#include <cctype>
#include <algorithm>
#include <regex>

/*
NOTE: .txt files are in cmake-build-debug directory
 file names: telltale.txt (ENG)
             lusiadas.txt (PT)
 */

bool isIgnorable(unsigned char c) {
// simplification, as it eliminates characters it shouldn't (ç, à, etc)
    return (c == ' ' || c == '\n' || c == '\r' ||
            c == '\t' || c == '\v' || c == '\f' ||
            c== '.' || c==','|| c=='!'|| c==';'|| c=='?'
            || c== ':'|| std::isdigit(c) || c=='\'' ||
            ! std::isalpha(c));
}

std::string plainText(std::string fileName){
// not the most careful implementation, check isIgnorable for more info
// LATER (added complications that have 0 to do with criptography
    std::stringstream str;
    std::ifstream stream(fileName);
    if(stream.is_open())
    {
        while(stream.peek() != EOF)
        {
            str << (char) stream.get();
        }
        stream.close();
        std::string stringToRet = str.str();
        stringToRet.erase(std::remove_if(stringToRet.begin(), stringToRet.end(), isIgnorable), stringToRet.end());
        std::transform(stringToRet.begin(), stringToRet.end(), stringToRet.begin(),
                       [](unsigned char c){ return std::toupper(c); });
        return stringToRet;
    }
    return "";
}
std::string cipherText(std::string plaintext, std::string key){
    std::string ciphered ="";
    int keyIndex = 0;
    for (char cc : plaintext) {

        ciphered += ((cc+key[keyIndex]) % 26 )+ 'A';
        keyIndex ++;
        if(key[keyIndex] == '\0')
            keyIndex=0;
    }
    return ciphered;
}

std::string decipherText(std::string ciphered, std::string key){
    std::string deciphered = "";
    int keyIndex = 0;
    for (char cc : ciphered) {
        char toPut = ((cc-key[keyIndex]) % 26 )+ 'A';
        while (toPut < 'A')
            toPut+=26;
        deciphered += toPut;
        keyIndex ++;
        if(key[keyIndex] == '\0')
            keyIndex=0;
    }
    return deciphered;
}


void countFrequentLetters(std::string s, int frequencies[26]) {

    for (int i = 0; i < 26; ++i) {
        frequencies[i] = 0;
    }
    for (char ch: s) {
        frequencies[ch % 26]++;
    }
}

void frequentNgrams(std::string s, int length, std::map<std::string, int> &ngrams){
    //there is a problem here somewhere
    for (int startIndex = 0; startIndex < s.length(); ++startIndex) {
        std::string sub = s.substr(startIndex,length);
            if(sub.length()==length){
            int count = 0;
            for (size_t offset = s.find(sub); offset != std::string::npos;
                 offset = s.find(sub, offset + sub.length()))
                {
                    ++count;
                }
            ngrams[sub]=count;
        }

    }
}

void printMap (std::map <std::string, int> &map){
    int count = 0;
    for (auto const& x : map)
    {
        std::cout << x.first  // string (key)
                  << ':'
                  << x.second // string's value
                  << std::endl;
    }

}

std::string mostFrequentNGram(std::map <std::string, int> &map){
    std::string currentMax;
    int currentTop = -1;
    for (auto const& x : map)
    {
        if (x.second > currentTop){
            currentMax = x.first;
            currentTop=x.second;
        }

    }
    return currentMax;
}

std::string getKey (std::string pool, int len){
    std::string key = "";
    while(key.length()!= len){
        key+= pool[rand() % pool.length()];
    }
    return key;
}

int main() {
    std::string masterKey = "QWERTYUIOPASDFGHJKLZXCVBNM"; //every letter of the alphabet
    //Getting plain text from file
    std::string plaintext = plainText("telltale.txt");
    double maximumNGram = 0.010;
    double maxCoincidence = 0.010;
    int sizeOfNgram = 10;
    //get most frequent ngrams here, iterate possible keys to get a good length -> both in terms of ngrams % and max index of coincidence
    for (int keylen = 1; keylen < plaintext.length() ; ++keylen) {
        std::string key = getKey(masterKey, keylen);
        std::cout << key ;
        //int sizeOfNgram = keylen%10;
        //ciphering plaintext
        std::string ciphered = cipherText(plaintext, key);

        /*
        //deciphering ciphered text
        std::string deciphered = decipherText(ciphered, key);

        //checking if plain and ciphered texts are the same (if everything goes well, they should match)
        if(deciphered.compare(plaintext)!=0){
            std::cout << "deciphered and plain text are different" << std::endl;
            std::cout << deciphered << std::endl;
        }
        */

        //counting letter frequency
        int arr [26];
        countFrequentLetters(ciphered, arr);
        int worstICAppearances = *std::max_element(arr, arr + 26);
        double worstIC =  ((worstICAppearances+0.0)/(ciphered.length()+0.0))*((0.0+worstICAppearances-1)/(ciphered.length()-1));

        //getting NGrams frequency (N is an argument)
        std::map<std::string, int> ngrams;
        frequentNgrams(ciphered, sizeOfNgram, ngrams);

        /*
        // printing frequent NGrams
        printMap(ngrams);
        */

        //getting the most frequent Ngram
        std::string word = mostFrequentNGram(ngrams);
        double worstNgram = (ngrams[word]+0.0)/((ciphered.length()/word.length())+0.0);
        /*
        //printing most frequent NGram and its frequency
        std::cout<< word <<std::endl;
        std::cout << ngrams[word] << std::endl;
         */
        if(worstNgram<= maximumNGram && worstIC <= maxCoincidence){
            std::cout << " was a good key" <<std::endl;
            std::cout << word << std::endl;
            //printf("%d\n",worstNgram);
            //std::cout << ciphered <<std::endl;
            std::cout << "................" << std::endl;
        }
        else
            std::cout << " was a bad key" <<std::endl;

    }


    /*
    Print frequent letters count
     for (int i = 0; i < 26; ++i) {
        std::cout << arr[i] << std::endl;
    }

    */


    /*
     TODO
     generate key length -> se incidência de n-gram mais frequente for < x%, we gucci,
     tornar isto num for para parar no primeiro que tiver key length aceitável
     sendo que o x% pode até ser roubado do ngrama mais comum do plaintext
     */
    return 0;
}
