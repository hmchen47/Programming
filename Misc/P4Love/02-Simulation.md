# Chapter 2: Predicting a US Presidential Election with Monte Carlo Simulation

<video src="https://youtu.be/LF2WwaFrFa8" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="subtitle" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


## 2.1 Polling data and Statistics

+ 538 and NY Times Projections in 2016
  + Note: Projections fluctuate but have same shape

+ Polling data inherently volatile
  + __Margin of Error:__ percentage value on either side of polling percentage within which we have confidence in the poll (here it's 4%)

+ The US Presidential election uses an "electoral college"

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://en.wikipedia.org/wiki/2016_United_States_presidential_election" ismap target="_blank">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/ElectoralCollege2016.svg/696px-ElectoralCollege2016.svg.png" style="margin: 0.1em;" alt="Presidential election results map. Red denotes states won by Trump and blue denotes those won by Clinton. Numbers indicate the number of electoral votes allocated to each state plus the District of Columbia, and show for whom they were cast. Altogether, Trump garnered 304 electoral votes and Clinton 227, as seven faithless electors, two pledged to Trump and five pledged to Clinton, voted for other persons." title="Presidential election results map" width=350>
    </a>
  </div>

+ Idea: simulate election many times from state polling data

+ Monte Carlo simulation everywhere
  + __Monte Carlo Simulation:__ repeatedly running random simulations to obtain an approximate result
  + eg, stock price, weather forecast, sporting events, 


## 2.2 Craps and the House Edge

+ A simple example compute "house edge"
  + __House edge:__ average result that casino wins (per dollar wagered) on a game of change over time
  + Answer: simulate computer to "play" the game $n$ times, and divide the amount lost by $n$

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://www.blackjackchamp.com/casino-news/22092-blackjack-buy-secondhand-car/" ismap target="_blank">
      <img src="https://bjcnew.gamblingzion.com/uploads/2014/03/blackjack-strategy-chart-310314.jpg" style="margin: 0.1em;" alt="In any game of blackjack the objective is simple and it’s always the same. Your hand consists of two cards which are dealt face up and on show to everyone at the table; with these you try to get to 21 without going over. However, more importantly, you must also beat the dealer’s hand; one card of which will be dealt face up and be on show to players at first, with the second being revealed after all players have requested any additional cards, or placed further bets." title="Advanced Blackjack Strategy Table" width=450>
    </a>
  </div>

+ Binary Game
  + __Binary Game:__ a game with two outcomes with equal and opposite payout (e.g., the player wins \$1 or loss \$1)
  + blackjack isn't binary because it has payouts that depends on the outcome, and it is hard to simulate because the player can make decisions.

+ Crap: a binary game - The rules of craps:
  + roll two fair dice
    + if the dice show 7 or 11, you win!
    + if the dice show 2, 3, or 12, you loss :-(
    + if the dice show some other number x, then you must continue rolling ...
  + on these continued rolls
    + if you roll x, you win!
    + if you roll a 7, you lose :-(
    + if you roll any other number, then you keep rolling until there's a result
  + pseudocode for house edge

    ```js
    ComputeHouseEdge(numTrials)
      count = 0
      for trial = 1 to numTrials
        outcome = PlayCrapsOnce()
        if outcome = true
          count = count + 1
        else
          count = count - 1
      return count/numTrials
    ```

  + STOP: where is the randomization hiding?
    + Ans: within the `PlayCrapsOnce()` subroutine ...
  + Note: this could b used to compute house edge of any binary game by replacing the `PlayCrapsOnce()`
  + Exercise: writing `PlayCrapsOnce()`. you may assume a `SumTwoDice()` subroutine.
  + pseudocode

    ```js
    PlayCrapsOnce()
      firstRoll = SumTwoDice
      if firstRoll = 2, 3, or 12
        return false (player loses)
      else if firstRoll = 7 or 11
        return true (player wins)
      else // other numbers
        while true
          newRoll = SunTwoDice()
          if newRoll = firstRoll
            return true (player wins)
          else if newRoll = 7
            return false (player loses)
    ```

  + STOP: isn't this an infinite loop?
    + theory yes, in practice, no

+ Summary
  + main goal: simulate a presidential election
  + more modest goal: program a computer to roll dice


## 2.3 Pitfalls of (Pseudo) Random Number Generation

+ Simple problem: generating digits
  + STOP: quickly think up a few random digits between 0 an d9 in you head
  + isn't it weird that you can do this without really thinking about it?
  + what evolutionary purpose might such a ability sever?
  + state of the art for random number generation in the 940s: a book with a million digits

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://blogs.agu.org/georneys/2011/02/20/a-million-random-digits/" ismap target="_blank">
      <img src="http://2.bp.blogspot.com/-dY5Tpn-20qw/TWHn_WPZqOI/AAAAAAAAAjk/oZ0_q94URUk/s400/Random_Digits_1.png" style="margin: 0.1em;" alt="First page of random digits in “A Million Random Digits” book" title="First page of random digits in “A Million Random Digits” book" width=350>
    </a>
  </div>

+ Middle-Square PRNG method
  + The ENIAC computer: missile target system
  + __Pseudorandom Number Generator (PRNG):__ a _deterministic_ (controlled) way of generating numbers, starting w/ a _seed_, to mimic randomness
  + von Neumann's middle-square idea (see diagram)
    + there must be a faster way of doing this using our "supercomputer"!
    + using seed (6 digits),  then square it and taking the middle 6 digits as output
  + STOP: is is a good PRNG?

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://en.wikipedia.org/wiki/Middle-square_method" ismap target="_blank">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Middle-square_method.svg/500px-Middle-square_method.svg.png" style="margin: 0.1em;" alt="One iteration of the middle-square method, showing a six digit seed, which is then squared, and the resulting value has its middle six digits as the output value (and also as the next seed for the sequence)." title="One iteration of the middle-square method" width=150>
    </a>
  </div>

  + Exercise: start with the four-digit seed of 1600.  what are the first few numbers generated?
    + Ans: No <br/>$1600 \to 02560000 \;(5600) \to 12960000 \;(9600) \to 92160000 \;(1600) \to\cdots$ <br/> $3792 \to 14379264 \;(3792) \to 14379264 \;(3792) \to \cdots$
  + Anyone who considers arithmetical random digits is, of course, in a state of sin. For, as has beed pointed out several times, there is no such thing as a rnadom number. -- John von Neumann

+ Lagged Fibonacci generators
  + __Fibonacci Number generator:__ for some fixed parameters $m$, take as the $n$-th number $F_n$

    \[ F_n = (F_{n-1} + F_{n-2}) \;\text{mod } m \]

    + mod: is the same as the remainder (%)
  + eg,

    \[ F_{32} = (F_{31} + F_{30}) \;\text{mod } 1,000,000 = (832040 + 1346269) \;\text{mod } 1,000,000 = 178309 \]

  + STOP: do you see any issues with this RPNG?
    + Ans: if $F_{n-1} = 100$, and $F_{n-2} = 200$, what is $F_n$?
  + Go's native RPNG using a lagged Fibonacci generator

    \[ F_n = (F_{n-273} + F_{n-607}) \;\text{mod } 2^{31} \]

  + there is a more sophisticated PRNG in "crypto/rand"

+ Properties of a "Good"  PRNG
  + __level 1:__ different sequences generated by the PRNG should likely be different from each other
  + __level 2:__ the PRNG should generate numbers with teh same properties of a sequence of truly random numbers (eg, how often a number repeats)
  + __level 3:__ a hacker shouldn't be able to use the sequence of numbers to guess any _future_ numbers
  + __level 4:__ a hacker shouldn't be able to use the sequence numbers to guess any _previous_ numbers

+ [Meet Alex, the Russian Casino Hacker Who Makes Millions Targeting Slot Machines](https://www.wired.com/story/meet-alex-the-russian-casino-hacker-who-makes-millions-targeting-slot-machines/)
  + A mathematician-turned-criminal unleashes his agents on casinos around the world. But there’s money in the extortion racket, too.
  + They then send timing data to a custom app on an agent’s phone; this data causes the phones to vibrate a split second before the agent should press the “Spin” button.


## 2.4 Simulating Craps

+ Three common built-in functions<br/>
  most languages have PRNG package that includes following functions
  + `Int()`: return "random integer
  + `Intn()`: takes an integer $n$ and returns a "random" integer btw $0$ and $n-1$, inclusively
  + `Float()`: returns "random" decimal in the range $[0, 1)$
  + STOP: which of these functions should used to simulated rolling a die?

+ Simulating a die roll
  + Idea 1: `Float()`

    ```js
    RollDie()
      roll = Float()
      if roll < 1/6
        return 1
      else if roll < 2/6
        return 2
      else if roll < 3/6
        return 3
      else if roll < 4/6
        return 4
      else if roll < 5/6
        return 5

      return 6
    ```

  + Idea 2: `Intn()`

    ```js
    RollDie()
      roll = Intn(6)
      return roll+1
    ```
  
  + Idea 3: `Int()`

    ```js
    RollDie()
      roll = Int()
      return Remainder(roll, 6) + 1
    ```

+ Exercise: write a function `SunTwoDice()` that takes no parameters and returns the sum of two rolled fair dice

  ```js
  SumTwoDice()
    roll = Float()
    if roll < 1/36 
      return 1
    else if roll < 3/36
      return 2
    else if roll < 6/36
    ...

  // a better approach by using modularity  
  SumTwoDice()
    return RollDie() + RollDie()
  ```

+ Exercise: write a unction `SumMultipleDice()` that takes an integer $n$ and return the sum of $n$ dice

  ```js
  SumMultipleDice()
    s = 0
    for n trials
      s = s + RollDie()
    return s
  ```

+ Craps Simulator

  ```js
  PlayCrapsOnce()
    firstRoll = SumTwoDice()
    if firstRoll = 2, 3, or 12
      return false (player loses)
    else if firstRoll = 7 or 11
      return true (player wins)
    else
      while true
        newRoll = SumTwoDice()
        if newRoll = firstRoll
          return true (player wins)
        else if newRoll = 7
          return false (player loses)
  ```




