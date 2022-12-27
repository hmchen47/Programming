# (Complete) Tutorial to Understand Floating-Point Errors

Institute: Microsoft

Date: 2005-08-16

[Original](https://www.betaarchive.com/wiki/index.php/Microsoft_KB_Archive/42980)


- Floating-point complications
  - decimal integer: exactly represented by a binary integer
  - fractional number: not able to exactly represented by a binary integer
  - fraction number ($p/q$) w/ $q = 2^n$: exactly represented by a floating point binary word
  - example: $a = 69.82 \ne b = 69.20 + 0.62$ in binary


- General floating-point concepts
  - binary floating point system: limited number of floating-point values
  - approximated by the closest representable value
  - IEEE standard "rounding" value to the "closest" representable value
  - goal of IEEE standard: maximizing accuracy w/ engineering calculations


- IEEE details
  - representation: $X = \text{Fraction} \times 2^{\text{ exponent - bias}}$
  - fraction:
    - normalized fractional part of the number
    - normalization: always w/ leading bit as "1" $\to$ implied bit
  - bias: 
    - avoid having to store negative exponent
    - bias value = 127 (single) / 1023 (double)






