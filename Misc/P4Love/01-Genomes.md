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


### 1.2 Hidden Messages in the Replication Origin

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



