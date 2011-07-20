.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

SLIDES= session1.pdf \
	session2.pdf \
	session3.pdf \
	session4.pdf \
	session5.pdf \

CHEATS= cheatsheet1.pdf \
	cheatsheet2.pdf \
	cheatsheet3.pdf \
	cheatsheet4.pdf \
	cheatsheet6.pdf

QUIZ= day1quiz1.pdf \
	day1quiz2.pdf \

all:	$(SLIDES) $(CHEATS) $(QUIZ)

cheats: $(CHEATS)

slides: $(SLIDES) $(CHEATS)

quiz: $(QUIZ)

clean-all:
	rm -f *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.pdf *.toc *.out *~ *.vrb *.nav *.snm

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm



