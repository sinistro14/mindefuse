#! usr/bin/env python3.7

from setuptools import setup, find_packages

setup(
    name='mindefuse',

    version='0.9.0',

    description='Hostage situation negotiator simulation',

    url='https://github.com/sinistro14/mindefuse',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Education',
                             
        'Topic :: Software Development :: TODO',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.7',

        'Operating System :: POSIX :: Linux',

        'Natural Language :: English',

        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        'Topic :: Scientific/Engineering :: Information Analysis',
    ],

    keywords='python hostage negotiation',

    packages=find_packages(exclude=['tests']),

    install_requires=[
        'cmd',
    ],

    tests_require=[
        'pytest',
        'mock',
        'pytest-mock'
    ],


    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'mindefuse=mindefuse:main',
        ],
    },

    project_urls={
        'Source': 'https://github.com/sinistro14/mindefuse'
    }
)
