### This is a library for rhymes detection.

## Table of contents
1. [How to use ipa_rhyming](#how-to-use-ipak_rhyming)
2. [Explanation of output (types of rhymes)](#explanation-of-output-types-of-rhymes)
3. [Authors](#authors)

## How to use ipa_rhyming
```python
pip install ipa_rhyming
```
```python
import ipa_rhyming
rhyme = ipa_rhyming.Rhymer('ko', 'en')
print(rhyme.get_rhyme_type('mʌtc͈iŋkjʌlmɐlʲetɐkʰʲe', 'haɪweɪhaɪweɪ'))

>>> {'rhyme_type': 'exact_perfect rhyme', 'sylls': ('kʰʲe', 'weɪ'), 'vowels': ('e', 'eɪ')}
```
## Explanation of output (types of rhymes)
The part before "_" determines the type of rhyme depending on vowels in last syllables.
- **exact** - vowels are the same
- **rhyme** - vowels are included in the list of combinations compiled by us on the basis of statistics, that is why we consider them rhymyng. Check combinations for each pair of laguages [here](https://github.com/AlinaRechina/rhyme_analysis/tree/main/ipa_rhyming/static)
- **not a rhyme** - vowels are **not** included in the list of combinations compiled by us on the basis of statistics

The part after "_" determines the type of rhyme depending on final consonants in last syllables.
- **pefect** - consonants are identical (mouse-house)
- **family** - consonants are different, but belong to the same family (heart-park)
- **assonance** - consonants are different and do not belong to the same family (light-shine)
- **additive** - consonants are added or substracted (contrary - married)

For more information on types of rhymes check [this document](https://docs.google.com/document/d/1twgABd6UiY-moVrT9AQd4vxxsHfdxSepO0EfpFpGdsM/edit#heading=h.xjvr0ln37qdp)

## Authors
Alina Lobanova (HSE University)  
Ekaterina Neminova (HSE University)  
Varvara Vasilyeva (HSE University)  
Alyona Zenina (HSE University)
