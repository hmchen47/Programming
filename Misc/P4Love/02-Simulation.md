# Chapter 2: Predicting a US Presidential Election with Monte Carlo Simulation

<video src="https://youtu.be/LF2WwaFrFa8" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="subtitle" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


## 2.1 An Introduction to Monte Carlo Simulation

+ 538 and NY Times Projections in 2016
  + Election projection results from FiveThirtyEight(top) and The New York Times (bottom) from June 2016 to November 8, 2016, the day of the US presidential election.
  + The blue line shows Clinton’s forecast percentage chance of winning, and the red line shows Trump’s forecast percentage chance of winning (the yellow line in the top plot corresponds to Libertarian Party candidate Gary Johnson, who was not included in the Times forecast).
  + Note that the projections disagree about the likelihood of a Clinton victory at any given time, but they indicate the same trend of this likelihood rising and falling over time.
  + Sources:
    + [projects.fivethirtyeight.com/2016-election-forecast](https://projects.fivethirtyeight.com/2016-election-forecast/)
    + [NY Times presidential polls forecast](https://www.nytimes.com/interactive/2016/upshot/presidential-polls-forecast.html?mtrref=www.google.com&gwh=98BBC964A93A5930F7E7DE8961D883F8&gwt=pay&assetType=REGIWALL)

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://compeau.cbd.cmu.edu/programming-for-lovers/chapter-2-forecasting-a-presidential-election-with-monte-carlo-simulation/" ismap target="_blank">
      <img src="http://compeau.cbd.cmu.edu/wp-content/uploads/2019/11/percentages_combined-768x589.jpg" style="margin: 0.1em;" alt="Election projection results from FiveThirtyEight(top) and The New York Times (bottom) from June 2016 to November 8, 2016, the day of the US presidential election. The blue line shows Clinton’s forecast percentage chance of winning, and the red line shows Trump’s forecast percentage chance of winning (the yellow line in the top plot corresponds to Libertarian Party candidate Gary Johnson, who was not included in the Times forecast). Note that the projections disagree about the likelihood of a Clinton victory at any given time, but they indicate the same trend of this likelihood rising and falling over time. Sources: https://projects.fivethirtyeight.com/2016-election-forecast/, and https://www.nytimes.com/interactive/2016/upshot/presidential-polls-forecast.html?mtrref=www.google.com&gwh=98BBC964A93A5930F7E7DE8961D883F8&gwt=pay&assetType=REGIWALL" title="Election projection results from FiveThirtyEight(top) and The New York Times (bottom) from June 2016 to November 8, 2016, the day of the US presidential election" width=350>
    </a>
  </div>

+ Polling data inherently volatile
  + __Margin of Error:__ percentage value on either side of polling percentage within which we have confidence in the poll (here it's 4%)

+ The US Presidential election uses an "electoral college"

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://en.wikipedia.org/wiki/2016_United_States_presidential_election" ismap target="_blank">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/ElectoralCollege2016.svg/696px-ElectoralCollege2016.svg.png" style="margin: 0.1em;" alt="Presidential election results map. Red denotes states won by Trump and blue denotes those won by Clinton. Numbers indicate the number of electoral votes allocated to each state plus the District of Columbia, and show for whom they were cast. Altogether, Trump garnered 304 electoral votes and Clinton 227, as seven faithless electors, two pledged to Trump and five pledged to Clinton, voted for other persons." title="Presidential election results map" width=350>
    </a>
  </div>

+ Idea: simulate election many times from state polling data
  + A FiveThirtyEight figure showing the variability in the number of electoral votes won by Clinton and Trump across thousands of simulations.
  + The height of each peak represents the percentage of simulations in which a given candidate won the corresponding number of electoral votes in a simulation.
  + The charts are mirror images of each other because in a given election simulation, there are always a fixed number (538) of electoral votes to be divided between the two candidates.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-2-forecasting-a-presidential-election-with-monte-carlo-simulation-53e79ad8c430" ismap target="_blank">
      <img src="https://miro.medium.com/max/3666/1*fqD3d3yALRHILaVoovdVaw.jpeg" style="margin: 0.1em;" alt="A FiveThirtyEight figure showing the variability in the number of electoral votes won by Clinton and Trump across thousands of simulations. The height of each peak represents the percentage of simulations in which a given candidate won the corresponding number of electoral votes in a simulation. The charts are mirror images of each other because in a given election simulation, there are always a fixed number (538) of electoral votes to be divided between the two candidates." title="The variability in the number of electoral votes won by Clinton and Trump across thousands of simulations" width=450>
    </a>
  </div>

+ Monte Carlo simulation everywhere
  + __Monte Carlo Simulation:__ repeatedly running random simulations to obtain an approximate result
  + eg, stock price, weather forecast, sporting events
  + Pennsylvania’s 7th Congressional District over six decades (left diagram)
  + The 2016 (left) and 2018 (right) Congressional district maps of Pennsylvania. (right diagram)
    + The 2018 district map was drawn by the Supreme Court of Pennsylvania, which ruled that the 2016 map had been unfairly drawn to benefit Republicans.
    + Pivotal testimony was given by a Carnegie Mellon mathematics professor, who ran trillions of random simulations to show that the map on the left was more unfair than practically every map that had been randomly generated.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-2-forecasting-a-presidential-election-with-monte-carlo-simulation-53e79ad8c430" ismap target="_blank">
      <img src="https://miro.medium.com/max/2444/1*WNS0r-BURhiqzlAzeUJgAg.jpeg" style="margin: 0.1em;" alt="Pennsylvania’s 7th Congressional District over six decades, as it changed from a relatively convex shape to a barely contiguous region that has been likened to Goofy kicking Donald Duck." title="Pennsylvania’s 7th Congressional District over six decades" height=150>
      <img src="https://miro.medium.com/max/4721/1*druH9zifZzYRI4cLqITZGQ.jpeg" style="margin: 0.1em;" alt="The 2016 (left) and 2018 (right) Congressional district maps of Pennsylvania. The 2018 district map was drawn by the Supreme Court of Pennsylvania, which ruled that the 2016 map had been unfairly drawn to benefit Republicans. Pivotal testimony was given by a Carnegie Mellon mathematics professor, who ran trillions of random simulations to show that the map on the left was more unfair than practically every map that had been randomly generated." title="The 2016 (left) and 2018 (right) Congressional district maps of Pennsylvania." height=150>
    </a>
  </div>


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

### 2.3.1 Von Neumann’s Middle-Square Pseudorandom Number Generator

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


### 2.3.2 Lagged Fibonacci Generators

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

### 2.4.1 Rolling a single die

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
  
  + STOP: stay that we have a weighted die that produces each of 1, 3, 4, and 5 with probability 1/10, and that produces each of 2 and 6 with probability 3/10.  Write pseudocode for a `RollWeightedDie` function that models this weighted die.

+ Exercise: write a function `SumTwoDice()` that takes no parameters and returns the sum of two rolled fair dice

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


## 2.5 Simulating a Presidential Election

+ Returning to election simulator

  ```js
  SimulateMultipleElection(pollingData, numTrials, marginOfError)
    winCount1 = 0
    winCount2 = 0
    tieCount = 0

    for trial = 1 to numTrials
      collegeVotes1, collegeVotes2 = SimulateOneElection(pollingData, marginOfError)
      if collegeVotes1 > collegeVotes2
        winCount1 = winCount1 + 1
      else if collegeVotes2 > collegeVotes1
        winCount2 = winCount2 + 1
      else
        tieCount = tieCount + 1
    probability1 = winCount1/numTrials
    probability2 = winCount2/numTrials
    probabilityTie = tieCount/numTrials

    return probability1, probability2, probabilityTie
  ```

  + Note: Haven't told anything about pollingData!

+ Using two maps for election data
  + Pools & ElectoralVotes

    <table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=50%>
      <thead>
      <tr>
        <th colspan="2" style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">electoralVotes</th>
        <th colspan="2" style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">pools</th>
      </tr>
      <tr>
        <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">State</th>
        <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Votes</th>
        <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">State</th>
        <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Percentage</th>
      </tr>
      </thead>
      <tbody>
      <tr> <td>"California"</td> <td>55</td> <td>"California"</td> <td>62.2%</td> </tr>
      <tr> <td>"Texas"</td> <td>38</td> <td>"Texas"</td> <td>45.6%</td> </tr>
      <tr> <td>"Florida"</td> <td>29</td> <td>"Florida"</td> <td>49.1%</td> </tr>
      <tr> <td>"New York"</td> <td>29</td> <td>"New York"</td> <td>57.9%</td> </tr>
      <tr> <td>"Illinois"</td> <td>20</td> <td>"Illinois"</td> <td>64.0%</td> </tr>
      <tr> <td>"Pennsylvania"</td> <td>20</td> <td>"Pennsylvania"</td> <td>53.3%</td> </tr>
      <tr> <td>"Ohio"</td> <td>18</td> <td>"Ohio"</td> <td>49.9%</td> </tr>
      </tbody>
    </table>

  + Simulating a single election

    ```js
    SimulateOneElection(polls, electoralVotes, marginOfError)
      collegeVotes1 = 0
      collegeVotes2 = 0
      for key in pools
        poll = polls[state]
        votes = electoralVotes[state]
        adjustedPoll = AddNoise(poll, marginOfError)
        if adjustedPoll >= 0.5
          collegeVotes1 = collegeVotes1 + votes
        else
          collegeVotes2 = collegeVotes2 + votes
      return collegeVotes1, collegeVotes2
    ```

  + just need to fill in the details of `AddNoise`, where the randomization is lurking
  + STOP: how could we implement `AddNoise`?

+ Ideal for `AddNoise()`
  + generating a random number uniformly between `-marginOfError` and `+marginOfError`

    ```js
    AddNoise(pool, marginOfError)
      x = random decimal number in [0, 1]
      x = 2 * x               // in [0, 2]
      x = x - 1               // in [-1, 1]
      x = x * marginOfError   // now it's in range
      return x + poll
    ```

  + STOP: why is this not an ideal model?

+ Standard Normal distribution
  + __Standard Normal Distribution:__ a "bell-shaped" distribution with infinitely-extending "tails"
  + height of graph at position x indicates relative likelihood of generating decimal number x
  + Note: languages also have a `NormalFloat()` function returning number from standard normal distribution

    <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
      <a href="https://doughtrading.squarespace.com/blog/understanding-standard-deviation" ismap target="_blank">
        <img src="https://images.squarespace-cdn.com/content/v1/53e4e1bbe4b08bfde27b5214/1444162403849-7OWK6SR12CJF8U4X779I/ke17ZwdGBToddI8pDm48kBAn57fvxhJmgXL6GZy1xhUUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYy7Mythp_T-mtop-vrsUOmeInPi9iDjx9w8K4ZfjXt2dsXMtqy5rx4mcmbzj6URbFz6p6kzYKQ5yPdvVFehL9j1CjLISwBs8eEdxAxTptZAUg/probability-distribution-standard-deviation?format=1500w" style="margin: 0.1em;" alt="A normal distribution graph always has the same general shape (that’s why they call it a bell curve). The standard deviation of a probability distribution graph tells us how likely a certain percentage price change is depending on the volatility of the stock or index. Values within one standard deviation of the mean value always represent 68.2% of the values, but how far the width of the graph expands to encompass the 68.2% of values changes with the volatility. If the volatility is higher, the graph’s standard deviation will be larger to encompass all 68.2% of values." title="The standard normal density function" width=550>
      </a>
    </div>


## 2.6 Implementing Our Work

+ Demo file
  + [Craps simulation](src/GoP4L/craps.go)
  + [Election Simulation](src/GoP4L/election.go)
  + [IP and parsing](src/GoP4L/io.go)


## 2.7 Reflecting on the Natural of (Election) Simulations

+ Evaluation on simulations
  + is our simulation any good?
  + Some results

    |   | Candidate 1 (Clinton) | Candidate 2 (Trump) | Tie |
    |---:|:--------------------:|:-------------------:|:---:|
    | Early Polls | 98.7% | 1.2% | 0.1% |
    | Convention Pools | 99.3% | 0.6% | 0.1% |
    | Debate Pools | 99.6% | 0.4% | 0.0% |

  + STOP: does this look like the results of major media election simulators?

+ What might real simulators do that we didn't?
  + Top diagram: 538 simulation
  + bottom diagram: NY Times
  + not all pools are made alike: different media having different results

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://compeau.cbd.cmu.edu/programming-for-lovers/chapter-2-forecasting-a-presidential-election-with-monte-carlo-simulation/" ismap target="_blank">
      <img src="http://compeau.cbd.cmu.edu/wp-content/uploads/2019/11/percentages_combined-768x589.jpg" style="margin: 0.1em;" alt="Election projection results from FiveThirtyEight(top) and The New York Times (bottom) from June 2016 to November 8, 2016, the day of the US presidential election. The blue line shows Clinton’s forecast percentage chance of winning, and the red line shows Trump’s forecast percentage chance of winning (the yellow line in the top plot corresponds to Libertarian Party candidate Gary Johnson, who was not included in the Times forecast). Note that the projections disagree about the likelihood of a Clinton victory at any given time, but they indicate the same trend of this likelihood rising and falling over time. Sources: https://projects.fivethirtyeight.com/2016-election-forecast/, and https://www.nytimes.com/interactive/2016/upshot/presidential-polls-forecast.html?mtrref=www.google.com&gwh=98BBC964A93A5930F7E7DE8961D883F8&gwt=pay&assetType=REGIWALL" title="Election projection results from FiveThirtyEight(top) and The New York Times (bottom) from June 2016 to November 8, 2016, the day of the US presidential election" width=350>
    </a>
  </div>

+ Tails should be fatter<br/>
  our distributions have fat tails
  + National error, regional error and state-specific error are drawn from a probability distribution. Specifically, they're drawn from a t-distribution (with 10 degrees of freedom)
  + the t-distribution has fatter tails than a normal (bell curve) distribution; i.e. it assigns shorter odds ot "extreme" outcomes.  For example if a normal distribution laid odds of 50-to-1 against an event, a t-distribution would have it more like 30-to-1 against.  Ans if a normal distribution assigned odds of 1,000-to-1 against, the t-distribution would have it more like 180-to-1 against.
  + the t-distribution is theoretically appropriate given a small sample size.  The model is only based on 11 past elections (from 1972 to 2012).  We don't have enough data to really know how the trail behave: whether a candidate trailing by 15 points on Election Day has 1, 0.1 or 0.01 percent chance of wining, doe example.  The t-distribution makes more conservative assumptions about this.
  + [Normal Distribution vs. t-distribution](https://www.geogebra.org/m/xp7A3A53) w/ GeoGebra
    + In real-world measurements we often do not have enough data points to form a normal distribution.
    + We have to make an extra calculation, a calculation of the confidence intervals using a student t-distribution the Mean and the Sample Standard Deviation.
    + This is normally taken to be the case with fewer than 20-30 measurements.
    + In general, Degree of Freedom (DoF) is the number of terms in a sum minus the number of constraints on the terms of the sum.
    + In this simple case the DoF is $n$, where $n$ is the number of measurements you have made. When the mean of the measurements is defined then DoF becomes $(n-1)$.


  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://andyjconnelly.wordpress.com/2017/05/16/uncertainty-and-repeats/" ismap target="_blank">
      <img src="https://andyjconnelly.files.wordpress.com/2017/05/distributions1.png?w=1140&h=658" style="margin: 0.1em;" alt="In real-world measurements we often do not have enough data points to form a normal distribution. We have to make an extra calculation, a calculation of the confidence intervals using a student t-distribution the Mean and the Sample Standard Deviation. This is normally taken to be the case with fewer than 20-30 measurements." title="Normal distribution vs. t-distribution" width=300>
    </a>
  </div>

+ Correlation between state voting (Demographic and regional error)
  + Some states’ outcomes are more correlated than others. For instance, if Trump beats his polls in Minnesota, he’ll probably also do so in Wisconsin. But that might not tell us much about Alabama.
  + The model simulates this by randomly varying the vote among demographic groups and regions. In one simulation, for instance, it might have Trump beating his polls throughout the Northeast. Therefore, he wins Maine, New Hampshire and New Jersey. In another simulation, Clinton does especially well among Hispanics and wins both Arizona and Florida despite losing Ohio.
  + The simulations are conducted from a file of more than 100,000 voters, built from the exit polls and CCES.
  + The following characteristics are considered in the simulations: religion (Catholic, mainline Protestant, evangelical, Mormon, other, none); race (white, black, Hispanic, Asian, other); region (Northeast, South, Midwest, West); party (Democrat, Republican, independent); and education (college graduate or not).
  + To get a better sense of how this works, here’s a correlation matrix drawn from recent simulations. You can see the high correlation between Wisconsin and Minnesota, for example.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/" ismap target="_blank">
      <img src="https://fivethirtyeight.com/wp-content/uploads/2016/06/silver-forecast-methology-31.png?w=575" style="margin: 0.1em;" alt="text" title="Demographic and regional error" width=350>
    </a>
  </div>

+ LA Times Daybreak poll

  > "Our operations allow voters to express a greater level of uncertainty than traditional poll questions which force respondents to choose a single candidate or say they don't know.  For example, in the Daybreak poll, a respondent might say that they are 60 percent for for Clinton and 40 percent for Trump."

  + STOP: does this make the Daybreak poll a good poll?
    + Ans: not really though the final result closer to the actual situation.  It's problematic in statistics.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://scalar.usc.edu/works/media-and-the-election/the-usc-dornsifela-times-charts.1" ismap target="_blank">
      <img src="http://scalar.usc.edu/works/media-and-the-election/media/Screen%20Shot%202016-11-20%20at%207.09.26%20PM.jpg" style="margin: 0.1em;" alt="Poll was conducted by USC Dornsife and the LA Times. They called these polls 'Daybreak' in which they track 3,000 eligible voters until election day, asking on a regular basis about their support for Hillary Clinton, Donald Trump or other candidates as well as their likelihood of actually casting a ballot. The poll presented here is a response from the question, Who would you vote for? The overall level of support for each candidate reflects the weighted averages of those responses." title="By the 3rd Presidential Debate, Trump had a higher possibility of being president than Clinton." width=450>
    </a>
  </div>

+ Notice the volatility in polls
  + STOP: if a weather forecaster told you there was a 70% chance of rain three months from now, would you believe them? what would be a better probability?
    + Ans: 
      + over expressing the certainty w/ 70%, it's very untrustworthy.
      + polling in July only reflects the situation at that moment
      + situation changing during the period from now on to the actual election day
      + it's difficult to infer that they reflect much about an election a few months down the time

+ Which stock would you rather bet on increasing 30% in 6 months?
  + Naive answer: this stock has gone up steadily in the past few years.
  + Scientist's answer: this stock is not very __volatile__.

+ Prediction markets gone wrong
  + __prediction market:__ investors can speculate on what they think might happen
  + LA Times prediction market for 2016 election
  + the market: a prediction market for stock
  + __derivative:__ an investment (i.e., an "option") whose price is tied to the value of an asset (e.g., stock)
  + opinion on stocks "price in" volatility
  + election market: "option pricing" models for election predictions
  + STOP: why might a gambling market not offer an accurate forecast?
    + people who gamble in a population are not necessarily the accurate subset of the people who are going to or an accurate proxy for the people who are going to actually vote in the election $\to$ might cause bias
    + what if a candidate had more total wagers placed upon them but the other candidate had more total money placed upon them which is exactly what happen in 2016

+ [Derivative](https://www.investopedia.com/ask/answers/12/derivative.asp)
  + a contract between two or more parties whose value is based on an agreed-upon underlying financial asset (like a security) or set of assets (like an index)
  + Common underlying instruments include bonds, commodities, currencies, interest rates, market indexes, and stocks.
  + secondary securities whose value is solely based (derived) on the value of the primary security that they are linked to
  + commonly used derivatives: [futures contracts](https://www.investopedia.com/terms/f/futurescontract.asp), forward contracts, [options](https://www.investopedia.com/terms/o/optionscontract.asp), [swaps](https://www.investopedia.com/terms/s/swap.asp), and [warrants](https://www.investopedia.com/terms/w/warrant.asp)
  + two classes of derivative products
    + Lock products (e.g. swaps, futures, or forwards) bind the respective parties from the outset to the agreed-upon terms over the life of the contract.
    + Option products (e.g. interest rate swaps), on the other hand, offer the buyer the right, but not the obligation, to become a party to the contract under the initially agreed upon terms.

+ [Option pricing theory](https://www.investopedia.com/terms/o/optionpricingtheory.asp)
  + using variables (stock price, exercise price, volatility, interest rate, time to expiration) to theoretically value an option
  + providing an estimation of an option's fair value which traders incorporate into their strategies to maximize profits
  + commonly used models: [Black-Scholes](https://www.investopedia.com/terms/b/blackscholes.asp), [binomial option pricing](https://www.investopedia.com/terms/b/binomialoptionpricing.asp), and [Monte-Carlo simulation](https://www.investopedia.com/terms/m/montecarlosimulation.asp)
  + primary goal: calculate the probability that an option will be exercised, or be in-the-money (ITM), at expiration
  + variables: asset price (stock price), exercise price, volatility, interest rate, and time to expiration
    + exercise price:
      + the price at which an underlying security can be purchased or sold when trading a call or put option, respectively
      + the same as the strike price of an option, which is known when an investor takes a trade
      + strike price: the set price at which a derivative contract can be bought or sold when it is exercised
    + volatility: 
      + a statistical measure of the dispersion of returns for a given security or market index
      + the amount of uncertainty or risk related to the size of changes in a security's value
      + often measured as either the standard deviation or variance between returns from that same security or market index

+ Moral: 
  + programming w/ Monte Carlo simulation is awesome!
  + must continually question/pick apart/make connections with out models
