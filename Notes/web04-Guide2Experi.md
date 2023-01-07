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




## 4. Implementation Architecture




## 5. Lesson Learned




## 6. Summary









