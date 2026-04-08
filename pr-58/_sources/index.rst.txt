..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

Module Template Documentation
=============================

This documentation describes the structure, usage and configuration of the Bazel-based C++/Rust module template according to the `SCORE module folder structure <https://eclipse-score.github.io/score/main/contribute/general/folder.html#module-folder-structure>`_.

.. contents:: Table of Contents
   :depth: 2
   :local:

Overview
--------

This repository provides a standardized setup for projects using **C++** or **Rust** and **Bazel** as a build system.
It integrates best practices for build, test, CI/CD and documentation.
It also provides Assumption of Use requirement snippets in :doc:`aou_requirements_template`.
It also provides an example of modeling architecture in Sphinx Needs in :doc:`architecture/architecture_modeling_example`.
It also provides the component architecture template snippets in :doc:`score/example_component/architecture/component_architecture_template`.
It also provides an example of documenting detailed design in :doc:`score/example_component/detailed_design/detailed_design_example`.
It also provides the stakeholder requirements template snippet in :doc:`stakeholder_requirements_template`.


Module Layout
-------------

The module template includes the following top-level structure:

- `score/`: Main C++/Rust sources with Unit Tests and component documentation and component integration tests, as well as architecture modeling and detailed design examples and component requirements, safety and security analysis documentation, and verification report documentation
- `tests/`: Module / Feature Integration Tests
- `examples/`: Usage examples for the module or feature
- `docs/`: Documentation using `docs-as-code` for the module and feature, including architecture modeling and detailed design examples, and release notes, safety and security management documentation, and verification report documentation
- `.github/workflows/`: CI/CD pipelines

.. toctree::
   :maxdepth: 1

   stakeholder_requirements_template
   aou_requirements_template


Module / Feature Documentation
------------------------------

.. toctree::
   :maxdepth: 1

   architecture/architecture_modeling_example
   manual/index
   release/release_note
   safety_mgt/index
   security_mgt/index
   verification_report/index

Example component documentation
-------------------------------

.. toctree::
   :maxdepth: 1

   score/example_component/index
   score/example_component/architecture/component_architecture_template
   score/example_component/detailed_design/detailed_design_example


Quick Start
-----------

To build the module:

.. code-block:: bash

   bazel build //src/...

To run all tests:

.. code-block:: bash

   bazel test //...

To run Unit Tests:

.. code-block:: bash

   bazel test //src/...

To run Component / Feature Integration Tests:

.. code-block:: bash

   bazel test //tests/...

Module Configuration
--------------------

The `project_config.bzl` file defines metadata used by Bazel macros.

Example:

.. code-block:: python

   PROJECT_CONFIG = {
       "asil_level": "QM",
       "source_code": ["cpp", "rust"]
   }

This enables conditional behavior (e.g., choosing `clang-tidy` for C++ or `clippy` for Rust).
