# Compiler scanner
College assignment to implement "TINY language" scanner. <br />
Scanning is  the process of converting a sequence of characters (such as in a computer program or web page) into a sequence of tokens (strings with an identified "meaning").A program that performs lexical analysis may be called a lexer, tokenizer, or scanner.<br />
## Implementation of a TINY scanner.
The scanner is using the finite state machine in it's core algorithm to identify three types of tokens [Number, identifier, Special Symbol].<br />
To be able to use it, you need to install it's dependencies.
## Installation
1. install dependencies.
2. git clone or zip download.

### Dependencies 


```
pip install transitions
```
## Usage

```
python scanner.py input.txt output.txt
```
#### where:
input.txt: is the input file.
output.txt: is the output file.
