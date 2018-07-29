from setuptools import setup, find_packages
from what import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='what',
    version=__version__,
    description='Python package to help look up errors.',
    long_description='''
        Python package to help look up errors.
    ''',
    keywords='python package errors ',
    author='Shreyas Mohan',
    author_email='shreyas5@illinois.edu',
    url='',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'certifi==2018.4.16',
        'chardet==3.0.4',
        'idna==2.6',
        'preggy==1.4.2',
        'requests==2.18.4',
        'six==1.11.0',
        'Unidecode==1.0.22',
        'urllib3==1.22'
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    
    entry_points={
        'console_scripts': [
            'what=what.main:main',
        ],
    },
)
