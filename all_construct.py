from typing import List
from copy import deepcopy
def all_construct(target_word: str, word_bank: List[str])-> List[List[str]]:
    #Declare and initialize a list with a len of len(word) + 1 filled with None values
    all_construct_words: List[List[str]] = [None for _ in range(len(target_word) + 1)]

    #Set index 0 of all_construct_words to [[]] since an empty string can be made by the empty list
    all_construct_words[0] = [[]]
    for index in range(len(target_word)):
        for word in word_bank:
            if  target_word[index : index + len(word)] == word and all_construct_words[index] != None:
                if all_construct_words[index + len(word)] != None:
                    current = deepcopy(all_construct_words[index])
                    list(map(lambda inner: inner.append(word), current))
                    all_construct_words[index + len(word)].extend(current)
                    # for i in range(len(all_construct_words[index])):
                    #     current[i].append(word)

                    # all_construct_words[index + len(word)].extend(current)
                else:
                    copy_value = deepcopy(all_construct_words[index])
                    for y in range(len(all_construct_words[index])):
                        copy_value[y].append(word)
                    all_construct_words[index + len(word)] = copy_value
    return all_construct_words[len(target_word)]

def main() -> None:
    target_word = 'abcdef'
    word_bank = ['ab', 'abc','cd', 'ef', 'abcd']
    words_construct = all_construct(target_word=target_word, word_bank= word_bank)
    print(words_construct)

if __name__ == "__main__":
    main()