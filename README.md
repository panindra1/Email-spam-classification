# Email-spam-classification
This is a  classification of text documents.
There are two data sets for classification
1) Email-spam
2) Eight newsgroup dataset

Two major files
1) NaiveBayes.py
2) categoryClassification.py

Input files: test_email.txt, train_email.txt (for Naive Bayse)
             8category.training.txt, 8category.testing.txt (for categoryClassification)

Output: (For Naive Bayse)
254
97.6923076923
Confusion Matrix
This is a 2x2 matrix whose entry in row r and column c is the percentage of test images from class r that are classified as class c.

0.961538461538 0.0384615384615
0.00769230769231 0.992307692308

Top20 Spam words --email 
s 
order 
report 
our 
address 
mail 
program 
send 
...

Top20 Not spam words
anguage 
university 
s
linguisti
de
information
...

Top 20 Odds ratio (For each pixel feature Fij and pair of classes c1, c2, the odds ratio is defined as
odds(Fij=1, c1, c2) = P(Fij=1 | c1) / P(Fij=1 | c2).

language : 1.35372052523
university : 1.29425942509
de : 1.22384116895
conference : 1.20620230213
english : 1.18226805072
edu : 1.1640902452
papers : 1.16218442133
speech 

etc..

The output is same for 8category as well.

