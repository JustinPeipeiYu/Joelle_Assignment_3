from typing import List
from typing import Tuple
from typing import Dict

from poetry_constants import (
    CLEAN_POEM, WORD_PHONEMES, LINE_PRONUNCIATION, POEM_PRONUNCIATION,
    PRONOUNCING_DICTIONARY)
"""Functions for reading the pronouncing dictionary and the poetry forms files
"""
from typing import TextIO

from poetry_constants import (
    # CLEAN_POEM, WORD_PHONEMES, LINE_PRONUNCIATION, POEM_PRONUNCIATION,
    PRONOUNCING_DICTIONARY, POETRY_FORM, POETRY_FORMS)

SAMPLE_POETRY_FORM_FILE = '''Limerick
8 A
8 A
5 B
5 B
8 A

Haiku
5 *
7 * 
5 *
'''
EXPECTED_POETRY_FORMS = {
    'Limerick': ([8, 8, 5, 5, 8], ['A', 'A', 'B', 'B', 'A']),
    'Haiku': ([5, 7, 5], ['*', '*', '*'])
}

SAMPLE_DICTIONARY_FILE = ''';;; Comment line
ABSINTHE  AE1 B S IH0 N TH
HEART  HH AA1 R T
FONDER  F AA1 N D ER0
'''

EXPECTED_DICTIONARY = {
    'ABSINTHE': ['AE1', 'B', 'S', 'IH0', 'N', 'TH'],
    'HEART': ['HH', 'AA1', 'R', 'T', ],
    'FONDER': ['F', 'AA1', 'N', 'D', 'ER0']
}

SAMPLE_POEM_FILE = '''  Is this mic on?

Get off my lawn.
'''


def read_and_trim_whitespace(poem_file: TextIO) -> str:
    """Return a string containing the poem in poem_file, with
     blank lines and leading and trailing whitespace removed.

     >>> import io
     >>> poem_file = io.StringIO(SAMPLE_POEM_FILE)
     >>> read_and_trim_whitespace(poem_file)
     'Is this mic on?\\nGet off my lawn.'
     """
    
    cleaned_line = ""
    for line in poem_file.readlines():
        if line != "\n":
            cleaned_line += line.strip(" ")
    return cleaned_line.strip()

def read_pronouncing_dictionary(
        pronunciation_file: TextIO) -> PRONOUNCING_DICTIONARY:
    """Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.

    >>> import io
    >>> dict_file = io.StringIO(SAMPLE_DICTIONARY_FILE)
    >>> result = read_pronouncing_dictionary(dict_file)
    >>> result == EXPECTED_DICTIONARY
    True
    """
    
    pronunciation_dictionary = {}
    for line in pronunciation_file.readlines():
        if ";;;" not in line and line != "\n":
            line_components = line.split()
            word = line_components.pop(line_components.index(line_components[0]))
            pronunciation_dictionary[word] = line_components
    return pronunciation_dictionary

def read_poetry_form_descriptions(
        poetry_forms_file: TextIO) -> POETRY_FORMS:
    """Return a dictionary of poetry form name to poetry pattern for the poetry
    forms in poetry_forms_file.

    >>> import io
    >>> form_file = io.StringIO(SAMPLE_POETRY_FORM_FILE)
    >>> result = read_poetry_form_descriptions(form_file)
    >>> result == EXPECTED_POETRY_FORMS
    True
    """
    poetry_forms_file_list = poetry_forms_file.readlines()
    index_of_line_currently_being_read = 0
    name = ""
    poem_dictionary = {}
    
    while index_of_line_currently_being_read < len(poetry_forms_file_list):
        if poetry_forms_file_list[index_of_line_currently_being_read].strip().isalpha():
            name = poetry_forms_file_list[index_of_line_currently_being_read].strip()
            index_of_line_currently_being_read += 1
        elif poetry_forms_file_list[index_of_line_currently_being_read] == "\n":
            index_of_line_currently_being_read += 1
        else:
            (poetry_pattern, index_of_line_currently_being_read) = read_single_poetry_form(poetry_forms_file_list, index_of_line_currently_being_read)
            poem_dictionary[name] = poetry_pattern
    return poem_dictionary
        

def read_single_poetry_form(
        poetry_forms_file_list: List[str], start_index: int) -> (Tuple[List[int], List[str]], int):
    """Return a dictionary of one poetry pattern for a single poetry form in 
    poetry_forms_file.
    
    >>> form_file_list = ["Limerick", "8 A", "8 A", "5 B", "5 B", "8 A", "\n", "Haiku", "5 *", "7 *", "5 *"]
    >>> read_single_poetry_form(form_file_list, 1)
    (([8, 8, 5, 5, 8], ['A', 'A', 'B', 'B', 'A']), 6)
    >>> form_file_list = ["Limerick", "8 A", "8 A", "5 B", "5 B", "8 A", "\n", "Haiku", "5 *", "7 *", "5 *"]
    >>> read_single_poetry_form(form_file_list, 8)
    ((['5', '7', '5'], ['*', '*', '*']), 11)
    """
    
    rhyme_scheme_list = [] #list for each lines rhyme scheme
    syllable_list = [] #list for each lines number of syllables
    index_of_line_currently_being_read = start_index
    line_currently_being_read = poetry_forms_file_list[index_of_line_currently_being_read]
    while  (index_of_line_currently_being_read < len(poetry_forms_file_list)
            and line_currently_being_read != "\n"):
        line_components = line_currently_being_read.strip().split(" ") #creates a list of elements split by " "
        line_components[0] = ((int)(line_components[0]))
        rhyme_scheme_list.append(line_components[1])
        syllable_list.append(line_components[0])
        index_of_line_currently_being_read += 1
        if index_of_line_currently_being_read < len(poetry_forms_file_list):
            line_currently_being_read = poetry_forms_file_list[index_of_line_currently_being_read]
    
    return (syllable_list, rhyme_scheme_list), index_of_line_currently_being_read

if __name__ == '__main__':
    import doctest

    #doctest.testmod()