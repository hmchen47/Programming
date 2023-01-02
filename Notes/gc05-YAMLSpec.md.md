# YAML Ain’t Markup Language

Institute: YAML.org

Date: Revision 1.2.2 (2021-10-01)

[Original](https://yaml.org/spec/1.2.2)


## Introduction to YAML

- YAML overview
  - a data serialization language
  - designed to be human-friendly and 
  - working well with modern programming languages for common everyday tasks
  - using Unicode printable characters 
    - some providing structural information
    - the rest containing the data itself
  - achieving a unique cleanness by minimizing the amount of structural characters
  - allowing the data to show itself in a natural and meaningful way
    - indentation used for structure
    - colons separating key/value pairs
    - dashes used to create “bulleted” lists


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
  - comments: begining with an octothorpe (also called a “hash”, “sharp”, “pound” or “number sign” - `#`)
  - flow styles: using explicit indicators rather than indentation to denote scope
  - flow sequence: written as a comma separated list within square brackets
  - flow mapping: useing curly braces.
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
    - first identified by an anchor (marked with the ampersand - “&”)
    - aliased (referenced with an asterisk - `*`) thereafter
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

    # Node for “Sammy Sosa” appears twice in this document
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





