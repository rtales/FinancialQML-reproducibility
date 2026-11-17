PYTHON ?= python3

.PHONY: verify test reproduce clean

verify:
	$(PYTHON) src/reproduce.py --verify-only

test:
	$(PYTHON) -m pytest -q

reproduce: verify
	$(PYTHON) src/reproduce.py --out outputs/reproduced

clean:
	rm -rf outputs/reproduced
