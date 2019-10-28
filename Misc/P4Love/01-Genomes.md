# Chapter 1: Finding Replication Origins in Bacterial Genomes

## 1.1 An Intro to DNA Replication

+ A Prophetic One-Liner (1953)
  + "It has not escaped our notice that the specific pairing we have postulated immediately suggests a possible copying mechanism for the genetic material." - James Watson & Francis Crick
  + The copying mechanism

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/13606/1*eMwmX19umdv5YL5-cJu1gQ.jpeg" style="margin: 0.1em;" alt="Watson and Crick’s hypothesized view of DNA replication, with template strands shown in green and complementary strands shown in yellow. Nucleotides adenine (A) and thymine (T) are complements of each other, as are cytosine (C) and guanine (G). Complementary nucleotides on opposing strands of DNA bind to each other." title="Watson and Crick’s hypothesized view of DNA replication" width=350>
    </a>
  </div>

  + Watson and Crick’s hypothesized view of DNA replication, with template strands shown in green and complementary strands shown in yellow. Nucleotides adenine (`A`) and thymine (`T`) are complements of each other, as are cytosine (`C`) and guanine (`G`). Complementary nucleotides on opposing strands of DNA bind to each other.
  
+ Three hypothesis of DNA replication
  + semiconservative hypothesis
    + Watson and Crick’s suggestion
    + each parent strand acts as its own template for the synthesis of a complementary strand
  + conservative hypothesis
    + the entire double-stranded parent DNA molecule serves as a template for the synthesis of a new DNA molecule
    + one molecule with two parent strands and another with two daughter strands
  + dispersive hypothesis
    + some mechanism breaks the DNA backbone into pieces and splices intervals of synthesized DNA
    + each of the four resulting strands is a patchwork of parent and daughter DNA.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/8398/1*V6HtclLD9vxjjn2mPZbRug.jpeg" style="margin: 0.1em;" alt="Semiconservative, conservative, and dispersive models of DNA replication make different predictions about the distribution of DNA strands after replication. Yellow strands indicate 15N (heavy) segments of DNA, and black strands indicate ¹⁴N (light) segments. The Meselson-Stahl experiment began with DNA consisting of 100% 15N." title="Semiconservative, conservative, and dispersive models of DNA replication replication" width=350>
    </a>
  </div>

+ The most beautiful experiment in biology (1958)
  + Meselson & Stahl's insight: one isotope of nitrogen, Nitrogen-14 (¹⁴N), is lighter and more abundant than Nitrogen-15 (¹⁵N)
  + Meselson and Stahl grew E. coli for many rounds of replication in a ¹⁵N medium, which caused the bacteria to gain weight as they absorbed the heavier isotope into their DNA. When they were confident that the bacterial DNA was saturated with ¹⁵N, they transferred the heavy E. coli cells to a less dense ¹⁴N medium
  + Key point: any of daughter DNA would be lighter
  + STOP: After one round of replication, Meselson & Stahl spun the DNA in a centrifuge.  Why?
    + conservative model eliminated, both daughter DNA w/ same weights
  + STOP: What would we observe in centrifuge for the other two models of replication?
    + dispersive model eliminated, all of them w/ the same weights
  
+ What a biologist sees

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://www.slideshare.net/veneethmathew/12-lecture-cellcycle-43264499" ismap target="_blank">
      <img src="https://image.slidesharecdn.com/12lecturecellcycle-150106201827-conversion-gate02/95/ch-12-cell-cycle-64-638.jpg?cb=1420575769 " style="margin: 0.1em;" alt="The precess of cell replicaton of its DNA (page 64)" title="The process of cell replication of its DNA" width=350>
    </a>
  </div>

+ What a computer scientist sees ...
  + __String:__ a contiguous collection of symbols
  + DNA string $\to$ complicated biological process $\to$ 

+ Origin of replication
  + __Replication of origin:__ bacterial genome replication begins in a single genomic region (denoted _ori_)
  + performed by molecular copy machines called DNA polymerases that attach free-floating nucleotides to the growing strand of DNA, in keeping with the semiconservative hypothesis
  + Objective: to determine where ori is hiding in the genome of a bacterium

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://pulpbits.net/4-dna-replication-animation/a-bacterial-dna-replication/" ismap target="_blank">
      <img src="https://pulpbits.net/wp-content/uploads/2013/11/bacterial-DNA-Replication-1024x689.jpg" style="margin: 0.1em;" alt="Origin of Replication" title="Origin of Replication" height=150>
      <img src="https://pulpbits.net/wp-content/uploads/2013/11/a-bacterial-dna-replication-728x324.jpg" style="margin: 0.1em;" alt="The precess of origin of  replication" title="The precess of origin of  replication" height=150>
    </a>
  </div> 

+ The finding _ori_ problem
  + Origin of Replication Problem
    + Input: A DNA string genome.
    + Output: The location of ori in genome.
  

+ Finding the origin of replication
  + how can we find _ori_ in a message?
  + Biologist: let's hack out this DNA fragment.  Can the genome replicate w/o it?
  + Computer scientist: I need more information before I hack this problem.

+ Looking for _ori_
  + verify _ori of vibrio cholera_, the bacterium that causes cholera (~500 nucleotides)

    > atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaac
    > ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca
    > cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgactt
    > gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt
    > acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga
    > tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat
    > tgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaag
    > atcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt
    > tccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc

  + there must be a hidden message telling the cell to start replication here

+ Finding hidden message
  + The Hidden Message Problem
    + Input: a string of _text_ (representing _ori_)
    + Output: a hidden message in text
  + STOP: is the Hidden Message Problem a computational problem?

+ Two scientific problems
  1. given a bacteria genome (~3 Mbp), where is _ori_?
  2. given _ori_ (~500 bp), what is the "hidden messages" saying that replication should start here?


## 1.2 Hidden Messages in the Replication Origin

+ Hidden Message Problem Revisited
  + The Hidden Message Problem
    + Input: a string of _text_ (representing _ori_)
    + Output: a hidden message in text
  + hidden message not defined
  + __DnaA:__ a protein mediating replication initiation
  + __DnaA box:__ a short segment in _ori_ where DnaA binds to, i.e., a hidden message saying "bind here!"
  + STOP: would it make sense for an organism to have multiple DnaA boxes, or just one?
    + Answer: multiple DnaA boxes $\to$ higher chance of binding $\to$ high "fitness"
  + "Nothing in biology makes sense expect in the light of evolution." -- Theodosius Dobzhansky


## 1.3 Hunting for Frequent Words

+ Counting words
  + looking for surprisingly frequent substrings (contiguous strings appearing within)n this _ori_
  + first, let's count how often a given substring occurs

+ Counting word problem
  + Substring Counting Problem
    + Input: a string _pattern_ and a longer string _text_
    + Output: the number of times _pattern_ occurs in text
  + STOP: how many times does `ATA` occur in `CGATATATCCATAG`?
    + Answer: could be 2 or 3. for this application, count as 3, i.e., count overlaps

+ Substring indexing
  + key point: think of a string as just an array of symbols (0-indexing)
  + notation for the substring `ATA` in text["CG<span style="color:red; weright: bold;">ATA</span>TATCCATAG"] is `text[2, 5]`
    + why not `text[2, 4]`?
  + STOP: how would refer the substring  `CGA` in text["<span style="color:red; weright: bold;">CGA</span>TATATCCATAG"]?
    + Answer: `text[0, 3]`
  + STOP: What do you notice?
    + Answer: easily get _length_ of the substring by subtracting the lower index from the upper index; eg, $3-0 = 3$
  + STOP: how would we refer to the substring of text of length $k$ starting at position $i$?
    + Answer: `text[i, i+k]` $\to$ very useful

+ Idea for counting patterns

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/9336/1*dPfjb4KZgaPGtVsU8VLdVw.jpeg" style="margin: 0.1em;" alt="“slide a window” down text, checking whether each length-k substring of text matches pattern, and adding one to a count variable every time we encounter a match" title="Illustriation of sliding window to check substring with k=3" width=350>
    </a>
  </div>

  + STOP: how many substrings of length $k$ are there in a string of length $n$?
    + Answer: $(n-k+1)$
  + Exercise: write pseudo code to count pattern occurrences.
  + pseudocode

    ```js
    PatternCount(pattern, text)
      count = 0
      for k = 0 to (text.len - pattern.len)
        if text[k, k+pattern.len] == pattern
          count++
      return count
    ```

    + `len()`: a (typically built-in) function determining the length (number of symbols) in a string; also works for counting elements in an array
    + `text.len`: an attribute to representing the length of the object text

+ The frequent words problem
  + __k-mer:__ a string of length $k$
  + __k-mer patter:__ a most frequent __k-mer__ in a string if no other k-mer is more frequent than _pattern_
  + Frequent Word Problem
    + Input: a string $text$ and an integer $k$
    + Output: all most frequent k-mers in text
  + STOP: is the problem clearly stated?
    + Answer: yes, no other statement required to clarify

+ Solving the Frequent Words Problem
  + Eg, if `text = "ACGTTTCACGTTTTACGG"` and $k = 3$, then the most frequent words are `ACG` and `TTT` (both occur 3 times)
  + Exercise: how to solve the problem w/ an array? what subroutines would be useful?
  + One frequent words solution
    1. create an array count of length `len(text) - k +1`
    2. for each `i`, set `count[i]` equal to the number of times `text[i, i_k]` appears in text
    3. take k-mers having the maximum values of `count[i]`
  + eg., `text = "ACGTTTCACGTTTTACGG"` and $k = 3$

    <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
      <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
        <img src="https://miro.medium.com/max/4225/1*MlojMRrjuYxdNrTr3PfduA.jpeg" style="margin: 0.1em;" alt="The count array for text = ACGTTTCACGTTTTACGG and k = 3. For example, count[0] = 3 because the 3-mer starting at position 0 (ACG) appears three times in text (at positions 0, 7, and 14). Accordingly, count[7] and count[14] are both equal to 3 as well." title="Demo of one frequent words solution" width=350>
      </a>
    </div>

    + count[0] = 3 because the 3-mer starting at position 0 (ACG) appears three times in text (at positions 0, 7, and 14)
    + count[7] and count[14] are both equal to 3 as well
  + pseudocode

    ```js
    FrequentWords(text, k)
      freqPatterns = an array of strings of length 0
      n = text.len
      count = array of integers of length n-k+1
      for i = 0 to n-k
        pattern[i] = text[i, i+k]
        count[i] = PatternCount(pattern, text)
      max = MaxArray(freqPatterns)
      for i = 0 to n-k
        if count[i] = max
          pattern = text[i, i+k]
          freqPatterns = Append(freqPatterns, pattern)
        freqPatterns = RemoveDuplicates(freqPatterns)
      return freqPatterns
    ```

  + __MaxArray:__ take maximum value in an array _A_
  + __RemoveDuplicates:__ remove duplicates from list _patterns_
  + STOP: this algorithm is inefficient, why? can we make it better?
  

## 1.4 A Faster Frequent Words Approach

+ Arrays/Slices store list of variables: frequency table for text and $k$

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/3327/1*Mr6KrtsUqhQ732SwYIljfg.jpeg" style="margin: 0.1em;" alt="A table corresponding to counting the number of occurrences of every 3-mer in text = ACGTTTCACGTTTTACGG" title="Demo of frequency table for text and 3" width=350>
    </a>
  </div>

+ What if the index is not integers?
  + making things easier when finding frequent words

    | Pattern | Count |
    |:-------:|:-----:|
    | "AA" | 17 |
    | "AC" | 4 |
    | "CG" | 15 |
    | "GA" | 23 |
    | ... | ... |

  + __map/dictionary:__ 
    + a generalized version of an array
    + an association of _keys_ and _values_
    + e.g., frequency table
  + the indices: arbitrary values (in this case, they are strings)
  + __key:__ the indices of a map
  + use a variable (said _freq_) to refer to the map
  + value access as arrays; eg., `freq["AG"]`
  + pseudocode

    ```js
    BetterFrequentWords(text, k)
      freqPatterns = an empty array
      freqMap = an empty map
      n = text.len
      for i = 0 to n-k+1
        pattern = text[i, i+k]
        if pattern not in freqMap
          freqMap[pattern] = 1
        else
          freqMap[pattern] ++
      maxCount = MaxMap(freqMap)
      for all keys in freqMap
        if freqMap[key] == maxCount
          freqPatterns = freqPatterns.append(key)
      return freqPatterns

      MaxMap(dict)
        m = 0
        for every key pattern in dict
          if dict[pattern] > m
            m = dict[pattern]
        return m
    ```

    + no `RemoveDuplicates()` and `Count()` required
    + much faster

  + shorten `BetterFrequentWords()` to have a more modular pseudocode amd improved `MaxMap()`

    ```js
    BetterFrequentWords(text, k)
      freqPatterns = an empty array
      freqMap = FrequencyMap(text, k)
      maxCount = MaxMap(freqMap)
      for all keys in freqMap
        if freqMap[key] == maxCount
          freqPatterns = freqPatterns.append(key)
      return freqPatterns

    FrequencyMap(text, k)
      freqMap = an empty map
      n = text.len
      for i = 0 to n-k+1
        pattern = text[i, i+k]
        if pattern not in freqMap
          freqMap[pattern] = 1
        else
          freqMap[pattern] ++
      return freqMap

    MaxMap(dict)
      m = 0
      firstTime = true
      for every key pattern in dict
        if firstTime = true or dict[pattern] > m
          firstTime= false
          m = dict[pattern]
      return m
    ```


## 1.5 Some Hidden Messages are Surprising than Others

+ Returning to _ori of Vibrio cholera_

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/4453/1*AFGmuIrjyAckddQJnZO7OA.jpeg" style="margin: 0.1em;" alt="The most frequent k-mers in the ori region of Vibrio cholerae for k from 3 to 9, along with the number of times that each k-mer occurs." title="The most frequent k-mers in the ori region of Vibrio cholerae with k=3~9" width=350>
    </a>
  </div>

  + STOP: what do you see?

+ Complementarity of DNA
  + DNA is double-stranded, and the two strands are _reverse complements_ of each other

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/3288/1*0v93SJyADZas0gOW_XbJnA.jpeg" style="margin: 0.1em;" alt="Complementary strands run in opposite directions" title="Complementary strands run in opposite directions" width=350>
    </a>
  </div>
  
  + a template strand "AGTCGCATAGT" and its complementary strand "ACTATGCGACT"

+ Reverse Complementary
  + Reverse Complement Problem
    + Input: A DNA string pattern.
    + Output: The reverse complement of pattern.
  + pseudocode

    ```js
    ReverseComplement(pattern)
      pattern1 = Reverse(pattern)
      pattern2 = Complement(pattern1)
      return pattern2

    ReverseComplement(pattern)
      return Complement(Reverse(pattern))
    ```

    + modularity: easier to read and debug
  + STOP: Write pseudocode for the Reverse and Complement functions.

+ Hidden messages found
  + "ATGATCAAG" and "CTTGATCAT": reverse complement
  + likely DnaA boxes (DnaA not knowing which strand it binds to)
  + very surprising to find a 9-mer appearing 6 or more times (w/ reverse complement) within ~500 nucleotides

+ Looking for other hidden messages?
  + STOP: now that we know the "hidden message" in _Vibrio cholera_ , how would we look for a hidden message starting replication in other bacteria?
  
  
+ Hidden message in Therotoga. peotrophila?

  > aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactga
  > aactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaa
  > ttacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaa
  > acaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggttt
  > ctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattca
  > agattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtat
  > ccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggta
  > agttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaa
  > cctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga

  + No occurrence of "ATGATCAAG" and "CTTGATCAT"
  + "CCTACCACC" and "GGATGGTGG" are candidate hidden message.

    > aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactga
    > aactaaaatggtaggtttGGTGGTAGGttttgtgtacattttgtagtatctgatttttaa
    > ttacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaa
    > acaaaCCTACCACCaaactctgtattgaccattttaggacaacttcagGGTGGTAGGttt
    > ctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattca
    > agattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtat
    > ccaagccgatttcagagaaacctaccacttacctaccacttaCCTACCACCcgggtggta
    > agttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaa
    > CCTACCACCtgcgtcccctattatttactactactaataatagcagtataattgatctga




