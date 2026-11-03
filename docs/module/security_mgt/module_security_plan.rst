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

[Module Name] Security Plan
===========================

.. note:: Document header

.. document:: [Module Name] Security Plan
  :id: doc__mod_temp_module_name_security_plan
  :status: draft
  :version: 1
  :safety: ASIL_B
  :security: YES
  :realizes: wp__module_security_plan
  :tags: template

.. attention::
    The above directive must be updated according to your Module.

    - Modify ``Your Module Name`` to be your Module Name
    - Modify ``id`` to be your Module Name in lower snake case preceded by ``doc__`` and followed by ``_security_plan``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

Security Management Context
============================

This Security Plan adds to the process security management guidance all the module development relevant work products needed for ISO SAE 21434 conformity.

Security Management Scope
==========================

This Security Plan's scope is a SW module of the SW platform <link to module documentation in platform/modules/<modulename>/index.rst>.
The module consists of one or more SW components and will be qualified as a OoC.

Security Management Roles
==========================

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Security Manager
          - <link to Module's Security Manager assignment or name>

        * - Project Manager
          - <link to Module's Project Lead assignment or name>

Tailoring
=========

Additional to the tailoring in the SW platform project as defined in the process security management guidance we define here the additional tailoring on module level.

- Excluded for this module are additionally the following work products (and their related requirements):

  - <ISO SAE 21434 reference>: <work product/requirement> - <Argumentation why it is not needed or replaced by another work product or activity.>

Component Out-of-Context Assumptions
======================================

As this module is developed and qualified as a Component Out-of-Context (OoC), the following assumptions on its intended use, context and external interfaces are made. These assumptions are the basis for the module's cybersecurity requirements and shall be validated upon integration into an item or a higher-level component:

- <assumption on intended use / operational environment>
- <assumption on external interfaces>

Off-the-Shelf / OSS Component Qualification
=============================================

If off-the-shelf or Open Source Software (OSS) components are integrated into this module, their cybersecurity-relevant documentation is gathered and analysed to determine whether the allocated cybersecurity requirements can be fulfilled and whether the existing documentation is sufficient to support the cybersecurity activities. The following OTS/OSS components are planned to be qualified this way:

- <component name> - <maintenance status / known vulnerability history / available documentation> - <Link to qualification record or issue>

If the existing documentation is insufficient for a component, the cybersecurity activities necessary to close the gap are identified here: <Link to issue/activity>.

Cybersecurity Assessment Decision
====================================

The decision whether a Cybersecurity Assessment is performed for this module, and the rationale for that decision, is documented here:

- Decision: <YES | NO>
- Rationale: <rationale for the decision, e.g. based on the module's TARA results and/or organizational criteria>
- If YES: responsible assessor, independent from the development team: <link to assignment>

Vulnerability Monitoring and Management
==========================================

For this module, the following is defined for the continual cybersecurity activities after release:

- Sources monitored for new cybersecurity information (e.g. advisories for used OTS/OSS components): <list sources>
- SBOM generation: <tool/process used to generate and maintain the module's SBOM>
- Vulnerability scan cadence: <e.g. on every release, on a fixed schedule, ...>
- Triage and remediation responsible: <link to role/assignment>
- Escalation to the cybersecurity incident response process: <link to process/contact>

Security Module Work Products
==============================

One set of work products for the module and one set for each component of the module:

.. list-table:: Module Work Products
        :header-rows: 1

        * - Work Product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__module_security_plan`
          - Security management guideline
          - <automated>
          - <Link to issue>
          - this document
          - see above

        * - :need:`wp__module_security_package`
          - Security management guideline
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__fdr_reports_security` (Module Security Plan)
          - :need:`gd_chklst__security_plan`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__fdr_reports_security` (Module Security Package)
          - :need:`Security Package Formal Review Checklist <gd_chklst__security_package>`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__fdr_reports_security` (Module's Security Analyses)
          - Security Analysis FDR tbd
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__audit_report_security`
          - performed by external experts
          - n/a
          - <Link to issue>
          - <Link to WP>
          - <WP status (manual)>

        * - :need:`wp__module_security_manual`
          - :need:`gd_temp__module_security_manual`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification_module_ver_report`
          - Verification process guidance
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__module_sw_release_note`
          - Release management guidance
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__module_user_manual`
          - :need:`gd_temp__rel_mod_user_manual`
          - <automated>
          - <Link to issue>
          - :need:`doc__mod_temp_module_name_user_manual`
          - <automated>

        * - :need:`wp__sw_module_sbom`
          - Security management guidance
          - not started
          - <Link to issue>
          - <Link to WP>
          - <automated>


.. list-table:: Component <name> Work Products
        :header-rows: 1

        * - Work Product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__requirements_comp`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__requirements_comp_aou`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__requirements_inspect`
          - <Link to process>
          - <automated>
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - :need:`wp__component_arch`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_security_analysis`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_arch_verification`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_implementation`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification_sw_unit_test`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_implementation_inspection`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification_comp_int_test`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>
