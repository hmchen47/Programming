# Practical guide to controlled experiments on the web: listen to your customers not to the hippo](web03-Experiments.md)

Author: R. Kohavi, R. Henne, D. Sommerfield

Proceedings: KDD '07

Date: 2007

[Original](https://ai.stanford.edu/~ronnyk/GuideControlledExperiments.pdf)

[PPT](https://pdfs.semanticscholar.org/ee60/9ee721abea507057d30c6d0c7039e9e42da7.pdf)


## 1. Introduction

- Amazon personalized recommendation System
  - Greg Linden prototyping recommendations based on shopping cart
  - run controlled experiment $\to$ “feature won by such a wide margin that not having it live was costing Amazon a noticeable chunk of change
  - culture of experiment
    - data trumps intuition
    - a system that made running experiments easy
    - allowed Amazon to innovate quickly and effectively


- Controlled experiments
  - randomized experiments (single-factor, or fractional design)
  - A/B tests or their generalizations
  - split tests
  - control/treatment
  - parallel flights


- Simplest manifestation of the experiments on web
  - randomly assigned to one of two variants
    - Control: commonly the “existing” version
    - Treatment: usually a new version being evaluated
  - metrics
    - ranging from runtime performance to implicit and explicit user behaviors
    - Return-on-Investment (ROI)
  - survey
    - collecting data
    - conducting statistical tests
    - evaluating evaluate whether there is a statistically significant difference between the two variants on metrics of interest
  - null hypothesis: no difference between the versions
  - segmenting of users using manual (e.g., OLAP) or machine learning and data mining to understand which subpopulations show significant differences $\to$ helping improve our understanding and progress forward with an idea


- Building a system for experimentation
  - little cost of testing and experimental failure
  - encouraging innovation through experimentation


## 2. Motivating Examples

- Case 1: Checkout page at Doctor FootCare
  - conversion rate: the percentage of visit to the website that include a purchase
  - nine differences between the two variants of the Doctor FootCare checkout page
  - which one results in a higher conversion rate


- Case 2: Ratings of Microsoft Office help articles
  - initial implementation: a Yes/No widget
  - modified the widget w/ a 5-star ratings
  - motivations
    - providing finer-grained feedback
    - improving usability by exposing users to a single feedback box


- Results and ROI
  - Doctor FootCare checkout page
    - Variant A on left, Variant B on right (diagram)
    - variant A outperformed variant B by an order of magnitude
    - "upgraded" from the A to B and lost 90% of their revenue
    - coupon code: people started to think twice about whether they were paying too much
    - removing discount code from the new version (B), conversion-rate increased 6.5% relative to the old version (A)
  - Microsoft’s Office Help articles
    - the number of ratings plummeted by an order of magnitude $\to$ significantly missing on goal #2 above
    - additional tests: two-stage model actually helps in increasing the response rate
  - hard to predict the success of new designs
  - controlled experiments used heavily in backend algorithms

  <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open('https://ai.stanford.edu/~ronnyk/GuideControlledExperiments.pdf')"
      src    = "img/web04-DrFootCare.png"
      alt    = "Doctor FootCare checkout page: Variant A (left) and Variant B (right)"
      title  = "Doctor FootCare checkout page: Variant A (left) and Variant B (right)"
    />
  </figure>

## 3. Controlled Experiments

- Simplest controlled experiment
  - usually referred to as an A/B test
  - randomly exposed to one of two variants: control (A), or treatment (B)
  - random
    - not distributed "any old which way"
    - no factor able to influence the decision
    - Overall Evaluation Criterion (OEC) derived for each variant
  - OEC possible metrics (case 1: the conversion rate, units purchased, revenue, profit, expected lifetime value, or or some weighted combination of these
  - experiment designed and executed properly
    - the only thing consistently different between the two variants is the change between the Control and Treatment
    - any differences in the OEC are inevitably the result of this assignment, establishing causality

  <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
      onclick= "window.open('https://ai.stanford.edu/~ronnyk/GuideControlledExperiments.pdf')"
      src    = "img/web04-ABTest.png"
      alt    = "Doctor FootCare checkout page: Variant A (left) and Variant B (right)"
      title  = "Doctor FootCare checkout page: Variant A (left) and Variant B (right)"
    />
  </figure>


### 3.1 Terminology

- Overall Evaluation Criterion (OEC)
  - a quantitative measure of the experiment’s objective
  - a.k.a. Response or Dependent Variable in statistics
  - other synonyms: Outcome, Evaluation metric, Performance metric, or Fitness Function (22). 
  - selecting a single metric though experiments possible w/ multiple objectives
  - possibly as a weighted combination of such objectives
  - forcing tradeoffs to be made once for multiple experiments
  - aligning the organization behind a clear objective
  - not a short-term focused (e.g., clicks)
  - including factors that predict long-term goals, e.g., predicted lifetime value and repeat visits


- Factor
  - to influence the OEC
  - assigned Values, sometimes called 
  - a.k.a. Levels or Versions, Variables
  - A/B tests: a single factor with two values - A and B.


- Variant
  - user experience being tested by assigning levels to the factors
  - either the Control or one of the Treatments
  - prefering to specifically differentiate between the Control
  - sometimes referred to as Treatment, a special variant that designates the existing version being compared against and the new Treatments being tried


- Experimentation unit
  - an entity observed, a.k.a. an item
  - assumption: independent
  - web experimentation unit
    - user: the most common experimentation unit
    - sessions or page views
    - commonly achieved through cookies

- Terminologies of statistics
  - Null Hypothesis
    - often referred to as $H_0$
    - no difference on the OECs for the variants
    - randomly observed differences during the experiment
  - Confidence level: probability of failing to reject (i.e., retaining) the null hypothesis when it is true
  - Power:
    - probability of correctly rejecting the null hypothesis, $H_0$, when it is false
    - measuring the ability to detect a difference when it indeed exists
  - Standard Deviation (Std-Dev)
    - a measure of variability
    - typically denoted by 𝜎$\sigma$
  - Standard Error (Std-Err)
    - the standard deviation of the sampling distribution of the sample statistic
    - a mean of 𝑛 independent observations: $\widehat{\sigma} / n$ where $\widehat{\sigma}$ is the estimated standard deviation.


- A/A Test
  - a.k.a. a Null Test
  - assigning users to one of two groups, but exposing them to exactly the same experience
  - scenarios
    - collecting data and assessing its variability for power calculations
    - testing the experimentation system
  - the Null hypothesis rejected about $5\%$ of the time when a $95\%$ confidence level is used



### 3.2 Hypothesis Testing and Sample Size

- Statistical test
  - used to evaluate one of the treatment is different than the Control
  - accept a Treatment as being statistically significantly different if the test rejects the null hypothesis
  - i.e., the OECs not different


- Important factors of statistical test
  - **Confidence level**
    - commonly set to 95%
    - 5% of the time incorrectly conclude that there is a difference when there is none (Type I error)
    - all else being equal, increasing this level reduces the power
  - **Power**
    - commonly desired to be around 80-95%, although not directly controlled
    - false Null Hypothesis:
      - there is a difference in the OECs
      - the power is the probability of determining that the difference is statistically significant
      - A Type II error: retaining the Null Hypothesis when it is false
  - **Standard Error**
    - the smaller the Std-Err, the more powerful the test
    - three useful ways to reduce the Std-Err
      - estimated OEC:
        - typically a mean of large samples
        - Std-Err of a mean decreasing proportionally to the square root of the sample size $\timplies$ increasing the sample size
        - usually implying running the experiment longer, reducing the Std-Err and hence increasing the power
      - using OEC components that have inherently lower variability
        - the Std-Dev, $\sigma$, smaller
        - example: conversion probability (0-100%) typically has lower Std-Dev than number of purchase units (typically small integers), which in turn has a lower Std-Dev than revenue (real-valued)
    - lower the variability of the OEC
      - filtering out users who were not exposed to the variants, yet were still included in the OEC
      - example:
        - a change to the checkout page $\to$ analyze only users who got to the page
        - everyone else adds noise, increasing the variability
  - the effect, or the difference in OECs for the variants
    - larger differences are easier to detect $\implies$ great ideas unlikely missed
    - samll effect: Type I or Type II errors more likely


- Sample size
  - the desired confidence level: $95\%$
  - the desired power: $90\%$
  - the desired sample size, $n$

    \[ n = (4r\sigma/\Delta)^2 \]

    - $r$: the number of variants (assumed to be approximately equal in size)
    - $\sigma$: the std-dev of the OEC
    - $\Delta$: the minimum difference between the OECs
    - $4$: overestimated by $25\%$ for large $n$
  - example of sample size
    - e-commerce site w/ $5\%$ of users who visit during the experiment period end up purchasing
    - purchasing spend about \$75
    - average user spending \$3.75 (95% spend \$0)
    - standard deviation: $30
    - running an A/B test and want to detect a 5% change to revenue
    - requiring over 1.6 million users to achieve the desired 90% power

      \[ 4 \cdot 2 \cdot 30 / (3.75 \cdot 0.05)^2 \ge 1,600,000\]


- Sample size with Bernoulli distribution
  - only looking for a 5% change in rate (not revenue)
  - a lower variability OEC used (Standard Error)
  - purchase, a conversion event, modeled as a Bernoulli trial with $p=0.05$ being the probability of a purchase
  - standard error of Bernoulli: $\sqrt{p(1-p)}$
  - sample size to achieve desired power: 

    \[(4 \cdot 2 \cdot \sqrt{0.05 \cdot (1 − 0.05)} / (0.05 \cdot 0.05))^2 \lt 500,000 \]

  - square factor
    - relaxed goal: detecting a 20% change in conversion
    - factor $4$ dropped by a factor of 16
    - sample size: 

    \[(4 \cdot 2 \cdot \sqrt{0.05 \cdot (1 − 0.05)} / (0.05 \cdot 0.05))^2 /16 \approx 30,400\]


- Example: lower varability of the OEC
  - change to the checkout process $\to$ only analyze users who started the checkout process
  - assumptions
    - 10% of users initiate checkout 
    - that 50% of those users complete
  - more homogenious user segment $\implies$ OEC w/ lower variability
  - average conversion rate: 0.5
  - std-dev: 0.5
  - sample size: 

    \[ (4 \cdot 2 \cdot \sqrt{0.5 \cdot (1 − 0.5)} / (0.5 \cdot 0.05))^2 = 25,600 \]

  - total number of users to the (excluding the 90% who do not initiate): 256,000


- Considerations of experiment
  - deciding in advance on the OEC (a planned comparison)
  - an increased risk of finding what appear to be significant results by chance (familywise type I error)
  - proposed adjustments
    - Fisher’s least-significantdifference
    - Bonferroni adjustment
    - Duncan’s test
    - Scheffé’s test
    - Tukey’s test
    - Dunnett’s test
  - increasing the 95% confidence level and thus reducing the statistical power


### 3.3 Extensions for Online Settings

- Extensions to basic controlled experiments in an online setting
  - treatment ramp-up
  - automation
  - software migrations


- Treatment ramp-up
  - initiated with a small percentage of users assigned to the treatment(s)
  - gradually increasing the percentage
  - example
    - planning to run an A/B test at $50\%/50\%$
    - starting with a $99.9\%/0.1\%$ split
    - rampping up the Treatment: $0.1\% \to0.5\% \to 2.5\% \to 10\% \to 50\%$
    - analyzing the data to ensure no egregious problems with the Treatment before exposing it to more users
  - square factor in the power formula
    - such errors could be caught quickly on small populations
    - the experiment can be aborted before many users are exposed to the bad treatment


- Automation
  - running experiments to optimize certain areas amenable to automated search w/ clear OEC
  - example: slots on the home page at Amazon are automatically optimized
  - quick decision required 
    - lower confidence levels because the cost of mistakes is lower
    - example: headline optimizations for portal sites
  - optimization algorithms: Multi-armed bandit algorithms and Hoeffding Races


- Software migrations
  - a feature or a system migrated to a new backend, new database, or a new language
  - but not expected to change uservisible features
  - an A/B test executed with the goal of retaining the Null Hypothesis, vairant no difference
  - migration declared complete, but an A/B test showed significant differences in key metrics $\to$ helping identify bugs in port
  - goal here to retain the Null Hypothesis 
  - crucial to ensure the experiment w/ enough statistical power to actually reject the Null Hypothesis if it false


### 3.4 Limitations

- Limitations in web
  1. Quantitative Metrics, but No Explanations
  2. Short term vs. Long Term Effects
  3. Primacy and Newness Effects
  4. Features Must be Implemented
  5. Consistency
  6. Consistency
  7. Launch Events and Media Announcements


- Quantitative metrics, but no explanations
  - possible know which variant better, and by how much, but not “why”
  - example: 
    - behavior often augmented with users’ comments
    - hence usability labs used to augment and complement controlled experiments


- Short term vs. long term effects
  - measuring the effect on the OEC during the experimentation period, typically a few weeks
  - some criticized that focusing on a metric implies short-term focus $\to$ disagree
  - long-term goals as part of the OEC
  - example
    - revenue as OEC
    - probably plastering ads over a page
    - too many ads hurt the user experience
    - a good OEC
      - including a penalty term of usage of real-estate for ads that are not clicked
      - directly measuring repeat visits and abandonment
    - latent conversions: delayed conversion metrics, a lag from the time a user is exposed to something and take action
  - good OECs difficult to retain
  - key point
    - recognize this limitation
    - but avoid throwing the baby out with the bathwater


- Primacy and newness effects
  - recognizing opposite effects required
  - example
    - changing the navigation on a web site
    - experienced users probably less efficient until they get used to the new navigation
    - giving an inherent advantage to the Control
  - example
    - introducing a new design or feature
    - some users investigating it by clicking everywhere
    - introducing a “newness” bias.
    - bias associated with the Hawthorne Effect
  - some experiments run for multiple weeks
  - one analysis able to be done: to compute the OEC only for new users on the different variants


- Features must be implemented
  - required to expose some users to a Treatment different than the current site (Control)
  - probably a prototype being tested against a small portion, or may not cover all edge cases
  - example:
    - the experiment may intentionally exclude 20% of browser types that would require significant testing
    - must be implemented
    - be of sufficient quality to expose users to it
  - Jacob Nielsen: paper prototyping
    - used for qualitative feedback
    - quick refinements of designs in early stages
  - recommend: the techniques complementing controlled experiments


- Consistency
  - probably getting a different variant than their friends and family
  - possible seeing multiple variants when using different computers (with different cookies)
  - relatively rare that users will notice the difference


- Parallel experiments
  - rarely strong interactions in practice
  - the concern overrated
  - raising awareness of this concern is enough for experimenters to avoid tests that can interact
  - pairwise statistical tests done by flagging such interactions automatically


- Launch Events and media announcements
  - a big announcement made about a new feature
  - announced to the media $\to$ all users need to see it



## 4. Implementation Architecture

- Components of implementing an experiment on a website
  - randomization algorithm: a function that maps users to variants
  - assignment method: using the output of the randomization algorithm to determine the experience that each user will see on the website


### 4.1 Randomization Algorithm

- Randomization algorithm overview
  - critical to find a good one
  - assumption: each variant of an experiment w/ a random sample of users
  - properties
    1. no bias toward any particular variant (assuming a 50-50 split)
    2. consistent on repeat assignments of a single user
    3. no correlation between experiments
    4. supporting monotonic ramp-up


- Pseudorandom with caching
  - using standard pseudorandom number generator coupled with a form of caching.
  - good pseudorandom number generator: satisfying the first and third requirements of the randomization algorithm
  - seeding: probably causing adjacent requests to use the same seed $\to$ introducing noticeable correlations between experiments
  - second requirement
    - introducing state: the assignments of users must be cached once they visit the site
    - cache: either on the server side or on the client side
      - server side: storing the assignments for users in some form of database
      - client side: storing a user’s assignment in a cookie
    - difficult to scale up to a large system with a large fleet of servers
    - communicating its state to all the other servers to keep assignments consistent
  - fourth requirement
    - difficult to implement using this method
    - required carefully to reassign Control users who visit the site after a ramp-up to a treatment


- Hash and partition
  - completely stateless
  - each user assigned a unique identifier, maintained either through a database or a cookie
  - identifier appended onto the name or id of the experiment
  - very sensitive to the choice of hash function
  - hash function
    - applied to this combined identifier to obtain an integer, uniformly distributed on a range of values
    - range partitioned w/ each variant represented by a partition
    - any funnels (instances where adjacent keys map to the same hash code) $\implies$ violated the first property
    - characteristics (instances where a perturbation of the key produces a predictable perturbation of the hash code) $\implies$ correlations occurted between experiments
    - satisfying second requirement
  - difficult to satisfy the first and third requirements
    - MD5: no correlations between experiments
    - HSA256: close, requiring a five-way interaction to produce a correlation


### 4.2 Assignment Method

- Assignment method overview
  - a piece of software that enables the experimenting website to execute a different code path for different users
  - good assignment method: causing anything from visible website content to backend algorithms to vary by user
  - implementations
    - traffic splitting
    - code-driven selection
    - client-side page modification (Ajax)
    - metadata-driven selection


- Traffic splitting
  - a method that involves implementing each variant of an experiment on a different logical fleet of servers
  - possible ways: different physical servers, different virtual servers, or event different ports on the same machine
  - using either a load balancer or proxy server to split traffic
  - advantage: the only assignment method that requires no changes to existing code to implement an experiment
  - significant disadvantages
    - disproportionately difficult w/ small features: the entire application must be replicated regardless of the size of the change
    - expensive to set up and configure parallel fleets: sufficient capacity to take 100% of the traffic in the event that the experiment needs to be shut down
    - tremendous effort when running multiple experiments simultaneously
      - the fleet requiring one partition for each combination of variants across all experiments
      - number increasing exponentially as the number of experiments increases
    - Any differences between the fleets used for each variant probably confounding the experimental results
      - identical hardware and network topology of each fleet
      - A/A tests run to confirm the absence of fleet-related effects
  - one of the most expensive ways to implement an experiment
  - recommendation: only for testing changes that introduce significantly different code


- Code-review selection
  - a family of methods using code embedded into the website’s servers to produce a different user experience for each variant
  - taking the form of an API call placed at the point where the website logic differs between variants
    - invoking the randomization algorithm
    - returning the identifier of the variant to be displayed for the current user
  - placed anywhere on the server side
    - from front-end rendering to back-end algorithms
    - a complex experiment probably making use of multiple API calls inserted into the code at different places
  - code changes
    - involving the API call specific to a single experiment
    - removed when the experiment ends
  - implemented as a local function call
  - using an external service to ensure that the assignment logic stays consistent across a large server fleet
  - advantages
    - extremely general method: possible to experiment on virtually any aspect of a page simply by modifying its code
    - placing the experimentation code in the best logical place: possible to experiment on backend features without touching the front end
    - API designed to record a special event (trigger): a user has reached a choice point between variants
    - running multiple experiments run simultaneously w/o requiring any coordination between their owners
  - disadvantages
    - requiring a developer to change code deep in the page logic for each experiment $\to$ introducing risk
    - difficult to implement on pages built on content management frameworks $\to$ metadata-driven selection as superior approach
    - manually undone to complete an experiment
      - a painful process if API calls are spread throughout the code
      - a big problem when experimenting on poorly designed pages
  - the best approach for experiments on
    - backend algorithms 
    - pages implemented directly in a language


- Client-side page modification (Ajax)
  - the assignment technique employed by several commercial products
  - running an experiment without making any decisions on the server
  - a form of code-driven selection 
  - inserting JavaScript code that instructs the user’s browser to invoke an assignment service at render time
  - service call
    - returning the appropriate variant for the user
    - triggering a JavaScript callback that instructs the browser to dynamically alter the page being presented to the user
  - proper changes: occurred before any part of the page renders
  - content of each variant: either be cleverly embedded into the page or served by the assignment service
  - easier to implement on a simple site than other code-driven method
  - disadvantages
    - not working well for complex sites that rely on dynamic content
    - adding a noticeable delay for users
    - able to extract the content of each variant and pollute the results






## 5. Lesson Learned




## 6. Summary









