Contributing
============

We welcome contributions to Eternal Math! This guide will help you get started.

Development Setup
-----------------

1. Fork the repository on GitHub
2. Clone your fork locally:

.. code-block:: bash

    git clone https://github.com/YOUR-USERNAME/eternal-math.git
    cd eternal-math

3. Create a virtual environment:

.. code-block:: bash

    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

4. Install development dependencies:

.. code-block:: bash

    pip install -e .[dev]

Code Quality Standards
----------------------

Type Checking
~~~~~~~~~~~~~

This project uses comprehensive type hints. Run type checking with:

.. code-block:: bash

    mypy eternal_math/

Code Formatting
~~~~~~~~~~~~~~~

We use Black for code formatting and isort for import sorting:

.. code-block:: bash

    # Format code
    black eternal_math/ tests/ examples/
    
    # Sort imports
    isort eternal_math/ tests/ examples/

Linting
~~~~~~~

We use flake8 for linting:

.. code-block:: bash

    flake8 eternal_math/ tests/ examples/

Testing
-------

Run the full test suite:

.. code-block:: bash

    pytest tests/ -v

Run tests with coverage:

.. code-block:: bash

    pytest tests/ --cov=eternal_math --cov-report=html

Writing Tests
~~~~~~~~~~~~~

* Write tests for all new functionality
* Aim for high test coverage (>90%)
* Use descriptive test names
* Include edge cases and error conditions

Documentation
-------------

Update documentation when:

* Adding new modules or functions
* Changing existing APIs
* Adding new features

Build documentation locally:

.. code-block:: bash

    cd docs/
    make html

Pull Request Guidelines
-----------------------

1. Create a feature branch from ``main``
2. Make your changes
3. Add tests for new functionality
4. Ensure all tests pass
5. Update documentation if needed
6. Submit a pull request with a clear description

Code Review Process
-------------------

All submissions require review. We use GitHub pull requests for this purpose.
Reviewers will check for:

* Code quality and style
* Test coverage
* Documentation updates
* Performance implications

Issue Reporting
---------------

When reporting issues, please include:

* Python version
* Operating system
* Eternal Math version
* Minimal code example
* Expected vs actual behavior
* Full error traceback (if applicable)

Feature Requests
----------------

We welcome feature requests! Please:

* Check if the feature already exists
* Describe the use case clearly
* Provide example usage if possible
* Consider contributing the implementation

Community
---------

* GitHub Discussions: For questions and general discussion
* GitHub Issues: For bug reports and feature requests
* Pull Requests: For code contributions

Thank you for contributing to Eternal Math!
