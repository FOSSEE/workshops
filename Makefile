.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

all: day-one day-two

cheats: 
	cd day1; make cheats
	cd day2; make cheats

slides: 
	cd day1; make slides
	cd day2; make slides

quiz: 
	cd day1; make quiz
	cd day2; make quiz

day-one: 
	cd day1; make slides
	cd day1; make cheats
	cd day1; make quiz

day-two: 
	cd day2; make slides
	cd day2; make cheats
	cd day2; make quiz

clean-all:
	rm -f *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.pdf *.toc *.out *~ *.vrb *.nav *.snm
	cd day1; make clean-all
	cd day2; make clean-all

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm
	cd day1; make clean
	cd day2; make clean



