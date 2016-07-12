The contains of the respository are:
README.txt (this file)
Source code (python .py file in the src folder)
Input file (.txt file in the input_file folder)
Output file (.txt file in the output_file folder)

The code is written in python 2.7.11 using the following dependencies (external libraries)
pandas
numpy 
ast
simplejson

The code imports the input file and converts it into pandas dataframe object. 
Subsequently, the code runs an outer and inner loop on the dataframe object to compute the rolling median. 
The rolling median is stored in a seperate output object. 
Finally the output is written to an external .txt file and all in-memory object holdig the data are deleted.
