Exercise 1:



Write a Python program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".



Exercise 2:

A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words. Write a program that reads a string from the user and uses a loop to determines whether or not it is a
palindrome. Display the result, including a meaningful output message.

Exercise 3:

Two words are anagrams if they contain all of the same letters, but in a different order. For example, “evil” and “live” are anagrams because each contains one e, one i, one l, and one v. Create a program that reads two strings from the user, determines whether or not they are anagrams, and reports the result.

Exercise 4: 



Write a Python program to construct the following pattern, using a nested for loop.



\* 



\* \* 



\* \* \* 



\* \* \* \* 

\* \* \* 

\* \* 

\* 

\* \* 

\*




\* \* \* 

\* \* 



\* 



Exercise 5: 



Multiplication Table In this exercise you will create a program that displays a multiplication table that shows the products of all combinations of integers from 1 times 1 up to and including 10 times 10. Your multiplication table should include a row of labels across the top of it containing the numbers 1 through 10. It should also include labels down the left side consisting of the numbers 1 through 10. When completing this exercise you will probably find it helpful to be able to print out a value without moving down to the next line. This can be accomplished by added end="" as the last parameter to your print statement. For example, print("A") will display the letter A and then move down to the next line. The statement print("A", end="") will display the letter A without moving down to the next line, causing the next print statement to display its result on the same line as the letter A.


Exercise 6:

One of the first known examples of encryption was used by Julius Caesar. Caesar needed to provide written instructions to his generals, but he didn’t want his enemies to learn his plans if the message slipped into their hands. As result, he developed what later became known as the Caesar Cipher.

The idea behind this cipher is simple (and as a result, it provides no protection against modern code breaking techniques). Each letter in the original message is shifted by 3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc. The last three letters in the alphabet are wrapped around to the beginning: X becomes A, Y becomes B and Z becomes C. Non-letter characters are not modified by the cipher.

Write a program that implements a Caesar cipher. Allow the user to supply the message and the shift amount, and then display the shifted message. Ensure that your program encodes both uppercase and lowercase letters. Your program should also support negative shift values so that it can be used both to encode messages and decode messages. Hints: ord(), chr()

```
 https://learncryptography.com/classical-encryption/caesar-cipher
```

Exercise 6: 

Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase “i” should be replaced with an uppercase “I” if it is both preceded and followed by a space. The first character in the string should also be capitalized, as well as the first non-space character after a “.”, “!” or “?”. For example, if the function is provided with the string “what time do i have to be there? what’s the address?” then it should return the string “What time do I have to be there? What’s the address?”. Include a main program that reads
a string from the user, capitalizes it using your function, and displays the result.









