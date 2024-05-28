def is_anagram(word1,word2):
    """ Check if the two given words are anagrams of each other """
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

print(is_anagram('shankar','raknass'))