from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='diceware_utils',  # Required
    version='0.6.0',  # Required
    description='A collection of tools to make diceware passphrase conform with "password policy"',  # Required
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/patarapolw/diceware_utils',  # Optional
    author='Pacharapol Withayasakpunt',  # Optional
    author_email='patarapolw@gmail.com',  # Optional
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
        'Topic :: Security :: Cryptography'
    ],
    keywords='password leet leetspeak diceware',  # Optional
    packages=['diceware_utils'],  # Required
    install_requires=['PyYAML'],  # Optional
    tests_require=['pytest', 'pytest-doctestplus'],
    extras_require={  # Optional
        'test': ['pytest', 'pytest-doctestplus'],
    },
    package_data={  # Optional
        'diceware_utils': ['database/*',
                           'database/wordlist/*'
                           ],
    },
    # include_package_data=True
)
