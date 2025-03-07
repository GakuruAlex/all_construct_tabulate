from typing import List
from copy import deepcopy
def all_construct(target_word: str, word_bank: List[str])-> List[List[str]]:
    #Declare and initialize a list with a len of len(word) + 1 filled with None values
    all_construct_words: List[List[str]] = [None for _ in range(len(target_word) + 1)]

    #Set index 0 of all_construct_words to [[]] since an empty string can be made by the empty list
    all_construct_words[0] = [[]]
    for index in range(len(target_word)):
        for word in word_bank:
            current_target_word: str = target_word[index : len(word)]
            save_index: int = index + len(word)
            if current_target_word == word:
                if all_construct_words[save_index] != None:
                    for values in all_construct_words[save_index]:
                        values.append(word)
                else:
                    copy_value = deepcopy(all_construct_words[index])
                    for values in copy_value:
                        values.append(word)
                    all_construct_words[save_index] = copy_value
    return all_construct_words[len(word)]

def main() -> None:
    target_word = 'abcdef'
    word_bank = ['ab', 'abc', 'abc', 'cd', 'ef', 'abcd']
    words_construct = all_construct(target_word=target_word, word_bank= word_bank)
    print(words_construct)

if __name__ == "__main__":
    main()