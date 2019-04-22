# Conclusion and final exam

## Intro final exam

You will find questions (multiple choice, checkboxes, etc.) related to Module 5 (exercises 1 to 15) and also related to the entirety of the course (exercises 16 to 30).

As stated in the [grading policy page](https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2017/courseware/556d952aabbe47bfab3cb81ab3750995/d930f54cb59f4559aefb06307e5197ce/3?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2017%2Btype%40vertical%2Bblock%409a577b3a1ccd4ee28831cdc02ce9962a), this final exam counts towards 28% of your final grade.

## Exercises (1-5)

1. Number of fonts

    What is considered a good number of different fonts to use per page?

    1. 4 - 6
    2. 1 - 3
    3. 7 - 10

    Ans: 2 <br/>
    A best practice is to use one font the titles and another font for the body text.


2. Sans-serif

    Which of the following statements are true about fonts in the "sans-serif" category? (2 correct answers!)

    1. They do not have flourishes at the end of the letters.
    2. Each letter is the same width.
    3. They have extra flourishes to help them be more readable.
    4. They are the best choice for large blocks of digital text.

    Ans: 14


3. Serif or not serif

    Which of the following are examples of "serif" fonts in the CSS classification? (2 correct answers!)

    1. Arial
    2. Times New Roman
    3. Courier New
    4. Garamond

    Ans: 24 <br/>
    Arial is a sans-serif font and Courrier New is an example of a monospace font.


4. Courier New

    Which of the following statements are true about the font "Courier New"? (2 correct answers!)

    1. it is a sans-serif font
    2. it is a monospace font
    3. its letters are as tall as they are wide
    4. it is often used to display example code

    Ans: 24 <br/>
    The "Courier New" font mimics an old typewriter and is traditionally use for computer code.


5. Palette colors

    What is considered a good number of colors for a Web page's color palette?

    1. 3 - 4
    2. 5 - 6
    3. 1 - 2
    4. 7 - 8

    Ans: 1 <br/>
    Colors can be used to make things stand out, but it only works if there are not too many colors.


## Exercises (6-10)

6. Text block width

    What is the ideal width for a text block to prevent user fatigue while reading?

    1. 80 - 100 characters wide
    2. 25 - 25 characters wide
    3. 50 - 75 characters wide
    4. 15 - 20 characters wide

    Ans: 3 <br/>
    Long lines make it difficult for your eyes to return to the start of the next line. So a best practice would be to limit lines of text to 50-75 characters wide, that is about 10 to 12 words per line.


7. Web accessibility

    Which users benefit from an accessibly designed Web page? (More than one answer possible!)

    1. People using older computers with low bandwidth and other limitations.
    2. People who are not fluent in the language of your particular Web site.
    3. People with temporary situational limitations, such as a broken arm.
    4. People living with physical limitations such as low-vision or color blindness.
    5. People using mobile devices, and other diverse access channels.

    Ans: 12345 (x1235)<br/>
    Web accessibility addresses all disabilities, including hearing, learning and cognitive, neurological, physical, speech, and visual disabilities. And also, Web accessibility helps for temporary situational limitations.


8. Accessibility improvements

    Which of the following are examples of accessibility improvements for a Web page? (2 correct answers!)

    1. A title element that briefly describes the content of the page
    2. Monospace fonts
    3. Alt text applied to images that describes the image
    4. Using HTML tables for formatting
    5. Using color exclusively to indicate interactive elements on the page

    Ans: 13 <br/>
    Explanation
        + Monospace fonts don't usually improve the readibility.
        + HTML tables are good for tabular data, but using them for formatting hides the logical order of elements.
        + Using only color can pose problems for people with color blindness, and often doesn't provide enough contrast.


9. Inclusive color palette

    Which of the following best describes how to choose an inclusive color palette?

    1. Analogous colors that are all in the same shade and tone so as to not fatigue users.
    2. A wide range of colors allowing for numerous options from all sides of the color wheel to accomodate different types of color-blindness.
    3. A small collection of colors that are highly contrasting, choosing at least one from the warmer color group and one from the cooler color group.
    4. Colors that are well coordinated according to "complimentary" colors located across the color wheel from one another.

    Ans: 3 <br/>
    Explanation
        + Colors that are too similar do not provide the contrast needed.
        + If you use a wide range of colors, there will also be colors among them that are hard to distinguish.
        + Complementary colors are not enough. You also need to give them different contrast.


Use this image of an interactive HTML page to answer question 10:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/71aae70f3f7f4bb0b8b039f7b0249e7d/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4042df4701e26e4d3b8b4e3d5c726224c3">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7908d82984cf540ae86152e558802b66/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/new-boutons-exo10.png" style="margin: 0.1em;" alt="Diagram for Final Exam Q10 - Image of an interaction with a green button and a red button" title="Diagram for Final Exam Q10" width="350">
  </a></div>
</div>


10. Inclusive interaction

    Which of the following is the best way to make the above interaction more inclusive while keeping a pleasing design?

    1. Include symbols/text as well as colors to accomodate those that cannot differentiate between red and green.
    2. Take away all color and leave the interaction black and white to provide optimum contrast.
    3. Add alt text to the buttons so those using a screen reader will understand which button is green and which is red.
    4. Change the colors of the buttons from red and green to blue and orange to accomodate those with different types of color-blindness.

    Ans: 1 <br/>
    It is not necessary to remove color as long as there are alternative ways to distinguish the buttons, such as shape and/or text.


## Exercises (11-15)

11. Low vision

    What is the best font size to accomodate users with low vision?

    1. Using at most 16pt, so when using a screen zoom fonts aren't overly exaggerated.
    2. Using at least 1em, so the font can grow and shrink based on user settings.
    3. Using at least 18px, so that fonts are displayed in relation to screen resolution.
    4. Using at least 12pt, so fonts cannot display smaller than typical printed text.

    Ans: 2 <br/>
    Setting any fixed font size means that some people will have to zoom! It is better to use 1em so people automatically get the font size they prefer.


12. Internationalization

    Which of the following are ways to make your site more accessible for international users? (2 correct answers!)

    1. Use ASCII characters to allow for non roman characters.
    2. Use UTF-8 character encoding to accomodate a wide range of language symbols.
    3. Declare the language of your page.
    4. Do not set the language of your page so that it can adapt accordingly.

    Ans: 24 <br/>
    Explanation

        + UTF-8 ensures that people can use all scripts of the world, so that they can can put their name in a form.
        + Indicating the language of the page helps, among other things, automatic translation and search engines.


13. Outdated

    Which of the following Web design elements are considered "outdated" and should generally be avoided? (4 correct answers!)

    1. Automative scrolling (marquee)
    2. Cursive text
    3. HTML tables as a way to structure layout
    4. Infinitely scrolling Web pages
    5. Animated cursors
    6. Frames as a way to keep navigation bars static

    Ans: 1356 <br/>
    Explanation
        + Cursive text is old as writing itself, and not likely to go out of fashion.
        + And, "infinite scrolling is a new trend. Whether it is also good design still remains to be seen...", states Bert Bos.


14. Flat design

    Which of the following is the best description of the current trend of "flat design"?

    1. Clean color palettes limited to few colors that are analogous on the color wheel.
    2. Simple, minimalistic design with clean typography, simple elements in a well organized grid layout and 2D design without drop shadows.
    3. Simple Web layouts that use a long scrolling page with anchor links instead of multiple pages linked via a nav bar.
    4. Rich design that makes the elements of the page jump out as if they were 3D through use of beveled edges, drop shadows and gradients.

    Ans: 2 <br/>
    "Flat design" refers to the absence of pseudo-3D elements and uses simple, grid-like alignments. Flat design can be applied to long and short pages alike and use few or many colors.


15. Best tool

    Since the release of HTML5 in 2014, what is considered the best tool with which to structure your page?

    1. context-specific tags like header, nav or footer
    2. HTML tables
    3. div tags
    4. frames

    Ans: 1 <br/>
    Tables and frames should not be used to structure a Web page. <br/>
    Div tags can be used if there aren't any more specific elements to express a purpose, such as header, nav and footer.



## Exercises (16-20)



## Exercises (21-25)



## Exercises (26-30)



## Continue your studies


