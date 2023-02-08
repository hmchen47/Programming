# Converting HTML Code to Markdown Code

The project builds a simple Python program to convert the html code to markdown code. The markdown files are used for my personal learning and reading notes.  

The Python project intends for personal use only.


## Project Scope

The project builds an executable command to convert the embedded HTML code in markdown files.  The markdown files mainly contain two basic elements: figure and table.  The main purpose of the html code is to prettify the presentation of the markdown file.  

The markdown syntax is very limited whereas the figure cannot resize and the table is controlled the systems used.  When the reading and learning notes print out for review purpose, we can preview and print the files in browser with the help of extension, such as [Markdown Viewer](https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk?hl=en) for Chrome.  However, the extension is great for preview but not suitable for printing.  

The are a couple of ways to produce prettified printable files from the preview.  One simply way is to convert the preview file to HTML file.  Then, change the CSS style of the HTML file with a customized one. The customized CSS file uses media queries to handle the print layout.  However, the change of media queries have much restriction and difficult to product two columns per page.  

Alternatively, [`pandoc`](https://pandoc.org/) can convert markdown files to PDF via LaTeX.  The layout could be controlled by LaTeX heading file. The way to control layout of the print document is much simpler.  The use of pandoc is located under the `pandoc` folder with the file structure suggested form [Markdown Template: Latex-PDF](https://github.com/jaantollander/Markdown-Templates/tree/master/latex-pdf).

  ```shell
  pandoc
  ├── assets
  │   └── citation-style.csl
  ├── build
  │   ├── reading.pdf
  │   └── read.md
  ├── build.sh
  ├── content
  │   ├── bibliography.bib
  │   ├── images
  │   │   └── 800x400.png
  │   ├── index.md
  │   ├── literatural_note_template.md
  │   ├── reading.md
  │   └── SoftSkills.bib
  ├── layouts
  │   ├── ereader.tex
  │   ├── my_notes.tex
  │   ├── print.tex
  │   ├── reading.yml
  │   ├── reading.tex
  │   └── reading.yml
  ├── Makefile
  ├── Makefile.sh
  └── pandoc_manual
      ├── pandoc-manual1.html
      └── StylesB.css
  ```

The purpose of the directories of the file structure is linerated as following:

- `Makefile`: targets for pdf and html
- `build.sh`: original shell script
- `Makefile.sh`: original Makefile to call `build.sh`
- `assets`: style files
- `build`: the output files
- `content`: the input files
- `layouts`: the layout control files
- `pandoc_manual`: old version manual of pandoc w/ clear variable list


The difficulty is that `pandoc` cannot process HTML code embedded in markdown file.  The simple solution is to parse `figure` and `table` elements to standard markdown syntax and then replace these elements with the related markdown syntax.


## Arguments and Working Directory

The syntax of parsing program is descripted as below:

```sh
usage: html2md.py [-h] [-d DIR] [-o OUTPUT] [inputs ...]

Convert embedded HTML figures and tables code to markdown syntax

positional arguments:
  inputs                Markdown files to process

options:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     The folder to retrieve markdown files, the path also used to process local
                        diagrams
  -o OUTPUT, --output OUTPUT
                        Output markdown file for pandoc to process
```

There are two optional arguments:

1. `[-d DIR]`:
    - the folder `DIR` containing the markdown files to read in
    - default directory: `working` directory
2. `[-o OUTPUT]`:
    - the output markdown file name
    - default value: `reading.md`

The positional argument `[inputs ...]` has different scenarios:

1. both `[inputs ...]` and `[-d DIR]` arguments present: read specified `inputs` markdown files in `DIR` directory
2. `[-d DIR]` present but `[inputs ...]` missing: read in all markdown files in directory `DIR`
3. `[inputs ...]` present but `[-d DIR]` missing: read in all markdown files in default directory
4. `[inputs ...]` present but not existed: display error message to ask for correct inputs

Notable issues when processing markdown files:

1. markdown file extension might be missing w/ `inputs ...`, add extension automamtically
2. local figures in markdown files prepend `DIR` for the image files, except for default value


## Parsing Figures

The typical `<figure>` element used in markdown files are as below snippet (basic one and other varieties based on this one):

```html
<figure style="display: table; margin: auto; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('page')"
    src    = "image"
    alt    = "alt text"
    title  = "text"
  />
  <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
    Fig. 1: ...
  </figcaption>
</figure>
```

The parser simply takes the `alt` value and translate into the markdown figure syntax w/ the `src` value:

```md
![alt text](image "Fig. 1 ...")
```

The above syntax replaces the original `figure` element.

Two scenarios requires to handle `src` attribute value `image`:

- URL format: simply replace `image` value in the markdown syntax w/ the `src` value in the `figure` element
- local file path format: replace `image` value in the markdown syntax w/ the relative file path vaalue to point to the local image




## Project Helper Functions

There are a couple of helper functions except for the parsing ones:

- process executable with arguments: `html2md.py -o path/to/output.md -d path/to/mdfiles file1.md file2.md ...`
  - `-o`: flag for output file
  - `-d`: flag for directory path of input files
  - `path/to/output.md`: the output filename and its path
  - `html2md`: executable python filename
  - `path/to/mdfiles`: the path where the input markdown files located
  - `file1.md file2.md ...`: a list of markdown files to concatnate into a single markdown file
  - the output markdown file only contains the standard markdown syntax, default filename, `reading.md`
- process various html tags
  - `code` tag: replaced w/ '`' character
  - `span` tag: according its embedded style attributes and values to add appropriate markdown syntax
    - the implementation hold on and check later
    - `font-style: italic;` replaced w/ `*text*`
  - `a` tag: most likely ignore; if process required, replacing w/ `[text](link)`
- separate individual file content w/ several new lines, e.g., 6 blank line inserted


## Project Virtual Environment

- custom virtual environment location: `export WORKON_HOME=~/.venvs`
- python path: `~/.venvs/html2md-Z6Rs3Moi/bin/python` 


## Reference

- [Markdown Templates](https://github.com/jaantollander/Markdown-Templates), 2022
- [Publishing Notes using Markdown](https://cs.uwaterloo.ca/~j2avery/posts/2021-08-13-markdown-notes/), 2020
- [Academic writing in Markdown](http://scorreia.com/research/markdown-correia-2019.pdf), 2019
- [How to make a scientific looking PDF from markdown (with bibliography)](https://gist.github.com/wayneeseguin/6ebfcfa967b0f9be4a87f3cd0898cd0a), 2022
- [Awesome Scientific Writing](https://github.com/writing-resources/awesome-scientific-writing), 2023
- [Pandoc-Suite and BibTeX-Zotero-Citation-Picker for Academic Writing in Markdown](https://github.com/chrisgrieser/pandoc_alfred/), 2022
- [Pandoc-Suite for Academic Writing in Markdown](https://www.alfredforum.com/topic/15997-pandoc-suite-for-academic-writing-in-markdown/), 2020
- [Writing Scientific Papers Using Markdown](https://github.com/djhocking/Markdown-for-Manuscripts), 2022



## Change Logs

- 2023-02-05: initial the ideal




