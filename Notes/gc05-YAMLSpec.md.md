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





