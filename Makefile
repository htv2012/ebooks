help:
	@echo make commit
	@echo make ebooks

commit:
	./commit.py

ebooks:
	./create_ebooks.sh
