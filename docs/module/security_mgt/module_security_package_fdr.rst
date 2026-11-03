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

[Module Name] Security Package Formal Review Report
===================================================

.. note:: Document header

.. document:: [Module Name] Security Package Formal Review
  :id: doc__mod_temp_module_name_sec_pkg_fdr
  :status: draft
  :version: 1
  :safety: ASIL_B
  :security: YES
  :realizes: wp__fdr_reports_security
  :tags: template

.. attention::
    The above directive must be updated according to your Module.

    - Modify ``Your Module Name`` to be your Module Name
    - Modify ``id`` to be your Module Name in lower snake case preceded by ``doc__`` and followed by ``_sec_pkg_fdr``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs


**1. Purpose**

The purpose of this review checklist is to report status of the formal review for the Security Package.

**2. Conduct**

As described in :need:`wf__p_formal_security_rv`, the formal document review is performed by an "external" security auditor, supported by the Security Manager:

- reviewer: <committer with security manager/auditor skills explicitly named here>

.. note::
    :need:`wf__p_formal_security_rv` is currently marked as "tailored out (needs discussion)" at process level.
    Confirm with the Security Manager whether a formal review is actually performed for this Module before relying on this checklist.

**3. Checklist**

See also the review concept for further information about reviews in general and inspection in particular.

.. list-table:: Security Package Checklist
        :header-rows: 1

        * - Id
          - Security Package activity
          - Compliant to ISO SAE 21434?
          - Reference
          - Comment

        * - 1
          - Is a Security Package provided which matches the Security Plan (i.e. all planned work products referenced)?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6471>`
          - <Rationale for result>

        * - 2
          - Is the argument how security is achieved (i.e. the Cybersecurity Case), provided in the Security Package, plausible and sufficient?
          - NO
          - :need:`[[title]] <std_req__isosae21434__prj_management_6471>`
          - The Cybersecurity Case argument is intentionally not provided in the Security Package by the Project (see :need:`wf__cr_mt_security_package`); it is covered by a dedicated work product, if created for the Module.

        * - 3
          - Are the referenced work products available?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6491>`
          - <Rationale for result>

        * - 4
          - Are the referenced work products in released state, including the Cybersecurity Assessment report (ISO SAE 21434 clause 6.4.8)?
          - [YES | NO ]
          - :need:`[[title]] <std_wp__isosae21434__prj_management_653>`
          - <Rationale for result>

        * - 5
          - Has the Organizational Cybersecurity Audit (ISO SAE 21434 clause 5.4.7) been performed, or is omitting it justified in the Security Plan's tailoring section? Note: this is distinct from the project-level Cybersecurity Assessment checked above.
          - NO
          - :need:`[[title]] <std_wp__isosae21434__org_management_555>`
          - The Organizational Cybersecurity Audit is currently tailored out at process level (:need:`wf__p_fs_audit_security`, needs discussion).

        * - 6
          - If security related deviations from the process or security concept are documented, are these argued understandably?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6471>`
          - <Rationale for result>

        * - 7
          - Are the requirements for post-development available, together with the cybersecurity-relevant information needed for continued conformance (e.g. open weaknesses/vulnerabilities, verification/validation results)?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6491>`, :need:`[[title]] <std_req__isosae21434__prj_management_6492>`
          - <Rationale for result>

        * - 8
          - If off-the-shelf/third-party (OTS/OSS) components are part of the Module, is their cybersecurity qualification (e.g. maintenance status, CVE history, SBOM) documented?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6461>`, :need:`[[title]] <std_req__isosae21434__prj_management_6462>`
          - <Rationale for result>
