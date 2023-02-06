# macros
BUILDID = $(warning Invoking the shell)$(shell date +Ymd)
CWD = $(shell pwd)
PANDOCDIR = pandoc
BUILDDIR = ./$(PANDOCDIR)/build
ASSETSDIR = ./$(PANDOCDIR)/assets
CONTENTDIR = ./$(PANDOCDIR)/content
LAYOUTSDIR = ./$(PANDOCDIR)/layouts

READINGINFILE = reading.md
READINGOUTFILE = reading.pdf

PARSERDIR = parser

MDDIR = ~/Projects/Programs/Notes
MDFILES = webgc05-YAMLSpec.md web07-ModelComp.md \
					web08-MVCDjango.md web09-CSSLAyout.md

default: html2md reading

reading: $(CONTENTDIR)/$(READINGINFILE) $(LAYOUTSDIR)/print.tex
	@echo
	@echo "Starting to build $(READINGOUTFILE) files ..."
	@echo "Current directory: $(CWD)"
	@echo

	rm -f $(BUILDDIR)/$(READINGOUTFILE)

	@echo
	pandoc $(CONTENTDIR)/$(READINGINFILE) \
		--resource-path $(CONTENTDIR):$(LAYOUTSDIR) \
		--csl $(ASSETSDIR)/citation-style.csl \
		--from markdown+tex_math_single_backslash+tex_math_dollars+raw_tex+smart \
		--to latex \
		--output $(BUILDDIR)/$(READINGOUTFILE) \
		--pdf-engine xelatex \
		--include-in-header $(LAYOUTSDIR)/reading.tex
	@echo
	@ls -l --color $(BUILDDIR)/
	@echo "End print pdf build! ..."
	@echo


# html2md: ./$(PARSERDIR)/html2md.py $(MDDIR)/$(MDFILES)
html2md: clean_target_md
	@echo
	@echo "Convert Figures & Tables HTML code to MD syantx ..."
	@echo

	$(PARSERDIR)/html2md.py -o $(CONTENTDIR)/$(READINGINFILE) -d $(MDDIR) $(MDFILES)

	@echo
	@echo End of converting ...
	@echo


clean_target_md:
ifeq (, $(wildcard $(CONTENTDIR)/$(READINEFILE)))
	rm $(CONTENTDIR)/$(READINEFILE)
endif

