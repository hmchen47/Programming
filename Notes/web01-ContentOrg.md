# Easy content organisation with HTML5

Author: Steve Faulkner

Date: 24 September 2015

[Origin](https://tinyurl.com/y36qwg6f)


## Intro

+ Regions
  + divide web pages into macro content areas
  + typical regions: header, navigation, main content, sidebar, footer

    <figure style="margin: 0.5em; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
        onclick="window.open('https://tinyurl.com/y36qwg6f')"
        src    ="https://tinyurl.com/y5umz2o3"
        alt    ="Page layout with header at top, nav on right side, main in the middle, aside on right side and footer at bottom."
      />
      <figcaption> Page layout with header at top, nav on right side, <br/>main in the middle, aside on right side and footer at bottom. </figcaption>
    </figure>

  + All of the page content is organised into a small number of regions which are parents of the rest of the page content.
  + usually regions identifiable visually by design and the type of content they contain
  + HRML5: 
    + e elements: [aside](https://tinyurl.com/y245fvvg), [footer](https://tinyurl.com/y244jq2f), [header](https://tinyurl.com/y5bgwkyj), [main](https://tinyurl.com/y2r7urud) and [nav](https://tinyurl.com/y369rxqy)
    + provide the understanding and navigation benefits of content organisation to users who would otherwise not be able to perceive it from the visual cues alone
  + code example

    ```html
    <header></header>
    <nav></nav>
    <main><main>
    <aside></aside>
    <footer></footer>
    ```

## Region order

Content region order based on content organization

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y36qwg6f')"
    src    ="https://tinyurl.com/y62j5wlj"
    alt    ="Page layout with a fat footer at the top, followed by the main content and navigation at the bottom."
  />
  <figcaption>Page layout with a fat footer at the top, <br/>followed by the main content and navigation at the bottom.</figcaption>
</figure>


```html
<footer></footer>
<main><main>
<nav></nav>
```


## Regions within Regions

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y36qwg6f')"
    src    ="https://tinyurl.com/y6ak3ggy"
    alt    ="Page with navigation within the header region"
  />
  <figcaption>Page with navigation within the header region</figcaption>
</figure>


```html
<header>
<nav></nav>
</header>
<main><main>
<aside></aside>
<footer></footer>
```

