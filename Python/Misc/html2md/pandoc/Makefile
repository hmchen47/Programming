# macros
BUILDID = $(warning Invoking the shell)$(shell date +Ymd)
CWD = $(shell pwd)
BUILDDIR = ./build
ASSETSDIR = ./assets
CONTENTDIR = ./content
LAYOUTSDIR = ./layouts

READINGINFILE = reading.md
READINGOUTFILE = reading.pdf

CONVERTDIR = ~/Projects/Programs/Notes/
CONVERTFILES = 	webgc05-YAMLSpec.md web07-ModelComp.md \
								web08-MVCDjango.md web09-CSSLAyout.md


reading: $(CONTENTDIR)/$(READINGINFILE) $(LAYOUTSDIR)/print.tex
	@echo
	@echo Starting to build $(READINGOUTFILE) files ...
	@echo Current directory: $(CWD)
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
	@echo End print pdf build!
	@echo


html2md: ./parser/html2md.py $(CONVERTDIR) $(CONVERTFILES)
	@echo
	@echo Convert Figures & Tables HTML code to MD syantx ...
	@




