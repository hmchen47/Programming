# YAML Ain’t Markup Language

Institute: YAML.org

Date: Revision 1.2.2 (2021-10-01)

[Original](https://yaml.org/spec/1.2.2)


## Introduction to YAML

- YAML overview
  - a data serialization language
  - designed to be human-friendly
  - working well with modern programming languages for common everyday tasks
  - using Unicode printable characters 
    - some providing structural information
    - the rest containing the data itself
  - achieving a unique cleanness by minimizing the amount of structural characters
  - allowing the data to show itself in a natural and meaningful way
    - indentation used for structure
    - colons separating key/value pairs
    - dashes used to create "bulleted" lists


- Basic primitives
  - mappings (hashes/dictionaries)
  - sequences (arrays/lists)
  - scalars (strings/numbers)


- Purpose of YAML
  - to form a complete language for serializing any native data structure by
    - leveraging primitives 
    - adding a simple typing system
    - aliasing mechanism
  - easy to view and understand
  - working well for common use cases such as
    - configuration files
    - log files
    - interprocess messaging
    - cross-language data sharing
    - object persistence
    - debugging of complex data structures


- Goals for YAML in decreasing priority
  - YAML should be easily readable by humans.
  - YAML data should be portable between programming languages.
  - YAML should match the native data structures of dynamic languages.
  - YAML should have a consistent model to support generic tools.
  - YAML should support one-pass processing.
  - YAML should be expressive and extensible.
  - YAML should be easy to implement and use.


## Language Overview

- Collections
  - block collections using indentation for scope
  - begining each entry on its own line
  - block sequences: indicating each entry with a dash and space (`- `)
  - mappings: using a colon and space (`: `) to mark each key/value pair
  - comments: begining with an octothorpe (also called a "hash", "sharp", "pound" or "number sign" - `#`)
  - flow styles: using explicit indicators rather than indentation to denote scope
  - flow sequence: written as a comma separated list within square brackets (`[]`)
  - flow mapping: useing curly braces(`()`)
  - examples

    ```yaml
    # Sequence of Scalars (ball players)
    - Mark McGwire
    - Sammy Sosa
    - Ken Griffey

    # Mapping Scalars to Scalars (player statistics)
    hr:  65    # Home runs
    avg: 0.278 # Batting average
    rbi: 147   # Runs Batted In

    # Mapping Scalars to Sequences (ball clubs in each league)
    american:
    - Boston Red Sox
    - Detroit Tigers
    - New York Yankees
    national:
    - New York Mets
    - Chicago Cubs
    - Atlanta Braves

    # Sequence of Mappings (players’ statistics)
    -
      name: Mark McGwire
      hr:   65
      avg:  0.278
    -
      name: Sammy Sosa
      hr:   63
      avg:  0.288

    # Sequence of Sequences
    - [name        , hr, avg  ]
    - [Mark McGwire, 65, 0.278]
    - [Sammy Sosa  , 63, 0.288]

    # Mapping of Mappings
    Mark McGwire: {hr: 65, avg: 0.278}
    Sammy Sosa: {
        hr: 63,
        avg: 0.288,
    }
    ```


- Structures
  - three dashes (`---`)
    - separating directives from document content
    - serving to signal the start of a document if no directives are present
  - three dots (`...`): indicating the end of a document without starting a new one, for use in communication channels
  - repeated nodes (objects):
    - first identified by an anchor (marked with the ampersand - `&`)
    - thereafter aliased (referenced with an asterisk - `*`)
  - question mark and space (`? `): indicating a complex mapping key
  - key/value pairs: started immediately following the dash, colon or question mark
  - examples

    ```yaml
    # Two Documents in a Stream (each with a leading comment)

    ## Ranking of 1998 home runs
    ---
    - Mark McGwire
    - Sammy Sosa
    - Ken Griffey

    ## Team ranking
    ---
    - Chicago Cubs
    - St Louis Cardinals

    # Play by Play Feed from a Game
    ---
    time: 20:03:20
    player: Sammy Sosa
    action: strike (miss)
    ...
    ---
    time: 20:03:47
    player: Sammy Sosa
    action: grand slam
    ...

    # Single Document with Two Comments

    ---
    hr: # 1998 hr ranking
    - Mark McGwire
    - Sammy Sosa
    # 1998 rbi ranking
    rbi:
    - Sammy Sosa
    - Ken Griffey

    # Node for "Sammy Sosa" appears twice in this document
    ---
    hr:
    - Mark McGwire
    # Following node labeled SS
    - &SS Sammy Sosa
    rbi:
    - *SS # Subsequent occurrence
    - Ken Griffey

    # Mapping between Sequences
    ? - Detroit Tigers
      - Chicago cubs
    : - 2001-07-23

    ? [ New York Yankees,
        Atlanta Braves ]
    : [ 2001-07-02, 2001-08-12,
        2001-08-14 ]

    # Compact Nested Mapping
    ---
    ## Products purchased
    - item    : Super Hoop
      quantity: 1
    - item    : Basketball
      quantity: 4
    - item    : Big Shoes
      quantity: 1
    ```


- Scalars of YAML
  - Scalar content
    - written in block notation, using a literal style (indicated by `|`) where all line breaks are significant
    - written with the folded style (denoted by `>`) where each line break is folded to a space unless it ends an empty or a more-indented line
  - flow scalars
    - including the plain style (most examples thus far) and two quoted styles
    - double-quoted style: providing escape sequences
    - single-quoted style: useful when escaping is not needed
    - able to span multiple lines
    - line breaks always folded
  - example

    ```yaml
    # In literals, newlines are preserved
    # ASCII Art
    --- |
      \//||\/||
      // ||  ||__

    # In the folded scalars, newlines become spaces
    --- >
      Mark McGwire's
      year was crippled
      by a knee injury.

    # Folded newlines are preserved for "more indented" and blank lines
    --- >
    Sammy Sosa completed another
    fine season with great stats.

      63 Home Runs
      0.288 Batting Average

    What a year!

    # Indentation determines scope
    name: Mark McGwire
    accomplishment: >
      Mark set a major league
      home run record in 1998.
    stats: |
      65 Home Runs
      0.278 Batting Average

    # Quoted Scalars
    unicode: "Sosa did fine.\u263A"
    control: "\b1998\t1999\t2000\n"
    hex esc: "\x0d\x0a is \r\n"

    single: '"Howdy!" he cried.'
    quoted: ' # Not a ''comment''.'
    tie-fighter: '|\-*-/|'

    # Multi-line Flow Scalars
    plain:
      This unquoted scalar
      spans many lines.

    quoted: "So does this
      quoted scalar.\n"
    ```


- Tags of YAML
  - untagged nodes:
    - given a type depending on the application
    - generally using the seq, map and str types from the fail safe schema
    - also using the int, float and null types from the JSON schema
  - explicit typing
    - denoted with a tag using the exclamation point (`!`) symbol
    - global tags:
      - URIs
      - probably specified in a tag shorthand notation using a handle
    - application-specific local tags probably used
  - examples

    ```yaml
    # Integers
    canonical: 12345
    decimal: +12345
    octal: 0o14
    hexadecimal: 0xC

    # Floating Point
    canonical: 1.23015e+3
    exponential: 12.3015e+02
    fixed: 1230.15
    negative infinity: -.inf
    not a number: .nan

    # Miscellaneous
    null:
    booleans: [ true, false ]
    string: '012345'

    # Timestamps
    canonical: 2001-12-15T02:59:43.1Z
    iso8601: 2001-12-14t21:59:43.10-05:00
    spaced: 2001-12-14 21:59:43.10 -5
    date: 2002-12-14

    # Various Explicit Tags
    ---
    not-date: !!str 2002-04-28

    picture: !!binary |
    R0lGODlhDAAMAIQAAP//9/X
    17unp5WZmZgAAAOfn515eXv
    Pz7Y6OjuDg4J+fn5OTk6enp
    56enmleECcgggoBADs=

    application specific tag: !something |
    The semantics of the tag
    above may be different for
    different documents.

    # Global Tags
    %TAG ! tag:clarkevans.com,2002:
    --- !shape
      # Use the ! handle for presenting
      # tag:clarkevans.com,2002:circle
    - !circle
      center: &ORIGIN {x: 73, y: 129}
      radius: 7
    - !line
      start: *ORIGIN
      finish: { x: 89, y: 102 }
    - !label
      start: *ORIGIN
      color: 0xFFEEBB
      text: Pretty vector drawing.

    # Unordered Sets
    # Sets are represented as a
    # Mapping where each key is
    # associated with a null value
    --- !!set
    ? Mark McGwire
    ? Sammy Sosa
    ? Ken Griffey

    # Ordered Mappings
    # Ordered maps are represented as
    # A sequence of mappings, with
    # each mapping having one key
    --- !!omap
    - Mark McGwire: 65
    - Sammy Sosa: 63
    - Ken Griffey: 58
    ```


- Full length example

  ```yaml
  # Invoice
  --- !<tag:clarkevans.com,2002:invoice>
  invoice: 34843
  date   : 2001-01-23
  bill-to: &id001
    given  : Chris
    family : Dumars
    address:
      lines: |
        458 Walkman Dr.
        Suite #292
      city    : Royal Oak
      state   : MI
      postal  : 48046
  ship-to: *id001
  product:
  - sku         : BL394D
    quantity    : 4
    description : Basketball
    price       : 450.00
  - sku         : BL4438H
    quantity    : 1
    description : Super Hoop
    price       : 2392.00
  tax  : 251.42
  total: 4443.52
  comments:
    Late afternoon is best.
    Backup contact is Nancy
    Billsmer @ 338-4338.


  # Log File
  ---
  Time: 2001-11-23 15:01:42 -5
  User: ed
  Warning:
    This is an error message
    for the log file
  ---
  Time: 2001-11-23 15:02:31 -5
  User: ed
  Warning:
    A slightly different error
    message.
  ---
  Date: 2001-11-23 15:03:17 -5
  User: ed
  Fatal:
    Unknown variable "bar"
  Stack:
  - file: TopClass.py
    line: 23
    code: |
      x = MoreObject("345\n")
  - file: MoreClass.py
    line: 58
    code: |-
      foo = bar
  ```


## Syntax Conventions

- Production syntax
  - syntax: `production-name ::= term`
  - atomic term
    - double quoted string (`"abc"`): concatenation of characters
    - single quoted character (`'a'`): usually a single character
    - hexadecimal number (`x0A`): character at that Unicode code point
    - range of hexadecimal numbers (`[x20-x7E]`): any character whose Unicode code point is within that range
    - name of a production (`c-printable`): that production
  - lookaround
    - `[ lookahead = term ]`:  the empty string if `term` would match
    - `[ lookahead ≠ term ]`:  the empty string if `term` would not match
    - `[ lookbehind = term ]`: the empty string if `term` would match beginning at any prior point on the line and ending at the current position
  - special production
    - `<start-of-line>`: the empty string at the beginning of a line
    - `<end-of-input>`: the empty string at the end of the input
    - `<empty>`: always matching the empty string
  - parenthesized term: matching its contents
  - concatenation `term-one term-two`: `term-one` followed by `term-two`
  - quantified term:
    - `term?`: `(term | <empty>)`
    - `term*`: `(term term* | <empty>)`
    - `term+`: `(term term*)`
    - quantified terms are always greedy
  - order of precedence: parenthesization, then quantification, then concatenation, then alternation
  - comment (`#`): informative only


- Production parameters
  - parameters in parentheses after the name, such as `s-line-prefix(n,c)`
  - shorthand for a (infinite) series of productions, each with a fixed value for each parameter
  - examples

    ```yaml
    # production 1
    production-a(n) ::= production-b(n)

    # shorthand of production 1
    production-a(0) ::= production-b(0)
    production-a(1) ::= production-b(1)
    …

    # production 2
    production-a(n) ::=
      ( production-b(n+m) production-c(n+m) )+

    # shorthand of production 2
    production-a(0) ::=
        ( production-b(0) production-c(0) )+
      | ( production-b(1) production-c(1) )+
      | …
    production-a(1) ::=
        ( production-b(1) production-c(1) )+
      | ( production-b(2) production-c(2) )+
      | …
    …
    ```

    - parameters
      - Indentation `n` or `m`: any natural number, including zero. n may also be -1
      - Context `c`: tweak their behavior according to their surrounding
        - two groups of contexts, distinguishing between [block styles](https://yaml.org/spec/1.2.2/#block-style-productions) and [flow styles](https://yaml.org/spec/1.2.2/#flow-style-productions)
        - `BLOCK-IN`: inside block context
        - `BLOCK-OUT`: outside block context
        - `BLOCK-KEY`: inside block key context
        - `FLOW-IN`: inside flow context
        - `FLOW-OUT`: outside flow context
        - `FLOW-KEY`: inside flow key context
      - (Block) Chomping `t`
        - the line break chomping behavior for flow scalars
        - `STRIP` – remove all trailing newlines
        - `CLIP` – remove all trailing newlines except the first
        - `KEEP` – retain all trailing newlines


- Production naming conventions
  - `e-`: a production matching no characters.
  - `c-`: a production starting and ending with a special character
  - `b-`: a production matching a single line break
  - `nb-`: a production starting and ending with a non-break character
  - `s-`: a production starting and ending with a white space character
  - `ns-`: a production starting and ending with a non-space character
  - `l-`: a production matching complete line(s)
  - `X-Y-`: a production starting with an X- character and ending with a Y- character, where X- and Y- are any of the above prefixes
  - `X+, X-Y+`: a production as above, with the additional property that the matched content indentation level is greater than the specified n parameter





