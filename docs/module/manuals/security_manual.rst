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

[Module Name] Security Manual
=============================

.. note:: Document header

.. document:: [Module Name] Security Manual
   :id: doc__mod_temp_module_name_security_manual
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__module_security_manual
   :tags: template

.. attention::
    The above directive must be updated according to your Module.

    - Modify ``Your Module Name`` to be your Module Name
    - Modify ``id`` to be your Module Name in lower snake case preceded by ``doc__`` and followed by ``_security_manual``
    - Adjust ``status`` to be ``valid``
    - Adjust ``security`` and ``tags`` according to your needs

Introduction/Scope
------------------
| <Describe here which module (or the platform) is covered by this manual.>

Assumed Platform Security Requirements
--------------------------------------
| For the <Project platform / module name> the following security related stakeholder requirements are assumed to define the top level functionality (purpose) of the <Project platform / module name>. I.e. from these all the feature and component requirements implemented are derived.
| <List here all the stakeholder requirements, with security relevance, the module's components requirements are derived from.>

Assumptions of Use
------------------

Assumptions on the Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| The platform and its components are developed as Out of Context (OoC) with assumptions on the environment.
  It is assumed that the platform/components are integrated in a secure system, i.e. qualified POSIX OS.
  Also the HW related failures are taken into account by the system integrator, if not otherwise stated in the module's security concept.
| <List here all the OS calls the Project platform expects to be secure.>

List of AoUs expected from the environment the platform / module runs on:

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" in need["tags"] and need["security"] == "YES":
                results.append(need)

.. attention::
    Make sure these AoU are here for a security reason, i.e. every one "mitigates" a security analysis entry.

Assumptions on the User
^^^^^^^^^^^^^^^^^^^^^^^
| As there is no assumption on which specific OS and HW is used, the integration testing of the stakeholder and feature requirements is expected to be performed by the user of the platform OoC. Tests covering all stakeholder and feature requirements performed on a reference platform (tbd link to reference platform specification), reviewed and passed are included in the platform OoC security package.
| Additionally the components of the platform may have additional specific assumptions how they are used. These are part of every module documentation: <link to add>. Assumptions from components to their users can be fulfilled in two ways:
| 1. There are assumption which need to be fulfilled by all SW components, e.g. "every user of an IPC mechanism needs to make sure that he provides correct data (e.g. including appropriate security (access) control)" - in this case the AoU is marked as "platform".
| 2. There are assumption which can be fulfilled by a security control realized by some other Project platform component and are therefore not relevant for an user who uses the whole platform. But those are relevant if you chose to use the module OoC stand-alone - in this case the AoU is marked as "module". An example would be an "external API input" AoU which requires "The user shall provide input that has been validated/sanitized against injection and has not been tampered with in transit" - which is covered when using together with the <Project> platform's input validation / secure transport feature.

List of AoUs on the user of the platform features or the module of this Security Manual:

Note: Platform security manual collects all platform wide AoU (have to be fulfilled by the user for any feature).
Module security manual collects all AoUs specific to a feature and its realizing components.
This means for every feature the user selects, the platform security manual and the related module manual has to be considered.

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" not in need["tags"] and need["security"] == "YES":
                results.append(need)

.. attention::
    Make sure these AoU are here for a security reason, i.e. every one "mitigates" a security analysis entry.

Security concept of the OoC
----------------------------
| <Describe here the security concept incl. which attack paths are taken care of, reactions of the implemented functions under threatened operating conditions ... if this is not already documented sufficiently in the feature documentation "security impact" section of all the features the module is used in.>

Cybersecurity Claims and Residual Risk
----------------------------------------
| For cybersecurity risks that were treated by "accept" or "share" in the module's TARA risk treatment decision (rather than mitigated by a cybersecurity requirement), the resulting cybersecurity claim and the residual risk are documented here. These claims are assumptions the integrator has to fulfil, or risks the integrator knowingly accepts, when using this module.
| <List here the cybersecurity claims and the residual risk per accepted/shared threat scenario, with a link to the corresponding TARA entry.>

Secure Configuration and Hardening
-------------------------------------
| <Describe here the assumptions on cryptographic algorithms/key and secrets management, and on OS-level access control (e.g. secure boot, HSM/TEE usage, user/process privilege separation) the module relies on. These are in addition to the general Assumptions of Use above.>

Security Weaknesses, Vulnerabilities
------------------------------------
| Weaknesses, vulnerabilities (bugs in security relevant SW, detected by testing or by users, which could not be fixed) known before release are documented in the platform/module release notes <add link to release note>.
| Vulnerabilities discovered after release shall be reported via <link to SECURITY.md / PSIRT contact for this module>.

Security Support
-------------------
| <Describe here until when security support (i.e. vulnerability monitoring and fixes) is provided for this module/version, and what happens at end of security support.>

References
----------
| :need:`doc__mod_temp_module_name_user_manual`
| <other links>
