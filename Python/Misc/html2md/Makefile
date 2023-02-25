# macros
BUILDID = $(warning Invoking the shell)$(shell date +Ymd)
CWD = $(shell pwd)

WORKINGDIR = working

PANDOCDIR = pandoc
BUILDDIR = ./$(PANDOCDIR)/build
ASSETSDIR = ./$(PANDOCDIR)/assets
CONTENTDIR = ./$(WORKINGDIR)
LAYOUTSDIR = ./$(PANDOCDIR)/layouts

COLORLINK = -V colorlinks=true \
						-V linkcolor=green \
						-V urlcolor=blue

READINGINMD = notes_reading.md
READINGOUTMD = notes_reading.md
READINGPDF = notes_reading.pdf
WEBPDF = web_reading.pdf

# WEBPAGE = https://pandoc.org/MANUAL.html

PARSERDIR = parser

MDDIR = ~/Projects/Programming/Notes
MDFILES = py20-Arguments.md py21-argparse.md

default: html2md reading

reading: 
	@echo
	@echo "Starting to build $(READINGOUTMD) files ..."
	@echo "Current directory: $(CWD)"
	@echo

	rm -f $(WORKINGDIR)/$(READINGPDF)

	@echo
	pandoc $(CONTENTDIR)/$(READINGINMD) $(COLORLINK) \
		--variable fontsize=12pt \
		--resource-path $(CONTENTDIR):$(LAYOUTSDIR) \
		--csl $(ASSETSDIR)/citation-style.csl \
		--from markdown+tex_math_single_backslash+tex_math_dollars+raw_tex+smart \
		--to latex \
		--output $(WORKINGDIR)/$(READINGPDF) \
		--pdf-engine xelatex \
		--verbose \
		--include-in-header $(LAYOUTSDIR)/reading.tex \

	@echo
	@ls -l --color $(WORKINGDIR)/
	@echo "End note pdf build! ..."
	@echo
	@echo


web: # readfile from a given URL and convert it to pdf
	@echo
	@echo Convert web page to PDF
	@echo
	pandoc $(WEBPAGE) $(COLORLINK) \
		--resource-path $(CONTENTDIR):$(LAYOUTSDIR) \
		--csl $(ASSETSDIR)/citation-style.csl \
		--from html \
		--to latex \
		--output $(WORKINGDIR)/$(WEBPDF) \
		--pdf-engine xelatex \
		--include-in-header $(LAYOUTSDIR)/web.tex \
		# --verbose

	@echo
	@ls -l --color $(WORKINGDIR)/
	@echo "End print pdf build! ..."
	@echo


# html2md: ./$(PARSERDIR)/html2md.py $(MDDIR)/$(MDFILES)
html2md: clean_target_md
	@echo
	@echo "Convert Figures & Tables HTML code to MD syantx ..."
	@echo

	./$(PARSERDIR)/html2md.py -d $(MDDIR) $(MDFILES)

	@echo
	@echo End of converting ...
	@echo


clean_target_md:
ifeq (, $(wildcard $(CONTENTDIR)/$(READINEFILE)))
	rm $(CONTENTDIR)/$(READINEFILE)
endif

