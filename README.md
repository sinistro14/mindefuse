# mindefuse
[![Build Status](https://travis-ci.com/sinistro14/mindefuse.svg?token=NY5sBpywnxqMdVGh3wnz&branch=master)](https://travis-ci.com/sinistro14/mindefuse)

Hostage situation negotiator simulation

## Prerequisites
The application is compatible with Linux based systems.
Python version 3.7 is assumed to be installed, as well as pip package manager utility and setuptools module.

## Installation
```bash
./setup_mindefuse.sh
``` 

## How to run

```bash
./run_mindefuse.sh
```

## Commands

Further information is provided while running the application by using _\<command\> -h_ instruction.

* help - list the available commands
* exit | quit - exit the application
* generate_problem - Generates a secret of a given type and size
* run_strategy - Generates and solves a problem in a given number of rounds, using the requested strategy

## Example run

To exercise some of the available commands, one can try:

1. Generate a problem of size 10 and type string, that must be solved in less than 12 rounds.
```
(mindefuse) > generate_problem -r 12 -t string -s 10
EhGnaXhAOH
```

2. Generate and solve a problem with secret sequence _378_ in less than 12 rounds, using Knuth strategy.
```
(mindefuse) > run_strategy -r 12 -a knuth --secret 378
-----------------------------------History-----------------------------------
Round: 1 | Secret: 378 | Guess: 001 | Result: (0, 0) | Time: 000.0000 s
Round: 2 | Secret: 378 | Guess: 223 | Result: (1, 0) | Time: 003.9081 s
Round: 3 | Secret: 378 | Guess: 445 | Result: (0, 0) | Time: 004.7819 s
Round: 4 | Secret: 378 | Guess: 662 | Result: (0, 0) | Time: 005.1764 s
Round: 5 | Secret: 378 | Guess: 377 | Result: (0, 2) | Time: 005.3405 s
Round: 6 | Secret: 378 | Guess: 378 | Result: (0, 3) | Time: 005.3870 s
The game was won!!!
```

3. Generate and solve a problem with secret sequence _iekl_ in less than 12 rounds, using Genetic strategy.
```
(mindefuse) > run_strategy -r 12 -a genetic --secret iekl
-----------------------------------History-----------------------------------
Round: 1 | Secret: iekl | Guess: aabb | Result: (0, 0) | Time: 000.0000 s
Round: 2 | Secret: iekl | Guess: ogdg | Result: (0, 0) | Time: 000.0094 s
Round: 3 | Secret: iekl | Guess: nxxh | Result: (0, 0) | Time: 000.0391 s
Round: 4 | Secret: iekl | Guess: ukyv | Result: (1, 0) | Time: 000.0873 s
Round: 5 | Secret: iekl | Guess: jeve | Result: (0, 1) | Time: 000.2677 s
Round: 6 | Secret: iekl | Guess: mrvw | Result: (0, 0) | Time: 001.1918 s
Round: 7 | Secret: iekl | Guess: ieuf | Result: (0, 2) | Time: 004.2101 s
Round: 8 | Secret: iekl | Guess: ceut | Result: (0, 1) | Time: 007.6359 s
Round: 9 | Secret: iekl | Guess: kepf | Result: (1, 1) | Time: 011.5047 s
Round: 10 | Secret: iekl | Guess: iekz | Result: (0, 3) | Time: 015.8030 s
Round: 11 | Secret: iekl | Guess: iekl | Result: (0, 4) | Time: 039.8143 s
The game was won!!!
```

4. Generate and solve a problem with a randomly generated secret of numeric elements with size 4,
in less than 12 rounds, using Genetic strategy. The generated secret was _8984_.
```
(mindefuse) > run_strategy -r 12 -a genetic -t numeric -s 4
-----------------------------------History-----------------------------------
Round: 1 | Secret: 8984 | Guess: 0011 | Result: (0, 0) | Time: 000.0000 s
Round: 2 | Secret: 8984 | Guess: 8866 | Result: (1, 1) | Time: 000.0173 s
Round: 3 | Secret: 8984 | Guess: 8287 | Result: (0, 2) | Time: 000.1418 s
Round: 4 | Secret: 8984 | Guess: 3286 | Result: (0, 1) | Time: 001.8032 s
Round: 5 | Secret: 8984 | Guess: 8989 | Result: (0, 3) | Time: 003.8772 s
Round: 6 | Secret: 8984 | Guess: 8985 | Result: (0, 3) | Time: 006.3854 s
Round: 7 | Secret: 8984 | Guess: 8988 | Result: (0, 3) | Time: 009.4058 s
Round: 8 | Secret: 8984 | Guess: 8984 | Result: (0, 4) | Time: 012.7700 s
The game was won!!!
```

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Disclaimer

This software was develop as an academic project, therefore,
no enterprise level reliability assurances can be provided.
