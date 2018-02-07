Exercise 1:

Please write a program which will take in a word from a user and search for that word in the word.txt file.

Example:

If the user enters the word "hello", the program should return the word "hello" if "hello" is in word.txt, otherwise it should return "NOT FOUND".

Exercise 2:

Please write a program which count and print the numbers of each character, from file letters.txt.

Example:

If the following string is given as input from file letters.txt to the program:

abcdefgabc

Then, the output of the program should be:

a,2

c,2

b,2

e,1

d,1

g,1

f,1

Hints:

Use dict to store key/value pairs.

Use dict.get() method to lookup a key with default value.

Exercise 3:

Take input from a user until they enter the word "quit". Once they enter the word quit print each line they entered in order.

Exercise 4:

The Sieve of Eratosthenes is a technique that was developed more than 2,000 years ago to easily find all of the prime numbers between 2 and some limit, say 100. 

A description of the algorithm follows:

Write down all of the numbers from 0 to the limit Cross out 0 and 1 because they are not prime

Set p equal to 2

While p is less than the limit do

Cross out all multiples of p (but not p itself)

Set p equal to the next number in the list that is not crossed out

Report all of the numbers that have not been crossed out as prime

The key to this algorithm is that it is relatively easy to cross out every nth number on a piece of paper. This is also an easy task for a computer—a for loop can simulate this behavior when a third parameter is provided to the range function. When a number is crossed out, we know that it is no longer prime, but it still occupies space on the piece of paper, and must still be considered when computing later prime numbers.

As a result, you should not simulate crossing out a number by removing it from the list. Instead, you should simulate crossing out a number by replacing it with 0. Then, once the algorithm completes, all of the non-zero values in the list are prime.

Create a Python program that uses this algorithm to display all of the prime numbers between 2 and a limit entered by the user. If you implement the algorithm correctly you should be able to display all of the prime numbers less than 1,000,000 in a few seconds.

```
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
```


Exercise 5:

Write a program that will take in a filename and a shift number, use the Ceasar cipher on the contents of the file and output to a second file with the name "encrypted_file.txt"


Exercise 6:

Write a program that takes a filename and an integer `n` and prints the `n` most common words in the file, and the count of their occurrences, in descending order.

For example:

        "article.txt" and 5 will return

        "the", 39
        "device", 21
        "start", 14
        "pidgeon", 9
        "box", 3

Import the included `article.txt` file and use that to test your program. What are the top 10 words and their frequency?



