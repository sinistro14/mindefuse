#! usr/bin/env python3.7

from setuptools import setup, find_packages

setup(
    name='mindefuse',

    python_requires='>=3.6.0',

    version='1.0.0',

    description='Hostage situation negotiator simulation',

    long_description=open('README.md', 'r').read(),

    long_description_content_type="text/markdown",

    url='https://github.com/sinistro14/mindefuse',

    download_url='https://github.com/schollz/howmanypeoplearearound/archive/v0.1.6.tar.gz',

    author="sinistro14",

    author_email="tiago14_ribeiro@ħotmail.com",

    license="MIT",

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Education',
                             
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',

        'Programming Language :: Python :: 3.7',

        'Operating System :: POSIX :: Linux',

        'Natural Language :: English',

        'Topic :: Games/Entertainment :: Simulation',

        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        'Topic :: Scientific/Engineering :: Information Analysis',
    ],

    keywords='python hostage negotiation',

    scripts=['make.py'],

    packages=find_packages(exclude=['tests']),

    install_requires=[
    ],

    tests_require=[
        'pytest',
        'mock',
        'pytest-mock',
        'pytest-repeat',
    ],

    extras_require={
        'dev': [
            'wheel',
        ]
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'mindefuse = mindefuse.__main__:main',
        ],
    },
)
