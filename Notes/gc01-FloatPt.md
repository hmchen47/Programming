# Floating Point Tutorial

Institute: RF Wireless World

[Original](https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html)


## IEEE Standard Floating Point

- IEEE 754 Standard Floating Point Numbers
  - floating point binary world
    - 1 bit = sign bit(s).
    - 8 = Biased exponent bits (e)
    - 23 = mantissa (m)
  - decimal equivalent value
    - $E = 8$: single precision IEEE floating point format

    \[ (-1)^S \times 1.m \times s^{(e-\text{bias})} \hspace{2em} \text{bias} = 2^{(E-1)} - 1\]

    <div style="display: flex; justify-content: center;">
      <figure style="display: table; float: left; margin-right: 0.25em; align-item: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; height: 75px;"
          onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
          src    = "https://www.rfwireless-world.com/images/floating-point-fig1.jpg"
          alt    = "IEEE 754 Floating point standard floating point word"
          title  = "IEEE 754 Floating point standard floating point word"
        />
        <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
          IEEE 754 Floating point standard floating point word
        </figcaption>
      </figure>
      <figure style="display: table; float: right; margin-left: 0.25em; align-item: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; height: 250px;"
          onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
          src    = "https://www.rfwireless-world.com/images/floating-point-fig3.jpg"
          alt    = "'1' is hidden in the representation of IEEE 754 floating point word, since it takes up an extra bit"
          title  = "'1' is hidden in the representation of IEEE 754 floating point word, since it takes up an extra bit"
        />
      </figure>
    </div>

  - examples
    - mantissa: `0101_0000_0000_0000_0000_000` $\to (1.\text{mantissa}) =1.0101_0000_0000_0000_0000_000$
    - floating point $X1$

    <div style="display: flex; justify-content: center;">
      <figure style="display: table; float: left; margin-right: 0.25em; align-item: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; height: 55px;"
          onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
          src    = "https://www.rfwireless-world.com/images/floating-point-fig4.jpg"
          alt    = "Sign bit (S1) =0. Biased Exponent (E1) =1000_0001 (2) = 129(10). Mantissa (M1) =0101_0000_0000_0000_0000_000"
          title  = "Sign bit (S1) =0. Biased Exponent (E1) =1000_0001 (2) = 129(10). Mantissa (M1) =0101_0000_0000_0000_0000_000"
        />
      </figure>
      <figure style="display: table; float: right; margin-left: 0.25em; align-item: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; height: 250px;"
          onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
          src    = "https://www.rfwireless-world.com/images/floating-point-fig5.jpg"
          alt    = "IEEE 754 standard floating point conversions"
          title  = "IEEE 754 standard floating point conversions"
        />
      </figure>
    </div>


- Decimal to IEEE 754 standard floating point
  - converting 286.75 to standard floating point
  - procedure: find the Sign, exponent and mantissa bits
    1. represting decimal number, $286.75_{(10)}$ to binary format

      \[ 286.75_{(10)} = 1\;0001\;1110.11_{(2)} \]

    2. normalizing binary number by shifting decimal point to get a "1" at the very end 
         - mantissa treated as fractional fixed point binary number
         - normalization: the process in which mantissa bits are either shifted right or to the left (add or subtract the exponent accordingly) s.t. the most significant bit is "1"
         - $\text{mantissa} = 0001\;1110\;1100\;0000\;0000\;000$

      <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
          onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
          src    = "https://www.rfwireless-world.com/images/floating-point-fig6.jpg"
          alt    = "Normalizing binary number"
          title  = "Normalizing binary number"
        />
      </figure>

    3. computing bias: $\text{bias} = 2^{(E-1)} - 1 = 2^{8-1} -1 = 127$ where $E = 8$ for single precision IEEE floating point format
    4. retrieving biased exponent $e$
         - obtained after normalizing in setp 2 w/ bias
         - $e = 8 + bias = 8 + 127 = 135 = 1000\;0111_{(2)}$
    5. final result

      <div style="display: flex; justify-content: center;">
        <figure style="display: table; float: left; margin-right: 0.25em; align-item: center;">
          <img style="margin: 0.1em; padding-top: 0.5em; height: 75px;"
            onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
            src    = "https://www.rfwireless-world.com/images/floating-point-fig7.jpg"
            alt    = "Standard floating point binary word of 286.75"
            title  = "Standard floating point binary word of 286.75"
          />
        </figure>
        <figure style="display: table; float: right; margin-left: 0.25em; align-item: center;">
          <img style="margin: 0.1em; padding-top: 0.5em; height: 100px;"
            onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
            src    = "https://www.rfwireless-world.com/images/floating-point-fig8.jpg"
            alt    = "Converting decimal value to standard floating point binary word"
            title  = "Converting decimal value to standard floating point binary word"
          />
        </figure>
      </div>


## IEEE 754 Standard Floating Point Arithmetic

- Arithmetic operands
  - considering the IEEE 754 floating point format numbers $X1$ & $X2$

    <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
        onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
        src    = "https://www.rfwireless-world.com/images/floating-point-fig9.jpg"
        alt    = "Two floating point numbers"
        title  = "Two floating point numbers"
      />
    </figure>

  - $S1$, $S2$: Sign bits of number $X1$ & $X2$
  - $E1$, $E2$: Exponent bits of number $X1$ & $X2$
  - $M1$, $M2$: Mantissa bits of Number $X1$ & $X2$


- Multiplication algorithm
  - multiplication

    \[
        \begin{aligned}
          X3 &= X1 \times X2 \\
             &= (-1)^{S1} (M1 \cdot 2^{E1}) \times (-1)^{S2} (M2 \cdot 2^{E2})
        \end{aligned}
    \]

  - procedure
    1. checking operands: one/both operands = 0 (all '0's) or $\infty$ (all '1's)
    2. sign bit: $S1 \text{ XOR } S2$
    3. mantissa: $M1 \cdot M2$ and truncating or rounding the results for 24 bits
    4. bias: $E = E1 + E2 - \text{bias}$
    5. exponent: normalizing the sum, shifting right to increase or shift left to decrease the exponent
    6. checking underflow/overflow: 0 $\to$ underflow; $\infty \to$ overflow
    7. $(E1 + E2 -\text{bias}) \ge E_{\max} \to \infty \hspace{1em}$ and $\hspace{1em} (E1 + E2 -\text{bias}) \le E_{\min} \to 0$
  - example
    - $X1 = 125.125$ and $X2 = 12.0625$ $\to X3= X1 * X2 = 1509.3203125$
    - floating point binary words

      <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
          onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
          src    = "https://www.rfwireless-world.com/images/floating-point-fig10.jpg"
          alt    = "Floating point binary words of X1 and X2"
          title  = "Floating point binary words of X1 and X2"
        />
      </figure>
    
    - procedure
      1. XOR sign: $X1 \text{ XOR } X2  = 0$
      2. mantissa:
          - multiply the mantissa values including the "hidden one": $\Rightarrow 24 \times 24 \to 48$
          - 2 bits to the left of binary point

          <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
            <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
              onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
              src    = "https://www.rfwireless-world.com/images/floating-point-fig11.jpg"
              alt    = "Resultant of multiplied mantissa"
              title  = "Resultant of multiplied mantissa"
            />
          </figure>

          - $M3 (48) = 1 \implies$ left shift the binary point and add "1" to the exponent
          - truncating the result to 24 bits and adding "1" to the final exponent
      3. exponent
          - range of the product is between $(1 - 3.9999999)$
          - normalization of the product simpler as the range of $M_A$ and $$ is between $1 - 1.9999999$
          - a 1 bit shift required with the adjust of exponent

        \[\begin{aligned}
          E3 &= E1 + E2 - \text{bias} + \text{(normalized exponent from step 2)} \\
             &= (1000\;0101)_2 + (1000\;0010)_2 - \text{bias} + 1 \\
             &= 133 + 130 - 127 + 1 = 137
        \end{aligned}\]

      4. final result: $X=1509.3203125$

          <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
            <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
              onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
              src    = "https://www.rfwireless-world.com/images/floating-point-fig12.jpg"
              alt    = "Floating point binary word of resultant of multiplication"
              title  = "Floating point binary word of resultant of multiplication"
            />
          </figure>


- Addition algorithm
  - addition

    \[\begin{aligned}
      X3 &= X1 \pm X2 \\
        &= (M1 \times 2^{E1}) \pm (M2 \times 2^{E2})
    \end{aligned}\]

  - procedure
    1. $X1$ and $X2$ addable w/ $E1 = E2$
    2. $|X1| \gt |X2|$, swap if necessary
    3. $E3 = \begin{cases} E1 & \text{if } E1 > E2 \\ E2 & \text{if } E1 < E2 \end{cases}$ 
    4. exponent difference: $E+{diff} = (E1 - E2)$
    5. left shift the decimal point of mantissa ($M2$) by the exponent difference $\to$ same exponent
    6. computing the sum/difference of the mantissa depends on the sign bit $S1$ and $S2$
        - $S1 == S2$: add mantissa
        - $S1 !- S2$: subtract mantissa
    7. normalizing $M3$ if required
    8. $ E3 = \begin{cases} \infty & E3 > E_{max} \;\text{ or overflow} \\ 0 & E3 < E_{min}\; \text{ or underflow} \end{cases}$
    9. $NaN$ not supported
  - example: $X1 = 9.75 \hspace{2em} X2 = 0.625$
    - floating point binary words

      <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
          onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
          src    = "https://www.rfwireless-world.com/images/floating-point-fig13.jpg"
          alt    = "Floating point binary words of X1 and X2"
          title  = "Floating point binary words of X1 and X2"
        />
      </figure>

    - procedure
      1. $|X1| > |X2|$: True
      2. $E3 = E1 = 1000\;0010 = 130_{(10)}$
      3. $E1 - E2 = (1000\;0010 - 0111\;1110) \implies (130-126)=4$
      4. shift the mantissa $M2$ by $(E1-E2)$

        <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
          <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
            onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
            src    = "https://www.rfwireless-world.com/images/floating-point-fig14.jpg"
            alt    = "Computing mantissa by shifting E1 - E2 to have same exponent"
            title  = "Computing mantissa by shifting E1 - E2 to have same exponent"
          />
        </figure>

      5. equal sign bits $\to$ add mantissa

        <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
          <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
            onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
            src    = "https://www.rfwireless-world.com/images/floating-point-fig15.jpg"
            alt    = "Adding mantissa of X1 and X2"
            title  = "Adding mantissa of X1 and X2"
          />
        </figure>

      6. no normalization required
      7. result: # X3 = 10.3125$

        <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
          <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
            onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
            src    = "https://www.rfwireless-world.com/images/floating-point-fig16.jpg"
            alt    = "Flating point binary word of X3"
            title  = "Flating point binary word of X3"
          />
        </figure>

      8. abstration: change $S2$ to $1$

        <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
          <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
            onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
            src    = "https://www.rfwireless-world.com/images/floating-point-fig17.jpg"
            alt    = "Flating point binary word of X3 w/ abstraction"
            title  = "Flating point binary word of X3 w/ abstraction"
          />
        </figure>


- Division algorithm
  - statement

    \[\begin{aligned}
      X3 &= (X1/X2) \\
        &= (-1)^{S1} (M1 \times 2^{E1}) / (-1)^{S2} (M2 \times 2^{E2}) \\
        &= (-1)^{S3} (M1/M2) 2^{(E1-E2)}
    \end{aligned}\]

  - procedure
    1. checking $X2 = 0 \implies X3 =\infty$ and $X1=X2=0 \implies NaN$
    2. $S3 = (S1 \text{XOR} S2)$
    3. $M3 = M1/M2$
    4. normalizing $M3$ if required
    5. checking overflow/underflow
        - $E3 > E_{\max} \to \infty$ or overflow
        - $E3 < E_{\min} \to \infty$ or underflow
  - example: $X1 = 127.03125 \hspace{2em} X2 = 16.9375$
    - floating point binary words

      <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
          onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
          src    = "https://www.rfwireless-world.com/images/floating-point-fig18.jpg"
          alt    = "Flating point binary word of X1 and X2"
          title  = "Flating point binary word of X1 and X2"
        />
      </figure>

    - procedure
      1. $S3 = S1 \text{ XOR } S2 = 0$
      2. $E3 = (E1 - E2) + \text{bias} = 133-131+127 = 129$
      3. dividing $M1/M2$

        <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
          <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
            onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
            src    = "https://www.rfwireless-world.com/images/floating-point-fig19.jpg"
            alt    = "Division of mantissa"
            title  = "Division of mantissa"
          />
        </figure>

      4. result: $X3 = 7.5$

        <figure style="display: flex; margin: 0.5em; justify-content: center; align-items: center;">
          <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
            onclick= "window.open('https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html')"
            src    = "https://www.rfwireless-world.com/images/floating-point-fig20.jpg"
            alt    = "Result of float point binary word"
            title  = "Result of float point binary word"
          />
        </figure>



## Tables of IEEE Floating Point Standard 

- IEEE 754 Floating point Standard

  <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 40vw;" cellspacing=0 cellpadding=5 border=1 align="center">
    <colgroup>
      <col style="width: 30%">
      <col style="width: 20%">
      <col style="width: 20%">
    </colgroup>
    <thead>
    <tr style="font-size: 1.0em; vertical-align:middle;">
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;"></th>
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">Single Precision</th>
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">Double Precision</th>
    </tr>
    </thead>
    <tbody>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">Word Length (bits)</td>
      <td style="text-align: center;">32</td>
      <td style="text-align: center;">64</td>
    </tr>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">Mantissa (bits)</td>
      <td style="text-align: center;">23</td>
      <td style="text-align: center;">52</td>
    </tr>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">Exponent (bits)</td>
      <td style="text-align: center;">8</td>
      <td style="text-align: center;">11</td>
    </tr>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">Bias</td>
      <td style="text-align: center;">127</td>
      <td style="text-align: center;">1023</td>
    </tr>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">Range</td>
      <td style="text-align: center;">3.8 x 10<sup>38</sup></td>
      <td style="text-align: center;">1.8 x 10<sup>308</sup></td>
    </tr>
    </tbody>
  </table><br/>


- IEEE 754 Number Representation Table

  <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 60vw;" cellspacing=0 cellpadding=5 border=1 align="center">
    <colgroup>
      <col style="width: 3%">
      <col style="width: 10%">
      <col style="width: 28%">
      <col style="width: 10%">
      <col style="width: 20%">
    </colgroup>
    <thead>
    <tr style="font-size: 1.0em; vertical-align:middle;">
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">Sign</th>
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">Exponent</th>
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">Mantissa (Significant)</th>
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">Number Representaion</th>
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">Comments</th>
    </tr>
    </thead>
    <tbody>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">0</td>
      <td style="text-align: center;"><code>0000 0000</code></td>
      <td style="text-align: center;"><code>0000 0000 0000 0000 0000 000</code></td>
      <td style="text-align: center;"><code>+/- 0</code></td>
      <td style="text-align: center;"></td>
    </tr>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">0</td>
      <td style="text-align: center;"><code>0000 0000</code></td>
      <td style="text-align: center;">
        None Zero<br/>
        <code>0000 0000 00000 0000 0000 001</code><br/>
        <code>0000 0000 00000 0000 0000 010</code><br/>
        <code>0000 0000 00000 0000 0000 011</code><br/>
        ...<br/>
        <code>1111 1111 11111 1111 1111 111</code>
      </td>
      <td style="text-align: center;"><br/>+1.4E-45<br/>+2.8E-45<br/>+4.2E-45<br/><br/>1.1754942E-38</td>
      <td>Denumalized number if the exponent is all zeros and Mantissa is non zero then the number represented are known as denormalized numbers. Other term is denormals</td>
    </tr>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">1</td>
      <td style="text-align: center;"><code>0000 0000</code></td>
      <td style="text-align: center;">Non Zero</td>
      <td style="text-align: center;"></td>
      <td>"- ive" Denomalized number</td>
    </tr>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">0</td>
      <td style="text-align: center;">1 ~ 254</td>
      <td style="text-align: center;">Any number</td>
      <td style="text-align: center;"></td>
      <td>"+ ive" Floating point number</td>
    </tr>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">1</td>
      <td style="text-align: center;">1 ~ 254</td>
      <td style="text-align: center;">Any number</td>
      <td style="text-align: center;"></td>
      <td>"- ive" Floating point number</td>
    </tr>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">0/1</td>
      <td style="text-align: center;"><code>1111 1111</code></td>
      <td style="text-align: center;">Zero</td>
      <td style="text-align: center;">+/- &infin;</td>
      <td style="text-align: center;"></td>
    </tr>
    <tr style="vertical-align:middle">
      <td style="text-align: center;">0/1</td>
      <td style="text-align: center;"><code>1111 1111</code></td>
      <td style="text-align: center;">Non Zero</td>
      <td style="text-align: center;">NaN</td>
      <td>"Not a Number"<br/>(0/0), (&infin;/&infin;), (0 x &infin;), etc. produce NaNs</td>
    </tr>
    </tbody>
  </table><br/>

