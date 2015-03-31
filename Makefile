.PHONY: test
test: pep8 clean
	py.test tests.py

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: pep8
pep8:
	@flake8 main.py tests.py --ignore=F403,F401,E501

.PHONY: clean
clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} 	\;
