>A PROGRAM TO CHECK WHETHER GIVEN GRAMMAR IS AMBIGUOUS OR NOT 

This topic comes under Theory of Computation where a Grammar G is said to be ambiguous if it has more than 1 Left Most Derivations or Right Most Derivations. Recursive backtracking is the backbone for this program._
In this program the user has to write the productions for the grammar to be checked and in addition to it ,the program also requests user for the word on which ambiguity will be checked. The program will find all the left most derivations and right most derivations for the word and if it comes out to be greater than 1 way , Its ambiguous otherwise not ambiguous for that word.

>Applications Required:

This project has been made in Python 3.5. Use python IDLE to run the program.

>Example:

Input format :
Enter no. of productions:3_
Enter the productions ( use # to denote null string )_

S->aSbS_
S->bSaS_
S->#_
Enter the word to be checked: abab_
Enter the Start Symbol: S_

Output :_
The number of Right Most Derivations is: 2_
The number of Left Most Derivations is: 2_
Ambiguous_

I have also shown the word formed at each step of the derivation after substitution ,for explanation purpose.You can get rid of it by commenting that part of the code.

>Built With

Python 3.5 IDLE

>Limitations

There are some grammar on which it may not give the right solution particularly if the grammar is left recursion. For left recursion some cases may still pass but some may fail. _
Another exception is , if we put the given word as an empty string , these type of examples may create problem and need further improvement in the program. 
