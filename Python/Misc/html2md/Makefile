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

PARSERDIR = parser

MDDIR = ~/Projects/Programming/Notes
MDFILES = web09-CSSLayout.md

default: html2md reading

reading: 
	@echo
	@echo "Starting to build $(READINGOUTMD) files ..."
	@echo "Current directory: $(CWD)"
	@echo

	rm -f $(WORKINGDIR)/$(READINGPDF)

	@echo
	pandoc $(CONTENTDIR)/$(READINGINMD) $(COLORLINK) \
		--resource-path $(CONTENTDIR):$(LAYOUTSDIR) \
		--csl $(ASSETSDIR)/citation-style.csl \
		--from markdown+tex_math_single_backslash+tex_math_dollars+raw_tex+smart \
		--to latex \
		--output $(WORKINGDIR)/$(READINGPDF) \
		--pdf-engine xelatex \
		--include-in-header $(LAYOUTSDIR)/reading.tex \
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

