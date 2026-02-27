Installation
============

Requirements
------------

- Python 3.9 or later
- Sphinx 5.0 or later
- `icalendar <https://icalendar.readthedocs.io/>`_ 5.0 or later

From PyPI
---------

.. code-block:: bash

    pip install sphinx-icalendar

From source
-----------

Clone the repository and install in editable mode:

.. code-block:: bash

    git clone https://github.com/nicco/sphinx-icalendar-extension.git
    cd sphinx-icalendar-extension
    pip install -e .

Enabling the extension
----------------------

Add ``sphinx_icalendar`` to the ``extensions`` list in your project's
``conf.py``:

.. code-block:: python

    extensions = [
        "sphinx_icalendar",
    ]

No further configuration is required.
