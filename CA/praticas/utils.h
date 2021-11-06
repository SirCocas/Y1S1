//
// Created by sofas on 27/10/2021.
//

#ifndef PRATICAS_UTILS_H
#define PRATICAS_UTILS_H
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


bool isIgnorable(unsigned char c);

std::string plainText(std::string fileName);

std::string cipherText(std::string plaintext, std::string key);


std::string decipherText(std::string ciphered, std::string key);

void countFrequentLetters(std::string s, int frequencies[26]);


void frequentNgrams(std::string s, int length, std::map<std::string, std::string> &ngrams);

void printMap (std::map <std::string, std::string> &map);

std::string mostFrequentNGram(std::map <std::string, int> &map);

std::string getKey (std::string pool, int len);

std::string readFile(std::string fileName);

void frequentDistances(std::map<std::string, int *> map, std::string text);

#endif //PRATICAS_UTILS_H
