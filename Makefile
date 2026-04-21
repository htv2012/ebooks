help:
	@echo make all
	@echo make commit
	@echo make ebooks

all: commit ebooks

commit:
	./commit.py

ebooks:
	./create_ebooks.sh
