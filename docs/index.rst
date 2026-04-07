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

.. toctree::
   :maxdepth: 1

   aou_requirements_template
   architecture/architecture_modeling_example
   score/example_component/component_architecture_template
   score/example_component/detailed_design_example
   stakeholder_requirements_template

.. contents:: Table of Contents
   :depth: 2
   :local:

Overview
--------

This repository provides a standardized setup for projects using **C++** or **Rust** and **Bazel** as a build system.
It integrates best practices for build, test, CI/CD and documentation.
It also provides Assumption of Use requirement snippets in :doc:`aou_requirements_template`.
It also provides an example of modeling architecture in Sphinx Needs in :doc:`architecture/architecture_modeling_example`.
It also provides the component architecture template snippets in :doc:`score/example_component/component_architecture_template`.
It also provides an example of documenting detailed design in :doc:`score/example_component/detailed_design_example`.
It also provides the stakeholder requirements template snippet in :doc:`stakeholder_requirements_template`.

Requirements
------------

.. stkh_req:: Example Functional Requirement
   :id: stkh_req__docgen_enabled__example
   :status: valid
   :safety: QM
   :security: YES
   :reqtype: Functional
   :rationale: Ensure documentation builds are possible for all modules


Project Layout
--------------

The module template includes the following top-level structure:

- `src/`: Main C++/Rust sources with Unit Tests
- `tests/`: Component and Feature Integration Tests
- `examples/`: Usage examples
- `docs/`: Documentation using `docs-as-code`
- `.github/workflows/`: CI/CD pipelines

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

Configuration
-------------

The `project_config.bzl` file defines metadata used by Bazel macros.

Example:

.. code-block:: python

   PROJECT_CONFIG = {
       "asil_level": "QM",
       "source_code": ["cpp", "rust"]
   }

This enables conditional behavior (e.g., choosing `clang-tidy` for C++ or `clippy` for Rust).
