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


- Single precision examples
  - $2 = 1 \cdot 2^1 = 0100\;0000\;0000\;0000\;...\;0000\;0000_{(2)} = 4000\;0000_{(16)}$: sign bit = 0, stored exponent = 128 or $100\;0000\;0_{(2)}$, stored mantissa = $(1.)\;000\;0000\;...\;0000\;0000_{(2)}$
  - $-2 = -1 * 2^1 = 1100\;0000\;0000\;0000\;...\;0000\;0000_{(2)} = C000\;0000_{(16)}$: sign bit = 1, stored exponent = 128 or $100\;0000\;0_{(2)}$, stored mantissa = $(1.)\;000\;0000\;...\;0000\;0000_{(2)}$
  - $4 = 1 * 2^2 = 0100\;0000\;1000\;0000\;...\;0000\;0000_{(2)} = 4080\;0000_{(16)}$: sign bit = 0, stored exponent = 129 or $100\;0000\;1_{(2)}$, stored mantissa = $(1.)\;000\;0000\;...\;0000\;0000_{(2)}$
  - $6 = 1.5 * 2^2 = 0100\;0000\;1100\;0000\;...\;0000\;0000_{(2)} = 40C0\;0000_{(16)}$: sign bit = 0, stored exponent = 129 or $100\;0000\;1_{(2)}$, stored mantissa = $(1.)\;100\;0000\;...\;0000\;0000_{(2)}$, same exponent, mantissa is larger by half which, since this is a binary fraction, is $1-1/2$
  - $1 = 1 * 2^0 = 0011\;1111\;1000\;0000\;...\;0000\;0000_{(2)} = 3F80\;0000_{(16)}$: same exponent, mantissa is one less than 2 at 127, or $011\;1111\;1$
  - $.75 = 1.5 * 2^{-1} = 0011\;1111\;0100\;0000\;...\;0000\;0000 = 3F40\;0000$: biased exponent = 126 = 011\;1111\;0_{(2)}$, mantissa = $(1.)\;100\;0000\;...\;0000\;0000$, which is $1-1/2$
  - $2.5 = 1.25 * 2^1 = 0100\;0000\;0010\;0000\;...\;0000\;0000_{(2)} = 4020\;0000_{(16)}$: same as 2, except mantissa bit of $1/4$ set
  - $0.1 = 1.6 * 2^{-4} = 0011\;1101\;1100\;1100\;...\;1100\;1101 = 3DCC\;CCCD_{(16)}$:
    - $1/10$ is a repeating fraction in binary
    - mantissa is just shy of 1.6, and 
    - biased exponent says that 1.6 is to be divided by 16 
    - true exponent = $123 - 127 = -4$, which means that the factor by which to multiply is $2^{-4} = 1/16$
    - an attempt to represent the unrepresentable number as accurately as possible
  - $0 = 1.0 * 2^{-128} = 0000\;0000\;0000\;0000\;...\;0000\;0000_{(2)} = 0000\;0000_{(16)}$: a special case


- Other common floating-point errors
  - round-off error: 
    - not all bits used in calculation
    - example: adding 0.0001 to 0.9900 (Single Precision)
      - $0.0001$ represented as $(1.)10100011011011100010111 \times 2^{(-14+\text{Bias})}$ (13 Leading 0s in Binary!)
      - $0.9900$ represented as $(1.)11111010111000010100011 \times 2^{(-1+\text{Bias})}$
      - the decimal (binary) points must be aligned $\to$ un-normalized

      ```text
       .000000000000011010001101 * 2^0  <- Only 11 of 23 Bits retained
      +.111111010111000010100011 * 2^0
      ________________________________
      .111111010111011100110000 * 2^0
      ```

  - substracting two almost equal values
  - overflow and underflow
  - quantizing error - not exact form
  - division by a small number $\to$ divided by zero?
  - output errors






