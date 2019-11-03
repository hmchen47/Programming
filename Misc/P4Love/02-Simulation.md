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





