//
// Created by sofas on 27/10/2021.
//


#include <iostream>
#include <string>
#include <fstream>
#include <iosfwd>
#include <sstream>

#include <cctype>
#include <algorithm>
#include <regex>
#include "utils.h"


bool isIgnorable(unsigned char c) {
// simplification, as it eliminates characters it shouldn't (ç, à, etc)
    return (c == ' ' || c == '\n' || c == '\r' ||
            c == '\t' || c == '\v' || c == '\f' ||
            c== '.' || c==','|| c=='!'|| c==';'|| c=='?'
            || c== ':'|| std::isdigit(c) || c=='\'' ||
            ! std::isalpha(c));
}

std::string readFile(std::string fileName){
    std::stringstream str;
    std::ifstream stream(fileName);
    if (stream.is_open()){
        while(stream.peek() != EOF){
            str << (char) stream.get();
        }
        stream.close();
        return str.str();
    }
    return "";
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
                       [](unsigned char c){ return std::tolower(c); });
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

void splitIntoInt(std::string string, char separator, int* array){
    std::istringstream ss(string);

    std::string word; // for storing each word

    int counter = 0;
    while (ss >> word)
    {
        // print the read word
        array[counter] = std::stoi(word);
        counter++;
    }
}

void frequentDistances(std::map<std::string, int *> map, std::string text){
    std::map<std::string, std::string> frequent;
    frequentNgrams(text,3, frequent);

    for (auto const& x : frequent)
    {
        int* splitted;
        splitIntoInt(x.second, ' ', splitted);
        map[x.first] = splitted;
    }

}



void frequentNgrams(std::string s, int length, std::map<std::string, std::string> &ngrams){
    for (int startIndex = 0; startIndex < s.length(); startIndex+=length) {
        std::string sub = s.substr(startIndex,length);
        if(sub.length()==length){
            std::string count = "";
            int prev_offset = 0;
            for (size_t offset = s.find(sub); offset != std::string::npos; offset = s.find(sub, offset + sub.length()))
            {
                count+= " "+ std::to_string(offset - prev_offset);
                prev_offset = offset;
            }
            ngrams[sub]=count;
        }

    }
}

void printMap (std::map <std::string, std::string> &map){
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
