from typing import List
from typing import Tuple
from typing import Dict

from poetry_constants import (
    CLEAN_POEM, WORD_PHONEMES, LINE_PRONUNCIATION, POEM_PRONUNCIATION,
    PRONOUNCING_DICTIONARY)


# ===================== Helper Functions =====================
    
def ALL_CAPS(text: str) -> str:
    """Convert lines to all caps.
    
    >>> ALL_CAPS('Feeling alive at twenty-five. Feeling bliss at twenty-six.')
    'FEELING ALIVE AT TWENTY-FIVE. FEELING BLISS AT TWENTY-SIX.'
    
    >>> ALL_CAPS('Jack and Jill went up the hill to fetch a pail of water. Jack \
    fell down and broke his crown and Jill came tumbling after.')
    'JACK AND JILL WENT UP THE HILL TO FETCH A PAIL OF WATER. JACK FELL DOWN AND BROKE HIS CROWN AND JILL CAME TUMBLING AFTER.'
    """
    return text.upper()
def clean_word(s: str) -> str:
    """Return a new string based on s in which all letters have been converted
    to uppercase and whitespace and punctuation characters have been stripped
    from both ends. Inner punctuation and whitespace is left untouched.

    >>> clean_word('Birthday!!!')
    'BIRTHDAY'
    >>> clean_word('  "Quoted?"\\n\\n\\n')
    'QUOTED'
    """
    
    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r''"""
    result = s.upper().strip(punctuation)
    return result

def clean_poem(raw_poem: str) -> CLEAN_POEM:
    """Return the non-blank, non-empty lines of poem, with whitespace removed
    from the beginning and end of each line and all words capitalized.
    >>> clean_poem('The first line leads off,\\n\\n\\nWith a gap before the next.\\n    Then the poem ends.\\n')
    [['THE', 'FIRST', 'LINE', 'LEADS', 'OFF'], ['WITH', 'A', 'GAP', 'BEFORE', 'THE', 'NEXT'], ['THEN', 'THE', 'POEM', 'ENDS']]
    """
    
    cleaned_master_list =[]
    master_list = raw_poem.split('\\n')
    master_list2 = []
    for line in master_list:
        if line != '':
            master_list2.append(line) 
    master_list3 = []
    for line in master_list2:
        master_list3.append(line.split())
    for line in master_list3:
        cleaned_list = []
        for word in line:
            cleaned_list.append(clean_word(word))
        cleaned_master_list.append(cleaned_list)
    return cleaned_master_list

def extract_phonemes(cleaned_poem: CLEAN_POEM, word_to_phonemes: PRONOUNCING_DICTIONARY) -> POEM_PRONUNCIATION:
    """Return a list where each inner list contains the phonemes for the
    corresponding line of poem_lines.

    >>> word_to_phonemes = {'YES': ['Y', 'EH1', 'S'], 'NO': ['N', 'OW1']}
    >>> extract_phonemes([['YES'], ['NO', 'YES']], word_to_phonemes)
    [[['Y', 'EH1', 'S']], [['N', 'OW1'], ['Y', 'EH1', 'S']]]
    """
    
    master_list = []
    for line in cleaned_poem:
        line_list = []
        for word in line:
            #words = []
            value = word_to_phonemes[word]
            #convert word into the pronouncing dictionary
            #words.append(value)
            line_list.append(value)
            #add to the list of the line
        master_list.append(line_list)
    return master_list

def phonemes_to_str(poem_pronunciation: POEM_PRONUNCIATION) -> str:
    """Return a string containing all the phonemes in each word in each line in
    poem_pronunciation. The phonemes are separated by spaces, the words are
    separated by ' | ', and the lines are separated by '\n'.

    >>> phonemes_to_str([[['Y', 'EH1', 'S']], [['N', 'OW1'], ['Y', 'EH1', 'S']]])
    'Y EH1 S\\nN OW1 | Y EH1 S'
    """
    poem_lines =[]
    sentence = ''
    
    for line in poem_pronunciation:
        line_list = []
        for word in line:
            line_list.append(" ".join(word))
        poem_lines.append(" | ".join(line_list))
    return "\\n".join(poem_lines)


def get_rhyme_scheme(poem_pronunciation: POEM_PRONUNCIATION) -> List[str]:
    """Return a list of last syllables from the poem described by
    poem_pronunction.

    Precondition: poem_pronunciation is not empty and each PHONEMES list
    contains at least one vowel phoneme.

    >>> get_rhyme_scheme([[['IH0', 'N']], [['S', 'IH0', 'N']]])
    ['A', 'A']
    """
    # if the last pronounciation is the same then assign the same rhyme scheme
    # get last elements of inner list and if it's the same produce a rhyme
    list_of_keys = []
    last_phonemes = []
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    
    for line in poem_pronunciation:
        for word in line:
            for letter in word: 
                last_phonemes.append([letter[-1] for letter in word])
                
                rhyme_schemes = {}
                for i in range(len(last_phonemes)):
                    last_phonemes[alphabet[i]] = last_phonemes[i]                
 
    for key in ryhme_schemes.keys():
        list_of_keys = list_of_keys.append(keys)   
        
    return list_of_keys

def get_num_syllables(poem_pronunciation: POEM_PRONUNCIATION) -> List[int]:
    """Return a list of the number of syllables in each poem_pronunciation
    line.
    
    >>> get_num_syllables([[['IH0', 'N']], [['S', 'IH0', 'N']]])
    [1, 1]
    """
    counting_list = []
    for line in poem_pronunciation:
        count = 0
        for word in line:
            for letter in word:
                if letter[-1] in '0123456789':
                    count += 1
        counting_list.append(count)        
    return counting_list


if __name__ == '__main__':
    import doctest

   # doctest.testmod()