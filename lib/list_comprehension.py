#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    add_exclaim = [n + "!" for n in sentence_list]
    return add_exclaim