import setuptools
from setuptools import setup, find_packages

setuptools.setup(name='ipa_rhyming',
                 version='1.1.0',
                 packages=find_packages(exclude=['tests']),
                 package_data={'ipa_rhyming': ['static/*', 'ipapy/data/ipa.dat']},
                 classifiers=[
                     'Programming Language :: Python :: 3',
                     'Operating System :: OS Independent',
                     'Topic :: Scientific/Engineering'
                 ],
                 python_requires='>=3',
                 author_email='shambratona@gmail.com',
                 url="https://github.com/AlinaRechina/rhyme_analysis"
                 )
