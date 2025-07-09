====================
How the Agent Works
====================

This page provides an overview of the AI-powered agentic workflow used to develop and maintain AlgoLib-ADG.

The Core Engine
---------------

The agent is built on a simple yet powerful premise: define a clear specification, and let automation handle the rest. The process is orchestrated by a core Python script that interprets YAML specification files and uses a suite of tools to generate, test, and document code.

The workflow is as follows:

1.  **Specification**: A new algorithm or data structure is defined in a ``.yml`` file in the ``specs/`` directory. This file contains metadata such as the name, category, complexity, and a natural language description.

2.  **Code Generation**: The agent reads the specification and uses a code generation tool to create the Python implementation file in ``algolib/``.

3.  **Test Generation**: Simultaneously, the agent generates a corresponding test file in ``tests/``, ensuring high test coverage from the start.

4.  **Documentation Generation**: A documentation stub is created in ``docs/source/``, which will be automatically populated with details from the implementation.

5.  **Pull Request**: The agent commits the new files and opens a pull request, ready for human review.

Tooling and Integration
-----------------------

The agent integrates with several key services and tools:

-   **FastAPI Backend**: A REST API provides endpoints for interacting with the library and its components. You can explore the available endpoints via the Swagger UI.

    -   `View the API Docs <http://localhost:8000/docs>`_

-   **Streamlit UI**: A simple web interface for generating new algorithm implementations by filling out a form, which then runs the agent pipeline.

    -   *Link to be added once the Streamlit UI is available.*

This agent-driven approach ensures that all contributions are consistent, well-tested, and adhere to the project's high standards for quality.
