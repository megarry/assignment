# assignment
<H3>Problem statement</H3>





For the end of year administration of Programming for History of Arts students you are to write a program that has 2 functions:

1.calculate a final grade

2.print a small graph of similarity scorn and, if applicable, list the students under investigation

The input is structured as follows:

The first line should be interpreted as follows:

Net van Cogh__5 6 7 4 5 6
5=20=22=10=0=0=1=0=1;Vincent Appel,Johannes Mondriaan
Karel van Rijn__7 8 6 6
2=30=15=8=4=3=2=0=0=0;
< Name of the student>< one or more underscores>< one or more grades separated by spaces>
You have to calculate the average grade of the student. All grades have the same weight, with the following conditions:

grades are rounded to the nearest half
a grade that is >= 5.5 AND < 6 should be noted as a "6-"
The second line should be interpreted as follows:

< 10 numbers separated by = >;< zero or more names separated by ,>
The first 10 numbers are the similarity scores. These scores represent the number of programs matching a certain percentage of the current program in steps of 10%. This means the first numbers indicates the matches from 1%-10% and the last number indicates the matches from 91%-100%.

Since this is not very readable, the professor would like a simple graph according to these rules:

if there are zero matches, display an underscore: _
if there are less than 20 matches, display a minus sign: -
if there are 20 or more matches, display a caret ^
The names of the students after the semicolon are the names of the students with matches in the final 3 categories. The names of these students should be printed under the graph. If there are no matches, the program should print "No matches found".

The output for the aforementioned input should be:

Piet van Gogh has an average of 6-
-^^--_-_-
Vincent Appel
Johannes Mondriaan
Karel van Rijn has an average of 7
-^-----__
No matches found
