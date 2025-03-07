from typing import List
def all_construct(target_word: str, word_bank: List[str])-> List[List[str]]:
    #Declare and initialize a list with a len of len(word) + 1 filled with None values
    all_construct_words: List[List[str]] = [None for _ in range(len(target_word) + 1)]

    #Set index 0 of all_construct_words to [[]] since an empty string can be made by the empty list
    all_construct_words[0] == [[]]
    for index in range(len(target_word)):
        for word in word_bank: