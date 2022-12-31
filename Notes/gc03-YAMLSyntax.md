# YAML Syntax

Institute: Grav

[Original](https://learn.getgrav.org/17/advanced/yaml)


- Introduction to YAML
  - YAML = YAML Ain't Markup Language
  - to configuration what markdown is to markup
  - a human-readbale structured data format
  - less complex and ungainly than XML and JSON but providing similar capabilities
  - to provide powerful configuration settings, w/o having to learn a more complex code type like CSS, JavaScript and PHP


- YAML basic rules
  - end in `.yaml` / `.yml`
  - case sensitive
  - not allowing the use of tab, but space


- YAML data types
  - mappings: hashes/dictionaries
  - sequences: arrays / lists
  - scalars: strings / numbers


- Scalars data type
  - the strings and numbers that make up the data on the page
  - could be
    - boolean property: `true`
    - integer (number): `5`
    - string of text: a sentence or the title of your website
  - often called **variables** in programming
  - most scalars unquoted
  - string w/ punctuation or other elements that can be confused w/ YAML syntax (dashes, colon, etc.) $\to$ quote this data using single `'` or double `"` marks
  - examples

    ```yaml
    integer: 25
    string: "25"
    float: 25.0
    boolean: true
    ```


- Sequence data type
  - each item in the list placed in its own line w/ an open dash, e.g.,

    ```yaml
    - Cat
    - Dog
    - Goldfish
    ```

  - nested sequence w/ items and subitems
  - YAML using spaces, not tab, for indentation, e.g.,

    ```yaml
    -
      - Cat
      - Dog
      - Goldfish
    -
      - Python
      - Lion
      - Tiger
    ```

  - nesting sequences even deeper $\to$ adding more levels, e.g.,

    ```yaml
    -
      -
        - Cat
        - Dog
        - Goldfish
    ```





