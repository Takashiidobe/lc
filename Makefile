PDOC_FLAGS=--math --mermaid
watch:
	firefox localhost:8080
	pdoc $(PDOC_FLAGS) *.py  -n

build:
	pdoc $(PDOC_FLAGS) -o docs *.py

deploy: build
	ntl deploy --prod
