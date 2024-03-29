import pandas as pd
import math
import json
import os
from .ipapy.ipastring import IPAString


class Rhymer:

    def __init__(self, lang1, lang2):
        self.difs = ['eɪ', 'oʊ', 'aɪɚ', 'aɪ', 'uə', 'ɔɪ']
        self.dict_pos = {'front': 1, 'near-front': 0.5,
                         'central': 0,
                         'near-back': -0.5, 'back': -1}
        self.dict_raise = {'open': 1, 'near-open': 0.75, 'open-mid': 0.5,
                           'mid': 0,
                           'close-mid': -0.5, 'near-close': -0.75, 'close': -1}

        self.path_to_module = os.path.dirname(__file__)
        self.pairs_path = os.path.join(self.path_to_module, "static", f"{lang1}_{lang2}.json")

        with open(self.pairs_path, 'r', encoding='utf-8') as rvf:
            self.rhyming_vowels = json.load(rvf)

    @staticmethod
    def get_last_syll(string):
        """
        Finds last syllable in the string&

        Args:
            string: str
                transcribed string in Unicode

        Returns: IPAString
            last syllable -- CV(C*)
        """

        desired = ['diacritic', 'suprasegmental']
        string = IPAString(unicode_string=string)
        ending = IPAString()

        for i in reversed(string):
            if i.name.split()[-1] in desired:
                ending.insert(0, i)
            elif i.name.split()[-1] == 'vowel':
                ending.insert(0, i)
            elif i.name.split()[-1] == 'consonant':
                ending.insert(0, i)
                if len(ending.vowels) >= 1:
                    break

        return ending.letters

    def split_on_vowel(self, syllable):
        """
        Eliminates vowels from the last syllable.

        Args:
            syllable: IPAString

        Returns: list
            syllable split by vowel, e.g. run --> ['r', 'n']
        """

        for dif in self.difs:
            if dif in str(syllable):
                syllable1 = str(syllable).split(dif)
                return syllable1, dif

            else:
                vowel = syllable.vowels[0]
                syllable2 = str(syllable).split(str(vowel))
        return syllable2, str(vowel)

    @staticmethod
    def a_or_f(split1, split2):
        """
        Decides whether rhyme is assonance or family.

        Args:
            split1: list
            split2: list
                both are lists of consonants in the syllable.

        Returns: str
            type of the rhyme depending on consonants.
        """

        split1, split2 = IPAString(unicode_string=split1), IPAString(unicode_string=split2)
        if split1[-1].name[-2] == split2[-1].name[-2]:
            rhyme_type = 'family rhyme'
        else:
            rhyme_type = 'assonance rhyme'
        return rhyme_type

    def on_vowels_phys(self, syll1, syll2):
        """
        Check type of rhyme based on a vowel in the last syllable.

        Args:
            syll1: IPAString
            syll2: IPAString

        Returns: str
            verdict depending on the degree of vowel similarity.
        """

        v1, v2 = syll1.vowels[0], syll2.vowels[0]
        if v1.is_equivalent(v2):
            return 'exact_'
        else:
            if v1.descriptors[-1] == v2.descriptors[-1]:
                diff_on_pos = abs(self.dict_pos[v1.descriptors[2]] - self.dict_pos[v2.descriptors[2]])
                diff_on_raise = abs(self.dict_raise[v1.descriptors[1]] - self.dict_raise[v2.descriptors[1]])
                if math.sqrt(diff_on_pos ** 2 + diff_on_raise ** 2) < 1.5:
                    return 'close to_'
                else:
                    return 'need to clarify_'
            else:
                return 'different roundness_'

    def on_vowels(self, syll1, syll2):
        """
        Check type of rhyme based on a vowel in the last syllable.

        Args:
            syll1: IPAString
            syll2: IPAString

        Returns: str
            verdict depending on the degree of vowel similarity.
        """

        v1, v2 = syll1.vowels[0], syll2.vowels[0]
        if v1.is_equivalent(v2):
            return 'exact_'
        else:
            # print(self.static)
            v1, v2 = syll1.vowels, syll2.vowels
            # print([str(v1.letters), str(v2.letters)])
            # print(self.rhyming_vowels)
            if [str(v1.letters), str(v2.letters)] in self.rhyming_vowels:
                # print(1)
                return 'rhyme_'
            else:
                return 'not a rhyme_'

    def get_rhyme_type(self, string1, string2, return_syllables=True, return_vowels=True):
        """
        Determines rhyme type depending on last consonant(s) and combines with verdict on vowels.

        Args:
            string1: str
            string2: str
                transcriptions in Unicode

        Returns: str
            final verdict on rhyme type.
        """

        self.syll1 = self.get_last_syll(string1)
        self.syll2 = self.get_last_syll(string2)
        split_syll1, vowel1 = self.split_on_vowel(self.syll1)
        split_syll2, vowel2 = self.split_on_vowel(self.syll2)

        if split_syll1[-1] == split_syll2[-1]:
            rhyme_type = 'perfect rhyme'
        else:
            shared_len = len(split_syll1[-1]) + len(split_syll2[-1])
            if (shared_len == len(split_syll1[-1])) or (shared_len == len(split_syll2[-1])):
                rhyme_type = 'additive/subtractive rhyme'
            else:
                rhyme_type = self.a_or_f(split_syll1[-1], split_syll2[-1])

        vowel_similarity = self.on_vowels(self.syll1, self.syll2)

        return_value = {'rhyme_type': vowel_similarity + rhyme_type}
        if return_syllables:
            return_value['sylls'] = (str(self.syll1), str(self.syll2))
        if return_vowels:
            return_value['vowels'] = (vowel1, vowel2)

        return return_value
