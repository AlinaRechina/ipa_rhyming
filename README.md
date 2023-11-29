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
