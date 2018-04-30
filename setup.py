from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='diceware_utils',  # Required
    version='0.2.0',  # Required
    description='A leetspeak-based password strengthener, while attempting minimalistic change.',  # Required
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/patarapolw/leetpass',  # Optional
    author='Pacharapol Withayasakpunt',  # Optional
    author_email='patarapolw@gmail.com',  # Optional
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='password leet leetspeak diceware',  # Optional
    packages=['diceware_utils'],  # Required
    install_requires=['PyYAML'],  # Optional
    tests_require=['pytest'],
    extras_require={  # Optional
        'test': ['pytest'],
    },
    package_data={  # Optional
        'diceware_utils': ['database'],
    },
)
