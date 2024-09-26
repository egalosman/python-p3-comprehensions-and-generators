#!/usr/bin/env python3

def return_evens(num_list):
    
    even_list = [x for x in num_list if x % 2 == 0]
    return even_list

def make_exclamation(sentence_list):
    if len(sentence_list) == 0:
        return [] 
    else:
        extended_list = [x + "!" for x in sentence_list]
        return extended_list



print(return_evens([2,3,23,5,6,88,13,15]))

print(make_exclamation(["ahmed", "hello", "good morning"]))