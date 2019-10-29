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
      <img src="https://miro.medium.com/max/8398/1*V6HtclLD9vxjjn2mPZbRug.jpeg" style="margin: 0.1em;" alt="Semiconservative, conservative, and dispersive models of DNA replication make different predictions about the distribution of DNA strands after replication. Yellow strands indicate 15N (heavy) segments of DNA, and black strands indicate ¹⁴N (light) segments. The Meselson-Stahl experiment began with DNA consisting of 100% 15N." title="Semiconservative, conservative, and dispersive models of DNA replication replication" width=450>
    </a>
  </div>

  + Semiconservative, conservative, and dispersive models of DNA replication make different predictions about the distribution of DNA strands after replication. Yellow strands indicate 15N (heavy) segments of DNA, and black strands indicate ¹⁴N (light) segments. The Meselson-Stahl experiment began with DNA consisting of 100% ¹⁵N.

+ The most beautiful experiment in biology (1958)
  + Meselson & Stahl's insight: one isotope of nitrogen, Nitrogen-14 (¹⁴N), is lighter and more abundant than Nitrogen-15 (¹⁵N)
  + Meselson and Stahl grew E. coli for many rounds of replication in a ¹⁵N medium, which caused the bacteria to gain weight as they absorbed the heavier isotope into their DNA. When they were confident that the bacterial DNA was saturated with ¹⁵N, they transferred the heavy E. coli cells to a less dense ¹⁴N medium
  + Key point: any of daughter DNA would be lighter
  + __STOP:__ After one round of replication, Meselson & Stahl spun the DNA in a centrifuge.  Why?
    + conservative model eliminated, both daughter DNA w/ same weights
  + __STOP:__ What would we observe in centrifuge for the other two models of replication?
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
  + [Vibrio cholerae genome](http://bioinformaticsalgorithms.com/data/realdatasets/Replication/Vibrio_cholerae.txt)

+ Finding hidden message
  + The Hidden Message Problem
    + Input: a string of _text_ (representing _ori_)
    + Output: a hidden message in text
  + __STOP:__ is the Hidden Message Problem a computational problem?

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
  + __STOP:__ would it make sense for an organism to have multiple DnaA boxes, or just one?
    + Answer: multiple DnaA boxes $\to$ higher chance of binding $\to$ high "fitness"
  + "Nothing in biology makes sense expect in the light of evolution." -- Theodosius Dobzhansky


## 1.3 Hunting for Frequent Words

+ Counting words
  + looking for surprisingly frequent substrings (contiguous strings appearing within) this _ori_
  + first, let's count how often a given substring occurs

+ Counting word problem
  + Substring Counting Problem
    + Input: a string _pattern_ and a longer string _text_
    + Output: the number of times _pattern_ occurs in text
  + __STOP:__ how many times does `ATA` occur in `CGATATATCCATAG`?
    + Answer: could be 2 or 3. for this application, count as 3, i.e., count overlaps

+ Substring indexing
  + key point: think of a string as just an array of symbols (0-indexing)
  + notation for the substring `ATA` in text["CG<span style="color:red; weright: bold;">ATA</span>TATCCATAG"] is `text[2, 5]`
    + why not `text[2, 4]`?
  + __STOP:__ how would refer the substring  `CGA` in text["<span style="color:red; weright: bold;">CGA</span>TATATCCATAG"]?
    + Answer: `text[0, 3]`
  + __STOP:__ What do you notice?
    + Answer: easily get _length_ of the substring by subtracting the lower index from the upper index; eg, $3-0 = 3$
  + __STOP:__ how would we refer to the substring of text of length $k$ starting at position $i$?
    + Answer: `text[i, i+k]` $\to$ very useful
  + using same notation for "subarray" if we want to refer to a contiguous collection of values in an array

+ Idea for counting patterns

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/9336/1*dofjb4KZgaPGtVsU8VLdVw.jpeg" style="margin: 0.1em;" alt="“slide a window” down text, checking whether each length-k substring of text matches pattern, and adding one to a count variable every time we encounter a match" title="Illustriation of sliding window to check substring with k=3" width=300>
    </a>
  </div>

  + Sliding a window to compute `PatternCount(text, pattern) = 3` for pattern = “ATA” and text = “CGATATATCCATAG”
  + initializing count to zero and then increment it each time that pattern appears in text (shown in green)

  + __STOP:__ how many substrings of length $k$ are there in a string of length $n$?
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
  + __k-mer pattern:__ a <span style="color: darkgreen; weight: bolder;">most frequent k-mer</span> in a string if no other k-mer is more frequent than _pattern_
  + Frequent Word Problem
    + Input: a string $text$ and an integer $k$
    + Output: all most frequent k-mers in text
  + __STOP:__ is the problem clearly stated?
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
        <img src="https://miro.medium.com/max/4225/1*MlojMRrjuYxdNrTr3ofduA.jpeg" style="margin: 0.1em;" alt="The count array for text = ACGTTTCACGTTTTACGG and k = 3. For example, count[0] = 3 because the 3-mer starting at position 0 (ACG) appears three times in text (at positions 0, 7, and 14). Accordingly, count[7] and count[14] are both equal to 3 as well." title="Demo of one frequent words solution" width=350>
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
  + __STOP:__ this algorithm is inefficient, why? can we make it better?
  

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

  + __STOP:__ what do you see?

+ Complementarity of DNA
  + DNA is double-stranded, and the two strands are _reverse complements_ of each other

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/3288/1*0v93SJyADZas0gOW_XbJnA.jpeg" style="margin: 0.1em;" alt="Complementary strands run in opposite directions" title="Complementary strands run in opposite directions" width=300>
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
  + __STOP:__ Write pseudocode for the Reverse and Complement functions.

+ Hidden messages found
  + "ATGATCAAG" and "CTTGATCAT": reverse complement
  + likely DnaA boxes (DnaA not knowing which strand it binds to)
  + very surprising to find a 9-mer appearing 6 or more times (w/ reverse complement) within ~500 nucleotides

+ Looking for other hidden messages?
  + __STOP:__ now that we know the "hidden message" in _Vibrio cholera_ , how would we look for a hidden message starting replication in other bacteria?
  
  
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

  + [Thermotoga petrophila genome](http://bioinformaticsalgorithms.com/data/realdatasets/Replication/Thermotoga_petrophila.txt)
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



## 1.6 An Explosion of Hidden Messages

+ Return to the first problem
  + found hidden messages if _ori_ id given, but still not knowing how to find _ori_ in (long) genome

+ Bacteria with unknown _ori_
  + __STOP:__ now that we know that "hidden messages" may differ, how could we look for _ori_ in a newly sequenced bacterial genome?

+ Finding _ori_ computationally
  + OLD strategy: given a previous __known__ _ori_ (500 nucleotide window), find __frequent words__ (clumps) in _ori_ s candidate DnaA boxes

    \[ \text{replicate origin} \to \text{frequent words} \]

  + NEW strategy: find frequent words in __ALL__ windows within a (3 million nucleotides) genome windows with __clumps__ of freqient words are candidate replication origins.

    \[ \text{frequent word} \to \text{replication origin} \]

+ Defining and hunting for clumps
  + A k-mer forms an `(L, t)-clump` inside Genome if there is a short (lenghth `L`) interval of Genome in which it appears many (at least `t`) times
  + Clump Finding Problem
    + Input: A string text, and integers `k` (length of pattern), `L` (window length), and `t` (number of patterns in a clump).
    + Output: All distinct k-mers forming `(L, t)-clumps` in text.
  + pseudocode

    ```js
    FindClumps(text, k, L, t)
      patterns = an array of strings of length 0
      n = len(text)
      for every integer i between 0 and n − L
          window = text[i, i + L]
          freqMap = FrequencyTable(window, k)
          for every key s in freqMap
              if freqMap[s] ≥ t and Contains(patterns, s) = false
                  patterns = append(patterns, s)
      return patterns
    ```

  + a complicated function cn be made easier by using subroutines as building blocks
  + STOP (biologist only): why is looking for clumps in bacterial genomes as a source of hidden messages destined to fail?

+ Issues
  + Genomes have too many __repeats__, some more useful than others. eg., Alu in human is ~300 bp long and occurs (with some changes) 1 million times
  + In E. Coli, 1900+ different 9-mer form `(500, 3)-clumps`.  It is unclear which ones point to _ori_ ...


## 1.7 A Surprise, Some Gritty Details about Replication

+ A surprising pattern in nucleotide counts
  + a very simple computational analysis: take a frequency of each nucleotide in 100,000 nucleotide windows of E. Coli (verified _ori_)
  + why would there be more C on half the genome? (left figure)
    + The frequency of cytosine in each of 46 equal-length disjoint windows (of approximately 100,000 nucleotides each) covering the E. coli genome. 
    + The replication terminus is located at position 0, whereas the replication origin site is located approximately 2.3 million nucleotides away, halfway down the genome.
  + why would be the story be opposite when we count G's? (middle left figure)
    + The frequency of guanine in the same 46 windows in the E. coli genome. 
    + Half of the genome has windows that tend to have low guanine frequency, and half of the genome has windows with high frequency. 
    + The picture is reversed from the preceding figure and the consideration of cytosine.
  + the pattern is even more stark if we take the difference between frequency of G and the frequency of C (middle right figure)
    + the difference between the frequencies of guanine and cytosine across the 46 windows of the E. coli genome
    + assuming that the genome begins at the experimentally verified replication terminus of E. coli.
  + the pattern still there even if we didn't know where _ori_ was and start counting at some arbitrary spot
    + The difference between the frequencies of guanine and cytosine across the 46 windows of the E. coli genome, starting at an arbitrary location of the genome. 
    + still infer the location of the replication origin as the point at which the guanine-cytosine difference passes from negative to positive, which in the figure above is approximately 3.9 million nucleotides into the genome file.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/2400/1*tKwZsS82wHPmuCrE3f0pLw.jpeg" style="margin: 0.1em;" alt="The frequency of cytosine in each of 46 equal-length disjoint windows (of approximately 100,000 nucleotides each) covering the E. coli genome. The replication terminus is located at position 0, whereas the replication origin site is located approximately 2.3 million nucleotides away, halfway down the genome." title="The frequency of cytosine" height=150>
      <img src="https://miro.medium.com/max/2416/1*guLngFfCJRN-4GbLRZpwyQ.jpeg" style="margin: 0.1em;" alt="The frequency of guanine in the same 46 windows in the E. coli genome. Half of the genome has windows that tend to have low guanine frequency, and half of the genome has windows with high frequency. However, the picture is reversed from the preceding figure and the consideration of cytosine." title="The frequency of guanine" height=150>
      <img src="https://miro.medium.com/max/2416/1*o1Sa7yHnp0joFU5nd8JwGQ.jpeg" style="margin: 0.1em;" alt="The difference between the frequencies of guanine and cytosine across the 46 windows of the E. coli genome, assuming that the genome begins at the experimentally verified replication terminus of E. coli." title="The difference between the frequencies of guanine and cytosine" height=150>
      <img src="https://miro.medium.com/max/2429/1*-Slxg4qjOvnwPWJZ4Rxa3g.jpeg" style="margin: 0.1em;" alt="The difference between the frequencies of guanine and cytosine across the 46 windows of the E. coli genome, starting at an arbitrary location of the genome. We can still infer the location of the replication origin as the point at which the guanine-cytosine difference passes from negative to positive, which in the figure above is approximately 3.9 million nucleotides into the genome file." title="The location of the replication origin as the point at which the guanine-cytosine difference passes from negative to positive" height=150>
    </a>
  </div>

+ The process of DNA replication
  + DNA strands have directions (top left figure)
  + DNA Polymerases do the Job of Copying (top middle figure)
    + Once the DNA strands are pulled apart the process of replication begins.
    + DNA proceeds in both directions on both strands and continues until the center of termination, terC, is reached.
  + the replication process starts in one direction
    + Beginning at the oriC locus the DNA molecule is pulled apart and two DNA polymerases, one on each strand begin copying on each strand.
  + Once the replication fork is opened far enough (bottom left figure)
    + This open region of single-stranded DNA eventually allows a second phase of the replication process to begin.
    + A second DNA polymerase detects a primer sequence, and then start replicating the exposed sequence Ahead of it and works towards the beginning of the previous replication primer. 
    + This DNA polymerase does not have too far to go.
  + When Opened a Little More (bottom middle figure)
    + As the initial, or Leading, polymerase continues to copy its half strand more of the complement strand is exposed, which sets off the process over and over again until the termination center is reached.
  + Eventually the whole genome is replicated
    + The lengths of Okazaki fragments in prokaryotes and eukaryotes differ. Prokaryotes have Okazaki fragments that are quite longer than those of eukaryotes. Eukaryotes typically have Okazaki fragments that are 100 to 200 nucleotides long, whereas prokaryotic E. Coli can be 2,000 nucleotides long.
  + [More detailed explanation slide 30-40](https://slideplayer.com/slide/4666399/)

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://www.csbio.unc.edu/mcmillan/Comp555S16/Lecture03.html" ismap target="_blank">
      <img src="http://www.csbio.unc.edu/mcmillan/Comp555S16/Media/DirectionalDNA.png" style="margin: 0.1em;" alt="Recall DNA Strands have Directions" title="DNA with directions" height=150>
      <img src="http://www.csbio.unc.edu/mcmillan/Comp555S16/Media/WrongModel.png" style="margin: 0.1em;" alt="Once the DNA strands are pulled apart the process of replication begins. It proceeds in both directions on both strands and contines until the center of termimination, terC, is reached." title="DNA Polymerases do the Job of Copying" height=150>
      <img src="http://www.csbio.unc.edu/mcmillan/Comp555S16/Media/RepStarts.png" style="margin: 0.1em;" alt="Beginning at the oriC locus the DNA molecule is pulled apart and two DNA polymerases, one on each strand begin copying on each strand." title="The replication process starts in one direction" height=150>
    </a>
  </div>
  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://www.csbio.unc.edu/mcmillan/Comp555S16/Lecture03.html" ismap target="_blank">
      <img src="http://www.csbio.unc.edu/mcmillan/Comp555S16/Media/Strand2.png" style="margin: 0.1em;" alt="This open region of single-stranded DNA eventually allows a second phase of the replication process to begin. A second DNA polymerase detects a primer sequence, and then start replicating the exposed sequence Ahead of it and works towards the beginning of the previous replication primer. However, this DNA polymerase does not have too far to go." title="Once the replication fork is opened far enough" height=150>
      <img src="http://www.csbio.unc.edu/mcmillan/Comp555S16/Media/Continue.png" style="margin: 0.1em;" alt="As the initial, or Leading, polymerase continues to copy its half strand more of the complement strand is exposed, which sets off the process over and over again until the termination center is reached." title="When Opened a Little More" height=150>
      <img src="http://www.csbio.unc.edu/mcmillan/Comp555S16/Media/FinishedRep.png" style="margin: 0.1em;" alt="The lengths of Okazaki fragments in prokaryotes and eukaryotes differ. Prokaryotes have Okazaki fragments that are quite longer than those of eukaryotes. Eukaryotes typically have Okazaki fragments that are 100 to 200 nucleotides long, whereas prokaryotic E. Coli can be 2,000 nucleotides long." title="Eventually the whole genome is replicated" height=150>
    </a>
  </div>

+ [Bioalgorithms - UNC CS course](http://www.csbio.unc.edu/mcmillan/index.py?run=Courses.Comp555S19)

+ Different lifestyle of half-strands
  + the leading half-strand lives a double-stranded life most of the time
  + the lagging hak=lf-strand spends a large portion of its life-stranded, waiting to be replicated
  + why would a computer scientist care?



## 1.8 Replication Asymmetry Leads to the Replication Origin

+ Asymmetry of replication affects nucleotide frequency
  + single-stranded DNA w/ a much higher mutation rate than double-stranded
  + if one nucleotide w/ a greater mutation rate $\to$ observe its shortage on the lagging half-stranded (more often single-stranded)
  + the process is random

+ Deamination: the answer
  + deamination: cytosine (C) mutates into thymine (T)
  + deamination rate rises 100-fold when DNA is single-stranded!
  + A mutation of a cytosine nucleotide to a thymine nucleotide on a lagging half-strand (see diagram)
  + lagging half-strand (single-stranded): shortage of C, normal G
  + leading half-strand (double-stranded): shortage of G, normal C

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/2783/1*3U0QXsI-FHfkygJ1fTj_hw.jpeg" style="margin: 0.1em;" alt="A mutation of a cytosine nucleotide to a thymine nucleotide on a lagging half-strand will cause DNA polymerase to pair the new thymine with an adenine, thus reducing the amount of guanine present on the leading half-strand as well in the daughter chromosome." title="A mutation of a cytosine nucleotide to a thymine nucleotide on a lagging half-strand" width=350>
    </a>
  </div>

+ Skew array/diagram
  + __skew array:__ `Skew[k] = #G - #C` for the first $k$ nucleotides of genome
  + __skew diagram:__ plot `Skew[k]` against $k$ (see left diagram)
  + __STOP:__ what will skew array of a bacterial genome look like?
  + skew diagram of E. Coli (right diagram_)
    + walk along the genome and see that `#G - #C` have between decreasing and then suddenly start increasing 
    + where are _ori_ in genome?

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://medium.com/programming-for-lovers/chapter-1-finding-replication-origins-in-bacterial-genomes-31725266f179" ismap target="_blank">
      <img src="https://miro.medium.com/max/2399/1*y8ethNaZgkiD3YY_gd48Eg.jpeg" style="margin: 0.1em;" alt="The skew diagram for genome = CATGGGCATCGGCCATACGCC" title="The skew diagram for genome" width=350>
      <img src="https://miro.medium.com/max/2362/1*Inj1VFoP13nDCjGfhiomuA.jpeg" style="margin: 0.1em;" alt="The skew diagram for E. coli achieves a maximum and minimum at positions 1550413 and 3923620, respectively." title="The skew diagram for E. coli: ori at position around 4,000,000" width=350>
    </a>
    </a>
  </div>

+ First question solved
  + Q: given a bacterial genome (~3 Mbp), where is _ori_?
  + Minimum Skew Problem
    + Input: a DNA string genome
    + Output: the minimum value of `Skew[k]` for genome
  + Ref: Analyzing genomes with cumulative skew diagrams, Nucleic Acids Reviews, 1998

+ Issue
  + the replication of origin found
  + but, there are no frequent 9=mers (that appear 3 or more times) in the region of E. coli
  + __STOP:__ any idea? should we give up?

+ Accounting for point mutation
  + frequent 9-mers (w/ 1 Mismatch and Reverse Complements) in putative _ori_ of E. coli
  + complications
    + some bacteria w/ fewer DnaA boxes
    + terminus of replication often not located directly opposite of _ori_
    + the skew diagram often more complex than in the case of E. coli (see diagram)
  + Moral?<br/>
    This division is not an appropriate view of how biology (or science in general) can and should operate in 21st Century.


