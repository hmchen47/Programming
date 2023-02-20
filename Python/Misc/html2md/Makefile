# macros
BUILDID = $(warning Invoking the shell)$(shell date +Ymd)
CWD = $(shell pwd)

WORKINGDIR = working

PANDOCDIR = pandoc
BUILDDIR = ./$(PANDOCDIR)/build
ASSETSDIR = ./$(PANDOCDIR)/assets
CONTENTDIR = ./$(WORKINGDIR)
LAYOUTSDIR = ./$(PANDOCDIR)/layouts

READINGINMD = notes_reading.md
READINGOUTMD = notes_reading.md
READINGPDF = notes_reading.pdf

PARSERDIR = parser

MDDIR = ~/Projects/Programs/Notes
MDFILES = gc05-YAMLSpec.md web07-ModelComp.md \
					web08-MVCDjango.md web09-CSSLAyout.md

default: html2md reading

reading: 
	@echo
	@echo "Starting to build $(READINGOUTMD) files ..."
	@echo "Current directory: $(CWD)"
	@echo

	rm -f $(WORKINGDIR)/$(READINGPDF)

	@echo
	pandoc $(CONTENTDIR)/$(READINGINMD) \
		--resource-path $(CONTENTDIR):$(LAYOUTSDIR) \
		--csl $(ASSETSDIR)/citation-style.csl \
		--from markdown+tex_math_single_backslash+tex_math_dollars+raw_tex+smart \
		--to latex \
		--output $(WORKINGDIR)/$(READINGPDF) \
		--pdf-engine xelatex \
		--include-in-header $(LAYOUTSDIR)/reading.tex
	@echo
	@ls -l --color $(WORKINGDIR)/
	@echo "End print pdf build! ..."
	@echo


# html2md: ./$(PARSERDIR)/html2md.py $(MDDIR)/$(MDFILES)
html2md: clean_target_md
	@echo
	@echo "Convert Figures & Tables HTML code to MD syantx ..."
	@echo

	./$(PARSERDIR)/html2md.py -o $(CONTENTDIR)/$(READINGINFILE) -d $(MDDIR) $(MDFILES)

	@echo
	@echo End of converting ...
	@echo


clean_target_md:
ifeq (, $(wildcard $(CONTENTDIR)/$(READINEFILE)))
	rm $(CONTENTDIR)/$(READINEFILE)
endif

