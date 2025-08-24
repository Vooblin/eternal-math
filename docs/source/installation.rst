Installation
============

Requirements
------------

* Python 3.12 or higher
* pip (Python package installer)

From PyPI
---------

.. code-block:: bash

    pip install eternal-math

From Source
-----------

To install the latest development version:

.. code-block:: bash

    git clone https://github.com/Vooblin/eternal-math.git
    cd eternal-math
    pip install -e .

Development Installation
------------------------

For contributing to the project:

.. code-block:: bash

    git clone https://github.com/Vooblin/eternal-math.git
    cd eternal-math
    pip install -e .[dev]

This installs additional development dependencies including:

* pytest - For running tests
* black - Code formatter
* isort - Import sorter
* flake8 - Linter
* mypy - Type checker
* pytest-cov - Coverage reporting

Dependencies
------------

Eternal Math depends on:

* **numpy** (>=1.21.0) - Numerical computing
* **sympy** (>=1.9) - Symbolic mathematics
* **matplotlib** (>=3.5.0) - Plotting and visualization

These will be automatically installed when you install eternal-math.

Verification
------------

To verify your installation, try importing the package:

.. code-block:: python

    import eternal_math
    print(eternal_math.__version__)

Or run the CLI:

.. code-block:: bash

    eternal-math --help
