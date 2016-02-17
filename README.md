# MultipleFindReplace
Python script that find a list of terms in a CSV file and replace them with the corresponding terms. The lists of terms to be found and replaced have to be provided in two separate files.

How to use:

You have to prepare 4 plain text files.
Suppose you have, in your Desktop, these files: listf, listr, corpus, result.
The path of the first file is "/home/user/Desktop/listf" where user is you username if you are in Linux environment.

Result is an empty file.
Corpus contains the text in which find and replace terms. It has to be a CSV file where comma is the separator.

Listf and listr are similar to a pair key-value. Listf contains the keys (one per line) and listr contains the values (one per line). The script search for keys in the corpus and replace them with values, writing the output in result file.

Keys and values could be composed by one or more words, separated by spaces.


