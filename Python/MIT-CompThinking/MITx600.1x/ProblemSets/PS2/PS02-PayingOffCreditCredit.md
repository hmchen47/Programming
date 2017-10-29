Problem Set 02 - Paying Off Credit Credit
=========================================

Each month, a credit card statement will come with the option for you to pay a minimum amount of your charge, usually 2% of the balance due. However, the credit card company earns money by charging interest on the balance that you don't pay. So even if you pay credit card payments on time, interest is still accruing on the outstanding balance.

Say you've made a $5,000 purchase on a credit card with an 18% annual interest rate and a 2% minimum monthly payment rate. If you only pay the minimum monthly amount for a year, how much is the remaining balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will call b0 (b for balance; subscript 0 to indicate this is the balance at month 0).

Any payment you make during that month is deducted from the balance. Let's call the payment you make in month 0, p_0. Thus, your unpaid balance for month 0, ub0, is equal to b_0−p_0.

    ub_0 = b_0 − p_0

At the beginning of month 1, the credit card company will charge you interest on your unpaid balance. So if your annual interest rate is r, then at the beginning of month 1, your new balance is your previous unpaid balance ub0, plus the interest on this unpaid balance for the month. In algebra, this new balance would be

    b_1 = ub_0 + r/12.0 * ub_0

In month 1, we will make another payment, p1. That payment has to cover some of the interest costs, so it does not completely go towards paying off the original charge. The balance at the beginning of month 2, b2, can be calculated by first calculating the unpaid balance after paying p1, then by adding the interest accrued:

    ub_1 = b_1 − p_1
    b_2 = ub_1 + r/12.0 * ub_1

If you choose just to pay off the minimum monthly payment each month, you will see that the compound interest will dramatically reduce your ability to lower your debt.

Let's look at an example. If you've got a $5,000 balance on a credit card with 18% annual interest rate, and the minimum monthly payment is 2% of the current balance, we would have the following repayment schedule if you only pay the minimum payment each month:

Mon | Balance | Minimum Payment  | Unpaid Balance   | Interest
0   | 5000.00 | 100 (=5000*0.02) | 4900 (=5000-100) | 73.50 (=0.18/12.0*4900)
1   | 4973.50 (=4900+73.50) | 99.47 (=4973.50*0.02) | 4874.03 (=4973.50-99.47) | 73.11 (=0.18/12.0*4874.03)
2   | 4947.14 (=4874.03+73.11) | 98.94 (=4947.14*0.02) | 4848.20 (=4947.14-98.94) | 72.72 (=0.18/12.0*4848.20)

You can see that a lot of your payment is going to cover interest, and if you work this through month 12, you will see that after a year, you will have paid $1165.63 and yet you will still owe $4691.11 on what was originally a $5000.00 debt. Pretty depressing!


Problem 1 - Paying The Minimum
------------------------------
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:
    1. balance - the outstanding balance on the credit card
    2. annualInterestRate - annual interest rate as a decimal
    3. monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance, and print to screen something of the format:
    Month: 1
    Minimum monthly payment: 96.0
    Remaining balance: 4784.0

Be sure to print out no more than two decimal digits of accuracy - so print
    Remaining balance: 813.41
instead of
    Remaining balance: 813.4141998135 

Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:
    Total paid: 96.0
    Remaining balance: 4784.0

A summary of the required math is found below:
    Monthly interest rate= (Annual interest rate) / 12.0
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Note that the grading script looks for the order in which each value is printed out. We provide sample test cases below; we suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.
Test Cases to Test Your Code With. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

Test Cases to Test Your Code With. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!
Note: Depending on where you round in this problem, your answers may be off by a few cents in either direction. Do not worry if your solution is within +/- 0.05 of the correct answer.

Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

Test Cases:
                    
    Test Case 1:
    balance = 4213
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
    
    Result Your Code Should Generate:
    -------------------
    Month: 1
    Minimum monthly payment: 168.52
    Remaining balance: 4111.89
    Month: 2
    Minimum monthly payment: 164.48
    Remaining balance: 4013.2
    Month: 3
    Minimum monthly payment: 160.53
    Remaining balance: 3916.89
    Month: 4
    Minimum monthly payment: 156.68
    Remaining balance: 3822.88
    Month: 5
    Minimum monthly payment: 152.92
    Remaining balance: 3731.13
    Month: 6
    Minimum monthly payment: 149.25
    Remaining balance: 3641.58
    Month: 7
    Minimum monthly payment: 145.66
    Remaining balance: 3554.19
    Month: 8
    Minimum monthly payment: 142.17
    Remaining balance: 3468.89
    Month: 9
    Minimum monthly payment: 138.76
    Remaining balance: 3385.63
    Month: 10
    Minimum monthly payment: 135.43
    Remaining balance: 3304.38
    Month: 11
    Minimum monthly payment: 132.18
    Remaining balance: 3225.07
    Month: 12
    Minimum monthly payment: 129.0
    Remaining balance: 3147.67
    Total paid: 1775.55
    Remaining balance: 3147.67

             
    Test Case 2:
    balance = 4842
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
      
    Result Your Code Should Generate:
    -------------------
    Month: 1
    Minimum monthly payment: 193.68
    Remaining balance: 4725.79
    Month: 2
    Minimum monthly payment: 189.03
    Remaining balance: 4612.37
    Month: 3
    Minimum monthly payment: 184.49
    Remaining balance: 4501.68
    Month: 4
    Minimum monthly payment: 180.07
    Remaining balance: 4393.64
    Month: 5
    Minimum monthly payment: 175.75
    Remaining balance: 4288.19
    Month: 6
    Minimum monthly payment: 171.53
    Remaining balance: 4185.27
    Month: 7
    Minimum monthly payment: 167.41
    Remaining balance: 4084.83
    Month: 8
    Minimum monthly payment: 163.39
    Remaining balance: 3986.79
    Month: 9
    Minimum monthly payment: 159.47
    Remaining balance: 3891.11
    Month: 10
    Minimum monthly payment: 155.64
    Remaining balance: 3797.72
    Month: 11
    Minimum monthly payment: 151.91
    Remaining balance: 3706.57
    Month: 12
    Minimum monthly payment: 148.26
    Remaining balance: 3617.62
    Total paid: 2040.64
    Remaining balance: 3617.62

The code you paste into the following box should not specify the values for the variables balance, annualInterestRate, or monthlyPaymentRate - our test code will define those values before testing your submission.

# Only two decimal of accuracy
Use the round function!

# How to think about this problem
To help you get started, here is a rough outline of the stages you should probably follow in writing your code:
    For each month:
        Compute the monthly payment, based on the previous month’s balance.
        Update the outstanding balance by removing the payment, then charging interest on the result.
        Output the month, the minimum monthly payment and the remaining balance.
        Keep track of the total amount of paid over all the past months so far.
    Print out the result statement with the total amount paid and the remaining balance.

Use these ideas to guide the creation of your code.

# Only hit "Chek" once per submission .  We are unable to give you more than 30 checks
Our automatic grader may take a few minutes to respond with feedback. If you hit "Check" multiple times, you will lose a check for every press of the button.

If you're unfamiliar with how our autograder works, first try out one of the infinite check problems in the Functions lecture sequence.

Please be judicious with your checks, as we are unable to give you more than 30 checks. However this should be more than sufficient: if you do your code development in your local environment, and ensure you can pass our test cases, you should not require more than a few checks once you paste your working, tested code into our code box.





Problem 2 - Paying Debet Off in a Year
--------------------------------------
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:
    1. balance - the outstanding balance on the credit card
    2. annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
    Lowest Payment: 180 

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:
    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Test Cases to Test Your Code With. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

Test Cases:

    Test Case 1:
    balance = 3329
    annualInterestRate = 0.2
    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 310
             
    Test Case 2:
    balance = 4773
    annualInterestRate = 0.2
    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 440
              
    Test Case 3:
    balance = 3926
    annualInterestRate = 0.2
    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 360

The code you paste into the following box should not specify the values for the variables balance or annualInterestRate - our test code will define those values before testing your submission. 

# How to think about this problem
* Start with $10 payments per month and calculate whether the balance will be paid off in a year this way (be sure to take into account the interest accrued each month).
* If $10 monthly payments are insufficient to pay off the debt within a year, increase the monthly payment by $10 and repeat.

# A way of structuring your code
* If you are struggling with how to structure your code, think about the following:
    - Given an initial balance, what code would compute the balance at the end of the year?
    - Now imagine that we try our initial balance with a monthly payment of $10. If there is a balance remaining at the end of the year, how could we write code that would reset the balance to the initial balance, increase the payment by $10, and try again (using the same code!) to compute the balance at the end of the year, to see if this new payment value is large enough.
    - I'm still confused! - A good way to implement this problem will be to use a loop structure. You may want to refresh your understanding of while loops. Think hard about how the program will know when it has found a good minimum monthly payment value - when a good value is found, the loop can terminate. 
* Be careful - you don't want to overwrite the original value of balance. You'll need to save that value somehow for later reference!



Problem 3 - Using Bisection Search to Make the Program Faster
-------------------------------------------------------------
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

The following variables contain values as described below:
    1. balance - the outstanding balance on the credit card
    2. annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

In short:
    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly payment lower bound = Balance / 12
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search [https://en.wikipedia.org/wiki/Bisection_method]) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

Note that if you do not use bisection search, your code will not run - your code only has 30 seconds to run on our servers.

Test Cases to Test Your Code With. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

Note: The automated tests are leinient - if your answers are off by a few cents in either direction, your code is OK.

Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

Test Cases:

    Test Case 1:
    balance = 320000
    annualInterestRate = 0.2
    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 29157.09
              
    Test Case 2:
    balance = 999999
    annualInterestRate = 0.18
    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 90325.03

The code you paste into the following box should not specify the values for the variables balance or annualInterestRate - our test code will define those values before testing your submission. 

