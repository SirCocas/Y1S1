#include <iostream>
#include <string>
#include <fstream>
#include <iosfwd>
#include <sstream>

#include <cctype>
#include <algorithm>
#include <regex>

#include "utils.h"




int main() {
    std::string masterKey = "QWERTYUIOPASDFGHJKLZXCVBNM"; //every letter of the alphabet
    //Getting plain text from file
    std::string plaintext = plainText("1.txt");
    //double maximumNGram = 0.10;
    //double maxCoincidence = 0.010;
    //int sizeOfNgram = 10;
    //get most frequent ngrams here, iterate possible keys to get a good length -> both in terms of ngrams % and max index of coincidence
    //for (int keylen = 1; keylen < plaintext.length() ; ++keylen) {
        //std::string key = getKey(masterKey, keylen);
        //std::cout << key ;
        //int sizeOfNgram = keylen%10;
        //ciphering plaintext
        std::string ciphered = plaintext;

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
        //int worstICAppearances = *std::max_element(arr, arr + 26);
        //double worstIC =  ((worstICAppearances+0.0)/(ciphered.length()+0.0))*((0.0+worstICAppearances-1)/(ciphered.length()-1));

        //getting NGrams frequency (N is an argument)
        std::map<std::string, std::string> ngrams;
        frequentNgrams(ciphered, 3, ngrams);

        ///*/*
        // printing frequent NGrams
        printMap(ngrams);
        //*/

        //getting the most frequent Ngram
        //std::string word = mostFrequentNGram(ngrams);

        //double worstNgram = (ngrams[word]+0.0)/((ciphered.length()/word.length())+0.0);
        /*
        //printing most frequent NGram and its frequency
        std::cout<< word <<std::endl;
        std::cout << ngrams[word] << std::endl;
         */
        //if(worstNgram<= maximumNGram && worstIC <= maxCoincidence){
            //std::cout << " was a good key" <<std::endl;
            //std::cout << word << std::endl;
            //printf("%d\n",worstNgram);
            //std::cout << ciphered <<std::endl;
            //std::cout << "................" << std::endl;
        //}
        //else
           // std::cout << " was a bad key" <<std::endl;

    //}

    /*
    Print frequent letters count
     for (int i = 0; i < 26; ++i) {
        std::cout << arr[i] << std::endl;
    }

    */

    return 0;
}
