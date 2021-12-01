#include <stdint.h>     //for int8_t
#include <string.h>     //for memcmp
#include <wmmintrin.h>  //for intrinsics for AES-NI
//compile using gcc and following arguments: -g;-O0;-Wall;-msse2;-msse;-march=native;-maes
__m128i aes_cypher(__m128i text, __m128i key){

    return _mm_aesenc_si128(text, key);
}

__m128i aes_lastcypher(__m128i text, __m128i key){
    return _mm_aesenclast_si128(text, key);
}

int* generate_dec_key(int* in_key){
    __m128i key [10] = {0,0,0,0,0,0,0,0,0,0};
    for (int i = 9; i != -1; i--)
    {
        __m128i tmp = _mm_load_si128(in_key[i]);
        key[i] = _mm_aesimc_si128(tmp);
    }
    return key;
    
}

__m128i aes_decypher(__m128i text, __m128i key){
    return _mm_aesdec_si128(text, key);
}

__m128i aes_lastdecypher(__m128i text, __m128i key){
    return _mm_aesdeclast_si128(text, key);
}

int main(void){
    return 1;
}
