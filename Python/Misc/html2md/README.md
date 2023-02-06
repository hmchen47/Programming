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


## Project Auxiliary




## Change Logs

- 2023-02-05: initial the ideal




