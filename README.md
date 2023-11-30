### This is a library for rhymes detection.

## How to use ipa_rhyming
```python
pip install ipa_rhyming
```
```python
import ipa_rhyming
rhyme = ipa_rhyming.Rhymer('ko', 'en')
print(rhyme.get_rhyme_type('mʌtc͈iŋkjʌlmɐlʲetɐkʰʲe', 'haɪweɪhaɪweɪ'))

>>> exact_perfect rhyme
```
**Breaking down the output:**  
The part before "_" determines the type of rhyme depending on a vowels in last syllables.
- **exact** - vowels are the same
- **rhyme** - vowels are included in the list of combinations compiled by us on the basis of statistics. Check combinations for each pair of laguages [here](https://github.com/AlinaRechina/rhyme_analysis/tree/main/ipa_rhyming/static)
- **not a rhyme** - vowels are **not** included in the list of combinations compiled by us on the basis of statistics.
