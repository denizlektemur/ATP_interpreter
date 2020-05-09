# Lines_interpreter
This repository contains my version of the ATP assignment.
The goal of the assignment was to create an interpreter using only functional programming.
<br><br>My version implements the following should haves:<br>
<b>Advanced language features</b> because I implemented more than the basic addition and substraction operators. In my programming language you can print and add comments as well.
<b>Creating your own programming language</b> because this is a made up programming language</b>

<br>In this document I will try to explain how the program works and how to use it.

|Contents|
|-|
|[Basic info](#Basic-info)|
|[Restrictions](#restrictions)|
|[How to use](#How-to-use)|
|[How to run](#How-to-run)|

## Basic info
This programming language is based on describing the look of an operator in lines hence the name Lines. For example the assignment operator <b>('=')</b> is translated to <b>HORIZONTAL_LINES</b> because it consists of 2 horizontal lines. The equal operator <b>('==')</b> translates to <b>DOUBLE_HORIZONTAL_LINES</b> because it consists of 2 assignment operators. An in depth breakdown of all the operators and keywords can be found in the [How to use](#How-to-use) section.

This program uses the lex, parse, run, structure to execute the given code. Before the lexing can start the input file needs to be prepared. The input gets split into lines <b>('\n')</b>. Every line then gets further split into words <b>(' ')</b>. Every line starting with a question mark <b>('?')</b> gets removed from the list. Tabs <b>('\t')</b> and blanklines also get removed.

### Lexing
When the lexing process starts every word gets compared to a known list of different operators and keywords. The lexer returns a list with tokens containing a value that corresponds to the given operator or keyword. When a word is classified as a digit the lexer returns a token containing the value of the digit. When a word does not match any of the known operators or keywords and is not classified as a digit, the program assumes it is a variable and returns a token containing the variable name.

### Parsing
The parsing process takes all the tokens from the lexer output and turns every token into the corresponding node. For example a token containing the value <b>IF</b> will return a <b>If_node</b>. Operator and keyword nodes store the operation that should be executed as well as their child nodes. When initially turning the tokens into nodes, the child nodes will be initialized as empty nodes. These nodes will be filled in the next step, where they will be turned into a AST.

In order to turn these nodes into a tree, the nodes should be handled in a specific sequence. This is done in order to adhere to mathematical priority rules.<br><br>
<b>Priority list with the top having the most priority:</b>
|Priority list|
|-|
|Multiplication, Division|
|Addition, Subtraction|
|Equals, Greater Than, Less Than|
|Assignment, Print, If, While|

In order to turn the nodes into a tree, the program handles the operators and keywords in the order seen above. When handling the operator the parser looks for the given operator or keyword for instance the <b>Addition Node</b>. When the program finds the <b>Addition Node</b> it takes the adjacent nodes and moves them to the child nodes of the <b>Addition Node</b>. The program repeats this for every <b>Addition Node</b> And every other operator and keyword. The result is a tree on every line with a line only containing 1 root node.

### Running
The program runs by executing the root node of every line. If the root node contains any child nodes with a keyword or operator in it, it will execute the child node(s) first before executing the root/parent node. The program keeps track of all variables and the program counter in a class object called <b>program_state</b>. This <b>program_state</b> gets passed on to every node, in case the node needs to request/modify a variable or change the program counter.

## How to use
### Restrictions
Using this interpreter comes with a few restrictions. First of all, every number will be handled as a float. When using integers the program will use the float variant of the integer. Printing 10 will restult in 10.0 being printed

Every word in the code file should be seperated by a space <b>(' ')</b>, this means you can not do the following:
```C
// Not supported in this interpreter
Variable=2+2
```
Every line of code should also be seperated by a newline character <b>('\n')</b>.

Every line must have an assignment, print, if, while, endif or endwhile, else the program will not work.

### Operators
|Operator|Description|C Equivalent|
|-|-|-|
|<b>HORIZONTAL_AND_VERTICAL_LINES</b>|Adds the two operands|<b>+</b>|
|<b>HORIZONTAL_LINE</b>|Subtracts the right operand from the left operand|<b>-</b>|
|<b>DIAGONAL_LINES</b>|Multiplies the two operands|<b>*</b>|
|<b>DIAGONAL_LINE</b>|Divides the right operand from the left operand|<b>-</b>|
|<b>DOUBLE_HORIZONTAL_LINES</b>|Checks if the two operands are equal|<b>==</b>|
|<b>BROKEN_LINE_LEFT</b>|Checks if the left operand is greater than the right operand|<b>></b>|
|<b>BROKEN_LINE_RIGHT</b>|Checks if the left operand is less than the right operand|<b><</b>|
|<b>HORIZONTAL_LINES</b>|Assigns the value from the right operand to the left operand|<b>=</b>|

### Keywords
|Keyword|Description|C Equivalent|
|-|-|-|
|<b>IF</b>|If the condition after the keyword is True the lines leading up to the matching <b>!IF</b> will be executed. If the condition turns out false the lines leading up to the <b>!IF</b> will be skipped.|<b>if</b>|
|<b>!IF</b>|Signals the end of the matching <b>IF</b>.|<b>}</b>|
|<b>WHILE</b>|If the condition after the keyword is True the lines leading up to the matching <b>!WHILE</b> will be executed until the condition turns false. If the condition turns out false the lines leading up to the <b>!WHILE</b> will be skipped.|<b>while</b>|
|<b>!WHILE</b>|Signals the end of the matching <b>WHILE</b>.|<b>}</b>|
|<b>SHOW</b>|Prints a variable or result from an expression.|<b>printf</b>|
|<b>?</b>|This line will be ignored.|<b>//</b>|

### Example code
```C
? C style:
?
? float my_balance = 25;
? if(my_balance < 10 * 3){
?   printf("%f", my_balance);
? }
?
? Lines style:

my_balance HORIZONTAL_LINES 25
IF my_balance BROKEN_LINE_LEFT 10 DIAGONAL_LINES 3
    SHOW my_balance
!IF

? expected output:
? 25.0

? C style:
?
? float countdown = 10;
? while(countdown > -1){
?   printf("%f", countdown);
?   countdown = countdown - 1
? }
?
? Lines style:

countdown HORIZONTAL_LINES 10
WHILE countdown BROKEN_LINE_RIGHT -1
    SHOW countdown
    countdown HORIZONTAL_LINES countdown HORIZONTAL_LINE 1
!WHILE

? expected output:
? 10.0
? 9.0
? 8.0
? 7.0
? 6.0
? 5.0
? 4.0
? 3.0
? 2.0
? 1.0
? 0.0
```

## How to run
The interpreter needs to be run using the command line.
<br>To run the program use the following line:
<br>`python interpreter.py file_name`
<br><br>With file_name being the name of the code file you want to run.
In the repository there is a test file called my_code.lines. So to run the test code you would replace file_name by my_code.lines.

The program also supports a few command line arguments to show specific statistics when running the program. To use these arguments, simply add them after the file_name.
<br>For example:
<br>`python interpreter.py file_name -l -p`

|Argument|Description|
|-|-|
|<b>-l</b>|Shows the output from the lexer|
|<b>-p</b>|Shows the output from the parser|
|<b>-t</b>|Shows the amount of time it took to run the program|
|<b>-h</b>|Shows all possible arguments|