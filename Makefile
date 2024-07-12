watch:
	firefox localhost:8080
	pdoc *.py --math -n

build:
	pdoc -o docs *.py --math

deploy: build
	ntl deploy --prod
