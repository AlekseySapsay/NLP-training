#! /usr/bin/env python
# -*- coding: utf-8 -*-

import nltk # the master library for NLP
import not_comperative_superlative  # my func to convert adj for positive form
import sys # module for handle with exceptions and interruption program

from nltk.corpus import wordnet # exaples from sendex NLP

from pattern.en import parsetree # to grow the word tree
from pattern.en import pluralize, singularize,NOUN, ADJECTIVE # for parsing nouns
from pattern.en import comparative, superlative # comperative and superlative adjunction
from pattern.en import conjugate, lemma, lexeme # module to work with verbs
from pattern.en import tenses, PAST, PL # work with tenses of verb
from pattern.en import verbs, conjugate, PARTICIPLE # Rule-based conjugation


# from the description pattern.en module, I would like to add modules
# thet modules can to help in tuning standard functions from NLTK, pattern.en . And compose work with it like the classes and the part of speech.
from itertools import izip, chain
try:
    from config import SLASH
    from config import WORD, POS, CHUNK, PNP, REL, ANCHOR, LEMMA
    MBSP = True # Memory-Based Shallow Parser for Python.
except:
    SLASH, WORD, POS, CHUNK, PNP, REL, ANCHOR, LEMMA = \
        "&slash;", "word", "part-of-speech", "chunk", "preposition", "relation", "anchor", "lemma"
    MBSP = False
