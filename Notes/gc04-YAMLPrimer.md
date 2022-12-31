# YAML Primer

Author: David Gidwani

Date: 2013-01-01

[Original](https://github.com/darvid/trine/wiki/YAML-Primer)


- Basic structures
  - mappings
    - synonymous with `map` in C++, associative `arrays` in PHP, and `dict` in Python

    ```yaml
    faction_A: FRIENDLY
    faction_H: FRIENDLY
    minlevel: 80
    maxlevel: 80
    ```

  - block sequences
    - simply lists or arrays of scalars or other structures

    ```yaml
    - Cloak of Displacement
    - Cloak of the Untamed Predator
    ```

  - inline sequences
    - sharing similar syntax for inline arrays/lists in other languages
    - not requiring scalars to be quoted unless they include characters that need escaping

    ```yaml
    npcflag: [GOSSIP, VENDOR]
    ```


- Using anchors
  - any YAML node able to be anchored and referenced elsewhere as an alias node
  - `&name` of anchor: to anchor a particular value or set of values
  - `*name` of anchor: to reference an anchor
  - example

    ```yaml
    item:
      - method: UPDATE
        where: &FREE_ITEMS
          - Portable Hole
          - Light Feather
        SellPrice: 0
        BuyPrice: 0

    npc:
      - method: MERGE
        merge-from: {name: General Goods Vendor}
        items: *FREE_ITEMS
    ```





