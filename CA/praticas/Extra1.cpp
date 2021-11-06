//
// Created by sofas on 27/10/2021.
//

# include "utils.h"

int main(){
    std::string masterKey="qwertyuiopasdfghjklzxcvbnm";
    std::string file = readFile("1.txt");
    //std::cout << file << std::endl;
    std::map<std::string, int*> frequentNGrams;
    frequentDistances(frequentNGrams, file);
    std::cout<<frequentNGrams["tme"][0]<<std::endl;

}