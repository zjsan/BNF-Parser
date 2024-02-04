
# BNF PARSER

This progam used the concept of recursive descent parser for the parsing of expressions. 

 A Python program that can parse and validate simple arithmetic expressions adhering to the provided BNF grammar below:
    
    <expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term>
    <term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
    <factor> ::= <number> | "(" <expression> ")"
    <number> ::= <digit> | <digit> <number>
    <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9


## Installation

Install the thru cloning the repository

```bash
  https://github.com/zjsan/BNF-Parser
```

Python version:
Python 3.10.7

IDE: Visual Studio Code
    
## Acknowledgements

 - [Recursive Descent Parser - geeksforgeeks](https://www.geeksforgeeks.org/recursive-descent-parser/)



## Authors

- [@zjsan](https://github.com/zjsan)

