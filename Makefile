VENV       = .venv
PYTHON     = $(VENV)/bin/python
PIP        = $(VENV)/bin/pip
SPHINXBUILD  = $(VENV)/bin/sphinx-build
SPHINXAUTO   = $(VENV)/bin/sphinx-autobuild

SOURCEDIR  = docs
BUILDDIR   = docs/_build
SPHINXOPTS ?=

# ── virtual environment ────────────────────────────────────────────────────

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

.PHONY: venv
venv: $(VENV)/bin/activate

# ── docs ───────────────────────────────────────────────────────────────────

.PHONY: html livehtml clean help clean-python clean-all

html: $(VENV)/bin/activate
	$(SPHINXBUILD) -M html $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)

livehtml: $(VENV)/bin/activate
	$(SPHINXAUTO) $(SOURCEDIR) $(BUILDDIR)/html $(SPHINXOPTS)

clean:
	rm -rf $(BUILDDIR)

clean-python:
	rm -rf $(VENV)

clean-all: clean clean-python

help: $(VENV)/bin/activate
	$(SPHINXBUILD) -M help $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)
