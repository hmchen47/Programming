# Floating Point Tutorial

Institute: RF Wireless World

[Original](https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html)



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
    - mantissa: `0101_0000_0000_0000_0000_000` $\to$ (1.mantissa) =1.0101_0000_0000_0000_0000_000
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
            alt    = "IEEE 754 standard floating point Arithmetic"
            title  = "IEEE 754 standard floating point Arithmetic"
          />
        </figure>
      </div>





