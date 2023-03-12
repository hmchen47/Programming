# Introducing JSON

[Origin](https://www.json.org/json-en.html)


+ JSON (JavaScript Object Notation)
  + a lightweight data-interchange format
  + easy for humans to read and write
  + easy for machines to parse and generate
  + based on a subset of the JavaScript Programming Language Standard ECMA-262 3rd Edition - December 1999
  + a text format completely language independent
  + using conventions familiar to programmers of the C-family of language
  + built on two structures
    + a collection of name/value pairs: an object, record, struct, dictionary, hash table, keyed list, or associative array
    + an ordered list of values: array, vector, list, or sequence
  + universal data structures

+ JSON object
  + an unordered set of name/value pair
  + begin w/ '{' and end w/ '}'
  + each name followed by ':'
  + name/value pairs separated by ','

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.json.org/json-en.html')"
      src    = "https://www.json.org/img/object.png"
      alt    = "JSON object syntax"
      title  = "JSON object syntax"
    />
  </figure>

+ JSON array
  + an ordered collection of values
  + begin w/ '[' and end w/ ']'
  + values separated by ','

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.json.org/json-en.html')"
      src    = "https://www.json.org/img/array.png"
      alt    = "JSON array syntax"
      title  = "JSON array syntax"
    />
  </figure>

+ JSON value
  + a string in double quotes, a number, `true`, `false`, `null` or an array
  + able to be nested

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.json.org/json-en.html')"
      src    = "https://www.json.org/img/value.png"
      alt    = "JSON value syntax"
      title  = "JSON value syntax"
    />
  </figure>

+ JSON string
  + a sequence of zero or more Unicode characters, wrapped in double quotes, using backslash escapes
  + a character represented as a single character
  + very much like a C orr Java string

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.json.org/json-en.html')"
      src    = "https://www.json.org/img/string.png"
      alt    = "JSON string syntax"
      title  = "JSON string syntax"
    />
  </figure>

+ JSON number
  + very much like C and Java number
  + exception: no octal and hexadecimal formats

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.json.org/json-en.html')"
      src    = "https://www.json.org/img/number.png"
      alt    = "JSON number syntax"
      title  = "JSON number syntax"
    />
  </figure>

+ JSON whitespace
  + inserted btw any pair of tokens
  + exception: a few encoding details

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.json.org/json-en.html')"
      src    = "https://www.json.org/img/whitespace.png"
      alt    = "JSON whitespace syntax"
      title  = "JSON whitespace syntax"
    />
  </figure>


