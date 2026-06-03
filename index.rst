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

Module Template Documentation
=============================

This documentation describes the structure, usage and configuration of the Bazel-based C++/Rust module template according to the `SCORE module folder structure <https://eclipse-score.github.io/score/main/contribute/general/folder.html#module-folder-structure>`_ and the `SCORE building blocks concept <https://eclipse-score.github.io/process_description/main/general_concepts/score_building_blocks_concept.html>`_.

.. contents:: Table of Contents
   :depth: 2
   :local:

Overview
--------

This repository provides a standardized setup for projects using **C++** or **Rust** and **Bazel** as a build system.
It integrates best practices for build, test, CI/CD and documentation.
It also provides an example of modeling architecture in Sphinx Needs in :doc:`/examples/docs/architecture_modeling_example`.
It also provides the component architecture template snippets in :doc:`/score/component_example/docs/architecture/component_architecture_template`.
It also provides an example of documenting detailed design in :doc:`/score/component_example/docs/detailed_design/detailed_design_example`.

Module Layout
-------------

The module template includes the following top-level structure:

.. parsed-literal::

   <module_name>/                       -> Folder containing all artifacts corresponding to one module.
   │                                       As folder optional if the repository only contains a single module.
   ├── docs/                            -> Documentation of the module
   │   ├── features/                    -> All features of the module.
   │   │   └── <feature_name>/          -> Features including sub-folders and feature/component (change) request
   │   │       │                           [:need:`wp__feat_request`], [:need:`wp__cmpt_request`]
   │   │       ├── architecture/        -> Feature architecture
   │   │       │                           [:need:`wp__feature_arch`], [:need:`wp__sw_arch_verification`]
   │   │       ├── safety_analysis/     -> Safety analysis on feature level
   │   │       │                           [:need:`wp__feature_fmea`], [:need:`wp__feature_dfa`]
   │   │       ├── safety_planning/     -> Feature specific safety workproducts planning
   │   │       │                           [:need:`wp__platform_safety_plan`]
   │   │       ├── security_analysis/   -> Security analysis on feature level
   │   │       │                           [:need:`wp__feature_security_analysis`]
   │   │       └── security_planning/   -> Feature specific security workproducts planning
   │   │                                   [:need:`wp__platform_security_plan`]
   │   ├── manuals/                     -> Module manual, e.g. integration manual, assumptions of use,
   │   │                                   safety manual [:need:`wp__requirements_comp_aou`],
   │   │                                   [:need:`wp__requirements_feat_aou`],
   │   │                                   [:need:`wp__module_safety_manual`],
   │   │                                   security_manual [:need:`wp__module_security_manual`].
   │   ├── release/                     -> Module release note [:need:`wp__module_sw_release_note`],
   │   │                                   module release plan [:need:`wp__module_sw_release_plan`],
   │   ├── safety_mgt/                  -> Module safety plan [:need:`wp__module_safety_plan`],
   │   │                                   module safety package [:need:`wp__module_safety_package`],
   │   │                                   formal documents reviews [:need:`wp__fdr_reports`],
   │   │                                   safety analysis formal reviews [:need:`wp__fdr_reports`],
   │   │                                   safety tailoring [:need:`wp__safety_tailoring`]
   │   │                                   safety component classification [:need:`wp__sw_component_class`]
   │   ├── security_mgt/                -> Module security plan [:need:`wp__module_security_plan`],
   │   │                                   module security package [:need:`wp__module_security_package`],
   │   │                                   formal documents reviews [:need:`wp__fdr_reports_security`],
   │   │                                   module SW bill of material [:need:`wp__sw_module_sbom`]
   │   └── verification_report/         -> Module verification report
   │                                       module verifications [:need:`wp__verification_module_ver_report`],
   └── score/                           -> Folder containing all artifacts corresponding to the components of the module.
       ├── <component_name>/            -> Components of the module.
       │   │                               Folder containing all artifacts corresponding to one component.
       │   ├── docs/                    -> Documentation of the component
       │   │   ├── architecture/        -> Component architecture (only if lower level components exist)
       │   │   │                           [:need:`wp__component_arch`].
       │   │   ├── detailed_design/     -> Detailed Design [:need:`wp__sw_implementation`] and
       │   │   │                           Detail design + code inspection [:need:`wp__sw_implementation_inspection`],
       │   │   ├── manuals/             -> User documentation of a single component
       │   │   │                           (e.g., user manual of a library, optional)
       │   │   ├── requirements/        -> Component requirements [:need:`wp__requirements_comp`],
       │   │   │                           requirements inspection [:need:`wp__requirements_inspect`]
       │   │   ├── safety_analysis/     -> Safety analysis on component level (only if component architecture exists)
       │   │   │                           [:need:`wp__sw_component_fmea`], [:need:`wp__sw_component_dfa`]
       │   │   └── security_analysis/   -> Security analysis on component level (only if component architecture exists)
       │   └── src/                     -> Source files of the component consisting of
       │       │                           Include and source Files [:need:`wp__sw_implementation`]
       │       │                           Test doubles
       │       │                           Unit tests [:need:`wp__verification_sw_unit_test`]
       │       ├── <lower_level_comp>/  -> lower level component following <component_name> folder structure
       │       └── tests/               -> Component-level tests (e.g., unit tests)
       │                                   [:need:`wp__verification_sw_unit_test`]
       └── tests/                       -> Module-level tests (e.g., feature integration tests, system tests)
                                           [:need:`wp__verification_comp_int_test`]
                                           Feature Integration tests [:need:`wp__verification_feat_int_test`]

.. note::

    The feature-specific subfolder under ``docs/features/<feature_name>/`` is only necessary
    if more than one feature is implemented in the module.

Module Folder Structure (Single-Feature Variant)
------------------------------------------------

The following variant keeps the same structure but removes the additional
feature-name nesting under ``docs/features/``. In this case, the ``features/``
subfolder is optional and omitted. This variant is intended for modules that only implement a single feature, to avoid unnecessary nesting.
For identification of the single feature, the repository name or module name should be replicate the feature name.

.. parsed-literal::

    <module_name>/                       -> Folder containing all artifacts corresponding to one module.
    │                                       As folder optional if the repository only contains a single module.
    ├── docs/                            -> Documentation of the module
    │   ├── architecture/                -> Feature architecture
    │   │                                   [:need:`wp__feature_arch`], [:need:`wp__sw_arch_verification`]
    │   ├── safety_analysis/             -> Safety analysis on feature level
    │   │                                   [:need:`wp__feature_fmea`], [:need:`wp__feature_dfa`]
    │   ├── safety_planning/             -> Feature specific safety workproducts planning
    │   │                                   [:need:`wp__platform_safety_plan`]
    │   ├── security_analysis/           -> Security analysis on feature level
    │   │                                   [:need:`wp__feature_security_analysis`]
    │   ├── security_planning/           -> Feature specific security workproducts planning
    │   │                                   [:need:`wp__platform_security_plan`]
    │   ├── manuals/                     -> Module manual, e.g. integration manual, assumptions of use,
    │   │                                   safety manual [:need:`wp__requirements_comp_aou`],
    │   │                                   [:need:`wp__requirements_feat_aou`],
    │   │                                   [:need:`wp__module_safety_manual`],
    │   │                                   security_manual [:need:`wp__module_security_manual`].
    │   ├── release/                     -> Module release note [:need:`wp__module_sw_release_note`],
    │   │                                   module release plan [:need:`wp__module_sw_release_plan`],
    │   ├── safety_mgt/                  -> Module safety plan [:need:`wp__module_safety_plan`],
    │   │                                   module safety package [:need:`wp__module_safety_package`],
    │   │                                   formal documents reviews [:need:`wp__fdr_reports`],
    │   │                                   safety analysis formal reviews [:need:`wp__fdr_reports`],
    │   │                                   safety tailoring [:need:`wp__safety_tailoring`]
    │   │                                   safety component classification [:need:`wp__sw_component_class`]
    │   ├── security_mgt/                -> Module security plan [:need:`wp__module_security_plan`],
    │   │                                   module security package [:need:`wp__module_security_package`],
    │   │                                   formal documents reviews [:need:`wp__fdr_reports_security`],
    │   │                                   module SW bill of material [:need:`wp__sw_module_sbom`]
    │   └── verification_report/         -> Module verification report
    │                                       module verifications [:need:`wp__verification_module_ver_report`],
    └── score/                           -> Folder containing all artifacts corresponding to the components of the module.
        ├── <component_name>/            -> Components of the module.
        │   │                               Folder containing all artifacts corresponding to one component.
        │   ├── docs/                    -> Documentation of the component
        │   │   ├── architecture/        -> Component architecture (only if lower level components exist)
        │   │   │                           [:need:`wp__component_arch`].
        │   │   ├── detailed_design/     -> Detailed Design [:need:`wp__sw_implementation`] and
        │   │   │                           Detail design + code inspection [:need:`wp__sw_implementation_inspection`],
        │   │   ├── manuals/             -> User documentation of a single component
        │   │   │                           (e.g., user manual of a library, optional)
        │   │   ├── requirements/        -> Component requirements [:need:`wp__requirements_comp`],
        │   │   │                           requirements inspection [:need:`wp__requirements_inspect`]
        │   │   ├── safety_analysis/     -> Safety analysis on component level (only if component architecture exists)
        │   │   │                           [:need:`wp__sw_component_fmea`], [:need:`wp__sw_component_dfa`]
        │   │   └── security_analysis/   -> Security analysis on component level (only if component architecture exists)
        │   └── src/                     -> Source files of the component consisting of
        │       │                           Include and source Files [:need:`wp__sw_implementation`]
        │       │                           Test doubles
        │       │                           Unit tests [:need:`wp__verification_sw_unit_test`]
        │       ├── <lower_level_comp>/  -> lower level component following <component_name> folder structure
        │       └── tests/               -> Component-level tests (e.g., unit tests)
        │                                   [:need:`wp__verification_sw_unit_test`]
        └── tests/                       -> Module-level tests (e.g., feature integration tests, system tests)
                                            [:need:`wp__verification_comp_int_test`]
                                            Feature Integration tests [:need:`wp__verification_feat_int_test`]

Module / Feature Documentation
------------------------------

.. toctree::
   :maxdepth: 1

   docs/features/index
   docs/manuals/index
   docs/release/release_note
   docs/safety_mgt/index
   docs/security_mgt/index
   docs/verification_report/module_verification_report

Component documentation
-------------------------------

.. toctree::
   :maxdepth: 1

   score/component_example/docs/index
   score/component_example/docs/architecture/index
   score/component_example/docs/detailed_design/index
   score/component_example/docs/requirements/index
   score/component_example/docs/safety_analysis/dfa
   score/component_example/docs/safety_analysis/fmea
   score/component_example/docs/safety_analysis/aou_requirements_template
   score/component_example/docs/component_classification

Examples
--------

.. toctree::
   :maxdepth: 1

   /examples/docs/architecture_modeling_example



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
