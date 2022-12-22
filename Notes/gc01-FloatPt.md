# Floating Point Tutorial

Institute: RF Wireless World

[Original](https://www.rfwireless-world.com/Tutorials/floating-point-tutorial.html)



- IEEE 754 Standard Floating Point Numbers
  - floating point binary world
    - 1 bit = sign bit(s).
    - 8 = Biased exponent bits (e)
    - 23 = mantissa (m)
  - decimal equivalent value

    \[ (-1)^S \times 1.m \times s^{(e-\text{bias})} \hspace{2em} \text{bias} = 2^{(e-1)} - 1\]

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





