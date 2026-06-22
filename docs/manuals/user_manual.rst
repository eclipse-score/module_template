..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

.. _user_manual:

User Manual
###########


.. attention::
    Update the document metadata according to your needs, particularly linking to the corresponding
    work package with the ``realizes`` field once work packages are defined.

Overview
========

This user manual provides comprehensive guidance for using the [Your Module Name] module.
It covers installation, configuration, basic usage, and best practices for integrating this module
into your project.

.. note::
   This is a template user manual. Replace placeholder text with actual module-specific information.

Feature List
============

Key features of this module:

* Feature overview and navigation: :doc:`/docs/features/index`
* Feature template and scope example: :doc:`/docs/features/feature_example/index`
* Feature architecture and verification artifacts: :doc:`/docs/features/feature_example/architecture/index`
* Feature safety artifacts (FMEA, DFA, AoU): :doc:`/docs/features/feature_example/safety_analysis/fmea`, :doc:`/docs/features/feature_example/safety_analysis/dfa`, and :doc:`/docs/features/feature_example/safety_analysis/aou_requirements_template`
* Feature security artifacts: :doc:`/docs/features/feature_example/security_analysis/index`
* Feature planning artifacts (safety/security): :doc:`/docs/features/feature_example/safety_planning/index` and :doc:`/docs/features/feature_example/security_planning/index`

Platform Requirements
=====================

Supported Platforms
-------------------

* **C++**: C++17 or later
* **Rust**: 1.70 or later (if Rust support is included)
* **Build System**: Bazel 6.0 or later
* **Operating Systems**: Linux, macOS, Windows (as applicable)

Dependencies
------------

[List key external dependencies, licenses, and version requirements]

**Example:**
* Standard library (STL/Core)
* [Other required libraries]

Quick Start - Building and Testing
===================================

Building the Module
--------------------

To build the entire module:

.. code-block:: bash

   bazel build //src/...

Running Tests
--------------

To run all tests:

.. code-block:: bash

   bazel test //...

To run only unit tests:

.. code-block:: bash

   bazel test //src/...

To run component or feature integration tests:

.. code-block:: bash

   bazel test //tests/...

Module Configuration Details
=============================

The ``project_config.bzl`` file at the root of the module defines metadata used by Bazel macros.
This file controls build behavior and project-specific settings.

Configuration Example
---------------------

.. code-block:: python

   PROJECT_CONFIG = {
       "asil_level": "QM",
       "source_code": ["cpp", "rust"]
   }

Configuration Effects
---------------------

The configuration enables conditional build behavior:

* **Language-specific tools**: For C++ code, tools like ``clang-tidy`` are used; for Rust code, ``clippy`` is used
* **Safety level**: The ASIL level affects safety-related build settings and validation
* **Source code languages**: The build system optimizes for the configured languages

Getting Started with Features and Components
============================================

Feature Documentation
---------------------

For documentation on features implemented in the module:

.. toctree::
   :maxdepth: 1

   /docs/features/index

Component Documentation
-----------------------

For documentation of individual components within this module:

.. toctree::
   :maxdepth: 1

   /score/component_example/docs/index

Examples
--------

Useful examples and tutorials:

.. toctree::
   :maxdepth: 1

   /examples/docs/architecture_modeling_example

Integration Guidelines
======================

Integrating with Your Project
------------------------------

1. Add the module to your Bazel workspace:

   .. code-block:: python

      # In your MODULE.bazel
      bazel_dep(name = "module_template", version = "1.0")

2. Reference in your build files:

   .. code-block:: python

      cc_library(
          name = "my_target",
          deps = ["@module_template//score/component_example:component"],
      )

3. Include headers and compile your code

Best Practices
--------------

* Always validate input parameters
* Handle error codes and exceptions appropriately
* Use the module in accordance with safety and security guidelines
* Review the safety manual (wp__module_safety_manual) for safety-critical applications
* Review the security manual (wp__module_security_manual) for security considerations

API Reference
=============

For complete API documentation and descriptions, refer to the API documentation in the ``api_description/`` directory.

Performance Considerations
==========================

This section covers performance characteristics, optimization strategies, and resource requirements.
Refer to the ``performance/`` directory for detailed performance guides and benchmarks.

Troubleshooting
===============

Common Issues and Solutions
----------------------------

**Issue: Build fails with undefined reference**

   Check that all dependencies are properly declared in your BUILD file and that the module is correctly linked.

**Issue: Runtime errors or crashes**

   Verify that:
   * You are using the module API correctly (refer to API Reference)
   * All required initialization steps have been completed
   * Input data meets the documented requirements

**Issue: Performance problems**

   Consult the Performance Considerations section or review the ``performance/`` documentation.

Getting Help
============

For additional support and resources:

* Review the API Reference documentation
* Check the configuration examples in the ``config/`` folder
* Refer to example implementations in ``examples/``
* Consult the Safety Manual for safety-critical usage
* Consult the Security Manual for security-related concerns
* Contact the module maintainers or community forums

Safety and Security
===================

**Safety-Critical Usage**: If you are using this module in a safety-critical context,
please refer to :doc:`safety_manual` for detailed safety requirements and guidelines.

**Security Considerations**: For information about security aspects and requirements,
please refer to :doc:`security_manual`.

Known Limitations
=================

* [Limitation 1]
* [Limitation 2]
* [Known issues and workarounds]

Version History and Compatibility
==================================

[Document version changes, API stability, deprecation notices, and migration guides]

**Current Version**: 1.0 (Draft)

Compatibility Notes
-------------------

* Backward compatibility with previous versions: [Yes/No/Partial]
* Migration guide for [previous version] users: [Link or reference]

License
=======

This module is licensed under the Apache License Version 2.0.
See the LICENSE file in the repository for full license text.

Feedback and Contributions
==========================

Your feedback and contributions are welcome! Please report issues or suggestions through the
project's issue tracker or contribute directly to the repository.
