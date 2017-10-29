
Problem Set 6 - Encryption & Decryption
=======================================

This problem set has two parts. The encryption part is graded and deals with encryption, a very important concept in computer science. The recursion part is an ungraded set of problems designed to help you practice writing recursive functions. We will not provide graders for this recursion part but urge you to practice coding and testing these problems on your own machine.

Download and save code_ProblemSet6.zip. This zip archive includes the following files: 

ps6_encryption.py: 
    Skeleton code you'll fill in for the encryption part the problem set.

words.txt:
    A list of English words

ps6_pseudo.txt:
    Pseudocode for Problem 2. We urge you to not look at this file until you reach Problem 2 and read the instructions contained there.

story.txt:
    An encoded story

ps6_recursion.py: 
    Skeleton code for the practice recursion problems.

Load ps6_encryption.py into a Python environment without making any modifications to it, in order to ensure that everything is set up correctly. The code that we have given you loads a list of words from a file. If everything is okay, after a small delay, you should see the following printed out:
    Loading word list from file...
    55909 words loaded. 

The line assert applyShift(s, bestShift) == 'Hello, world!' will also print out an assertion error, and that is ok, because you haven't implemented the functions yet. If you see an IOError instead (e.g., No such file or directory), you should change the value of the WORDLIST_FILENAME constant (defined near the top of the file) to the complete pathname for the file words.txt (this will vary based on where you saved the file).

The file ps6_encryption.py has a few functions already implemented that you can use while writing up your solution. You can ignore the code between the following comments, though you should read and understand everything else:

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
. . .
# (end of helper code)
# -----------------------------------  


HAIL CAESAR!
------------
Encryption is the process of obscuring information to make it unreadable without special knowledge. For centuries, people have devised schemes to encrypt messages - some better than others - but the advent of the computer and the Internet revolutionized the field. These days, it's hard not to encounter some sort of encryption, whether you are buying something online or logging into a shared computer system. Encryption lets you share information with other trusted people, without fear of disclosure.

A cipher is an algorithm for performing encryption (and the reverse, decryption). The original information is called plaintext. After it is encrypted, it is called ciphertext. The ciphertext message contains all the information of the plaintext message, but it is not in a format readable by a human or computer without the proper mechanism to decrypt it; it should resemble random gibberish to those for whom it is not intended.

A cipher usually depends on a piece of auxiliary information, called a key. The key is incorporated into the encryption process; the same plaintext encrypted with two different keys should have two different ciphertexts. Without the key, it should be difficult to decrypt the resulting ciphertext into readable plaintext.

This assignment will deal with a well-known (though not very secure) encryption method called the Caesar cipher. In this problem set you will need to devise your own algorithms and will practice using recursion to solve a non-trivial problem.

CAESAR CIPHER

The basic idea of the Caesar cipher is that you pick an integer for a key, and shift every letter of your message by the key. For example, if your message was "happy" and your key was 3, "h" becomes "k", "a" becomes "d", and so on, because we are shifting every letter three spots to the right. Here is what the whole alphabet looks like shifted three spots to the right:

 
Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
 3-shift:  d e f g h i j k l m n o p q r s t u v w x y z a b c
Using the above key, we can quickly translate the message "happy" to "kdssb" (note how the 3-shifted alphabet wraps around at the end, so x -> a, y -> b, and z -> c).

Note!! We are using the English alphabet for this problem - that is, the following letters in the following order:

>>> import string
>>> print string.ascii_lowercase
abcdefghijklmnopqrstuvwxyz
In this problem, we will use a variant of the standard Caesar cipher where we will treat upper and lower case letters separately, so upper case letters will always be mapped to upper case letters, and lower case letters will always be mapped to lower case letters. Thus, if "a" maps to "c", "A" will map to "C". Characters such as the space character, commas, periods, exclamation points, etc will not be encrypted by this cipher - basically, all the characters within string.punctuation, plus the space (' ') and all numerical characters (0 - 9).

To learn more about the Caesar cipher, check out this Wikipedia article.

WRAPPER FUNCTIONS

Now that you are ready to start coding, you can look carefully at the code skeletons that we have provided for you. Do not be intimidated by the length of the function specifications we provide with the supplied code! Many of these problems rely on wrapper functions, an extremely useful coding concept that, when implemented correctly, often requires very little additional code. The idea of wrapper functions here is that the functions visible to a user take as arguments simple inputs, and then supply these arguments - plus other information - to functions visible only within the implementation to perform the computation.

Read the Wikipedia article on wrapper functions (http://en.wikipedia.org/wiki/Wrapper_function) for more information.


Problem 1: Encryption (Buildcoder)
----------------------------------
You'll now write a program to encrypt plaintext into ciphertext using the Caesar cipher.

# Upper & Lower Case Letters
Be sure that your dictionary includes both lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".
If you are unfamiliar with the ordering or characters of the English alphabet, we will be following the letter ordering displayed by string.ascii_lowercase and string.ascii_uppercase:
>>> import string
>>> print string.ascii_lowercase
abcdefghijklmnopqrstuvwxyz
>>> print string.ascii_uppercase
ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Characters to Ignore
A reminder from the introduction page - Characters such as the space character, commas, periods, exclamation points, etc will not be encrypted by this cipher - basically, all the characters within string.punctuation, plus the space (' ') and all numerical characters (0 - 9) found in string.digits.

# Test Cases

buildCoder(3)
{'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'B', 'X': 'A', 'Z': 'C', 'a': 'd', 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 'v': 'y', 'y': 'b', 'x': 'a', 'z': 'c'}
buildCoder(9)
{'A': 'J', 'C': 'L', 'B': 'K', 'E': 'N', 'D': 'M', 'G': 'P', 'F': 'O', 'I': 'R', 'H': 'Q', 'K': 'T', 'J': 'S', 'M': 'V', 'L': 'U', 'O': 'X', 'N': 'W', 'Q': 'Z', 'P': 'Y', 'S': 'B', 'R': 'A', 'U': 'D', 'T': 'C', 'W': 'F', 'V': 'E', 'Y': 'H', 'X': 'G', 'Z': 'I', 'a': 'j', 'c': 'l', 'b': 'k', 'e': 'n', 'd': 'm', 'g': 'p', 'f': 'o', 'i': 'r', 'h': 'q', 'k': 't', 'j': 's', 'm': 'v', 'l': 'u', 'o': 'x', 'n': 'w', 'q': 'z', 'p': 'y', 's': 'b', 'r': 'a', 'u': 'd', 't': 'c', 'w': 'f', 'v': 'e', 'y': 'h', 'x': 'g', 'z': 'i'}

```
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 

```

Problem 1 - Encryption(Apply Coder)
-----------------------------------
Next, define the function applyCoder, which applies a coder to a string of text.

Test Cases

>>> applyCoder("Hello, world!", buildCoder(3))
'Khoor, zruog!'
>>> applyCoder("Khoor, zruog!", buildCoder(23))
'Hello, world!'

```
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
```


Problem 1 - Encryption (AppluShift)
------------------------------------
Once you have written buildCoder and applyCoder, you should be able to use them to encode strings.

Test Cases

>>> applyShift('This is a test.', 8)
'Bpqa qa i bmab.'
>>> applyShift('Bpqa qa i bmab.', 18)
'This is a test.'

```
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
```

PseudoCode
----------
PSEUDOCODE

If you recall from Problem Set 4, creating pseudocode is the process of writing out the algorithm/solution in a form that is like code, but is not quite code. Pseudocode is language independent, uses plain English (or your native language), and is readily understandable. Algorithm related articles on Wikipedia (https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Computer_science/Manual_of_style#Algorithms) often use pseudocode to explain the algorithm.

Think of writing pseudocode like you would explain it to another person -- it doesn't generally have to conform to any particular syntax as long as what's happening is clear to the grader. - Paul McMillan

Read more about the whats and whys of pseudocode here.

In order to help you solve the following problems correctly, we strongly suggest that you try writing pseudocode for your solutions to Problem 2 before starting to code. To do this, read Problem 2, and think about high level algorithms to solve the problem, and write down the steps in your algorithms.

After you have made an honest attempt at writing your own pseudocode, then open ps6_pseudo.txt to compare your pseudocode to ours. We strongly encourage you to write your own pseudocode for this problem before looking at the staff's pseudocode. To write the Python code that actually solves Problem 2, feel free to use the staff's pseudocode as a reference, or your own if you believe that it is correct.


Problem 2 - Decryption (Findbestshift)
--------------------------------------
Your friend, who is also taking 6.00.1x, is really excited about the program she wrote for Problem 1 of this problem set. She sends you emails, but they're all encrypted with the Caesar cipher!

If you know which shift key she is using, then decrypting her message is an easy task. If the string message is the encrypted message and k is the shift key she is using, then calling applyShift(message, 26-k) returns her original message. Do you see why?

The problem is, you don't know which shift key she is using. The good news is, you know your friend only speaks and writes English words. So if you can write a program to find the decoding that produces the maximum number of real English words, you can probably find the right decoding (there's always a chance that the shift may not be unique. Accounting for this would use statistical methods that we won't require of you.)

PSEUDOCODE

Right now, you should take time to write some pseudocode! Think about an algorithm you could use to solve this problem and write the steps down. Then, you can verify your algorithm with the supplied pseudocode in ps6_pseudo.txt before coding.

After you've done writing and checking your pseudocode, implement findBestShift(). This function takes a wordList and a sample of encrypted text and attempts to find the shift that encoded the text. A simple indication of whether or not the correct shift has been found is if most of the words obtained after a shift are valid words. Note that this only means that most of the words obtained are actual words. It is possible to have a message that can be decoded by two separate shifts into different sets of words. While there are various strategies for deciding between ambiguous decryptions, for this problem we are only looking for a simple solution.

To assist you in solving this problem, we have provided a helper function, isWord(wordList, word). This simply determines if word is a valid word according to the wordList. This function ignores capitalization and punctuation.

# Using string split
You may find the function string.split useful for dividing the text up into words.
>>> 'Hello world!'.split('o')
['Hell', ' w', 'rld!']
>>> '6.00.1x is pretty fun'.split(' ')
['6.00.1x', 'is', 'pretty', 'fun']

# Test Cases
>>> s = applyShift('Hello, world!', 8)
>>> s
'Pmttw, ewztl!'
>>> findBestShift(wordList, s)
18
>>> applyShift(s, 18)
'Hello, world!'

```
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
```

Problem 2 - Decryption (decryptstory)
-------------------------------------
Now that you have all the pieces to the puzzle, please use them to decode the file story.txt. In the skeleton file, you will see a method getStoryString() that will return the encrypted version of the story. Fill in the following function; it should create the wordList, obtain the story, and then decrypt the story. Be sure you've read through the whole file to see what helper functions we've defined for you that may assist you in these tasks! This function will be only a few lines of code (our solution does it in 4 lines).

```
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
```