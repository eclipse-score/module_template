..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
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

AoU Requirements Template
=========================

This page contains Assumption of Use requirement snippets that belong to the
template repository.

Platform AoU
------------

.. code-block:: rst

   .. aou_req:: Some Other Title
      :id: aou_req__platform__some_other_title
      :reqtype: Interface
      :security: YES
      :safety: ASIL_B
      :status: invalid

      The Platform User shall do xyz to use the platform safely.

Feature AoU
-----------

.. code-block:: rst

   .. aou_req:: Some Other Title
      :id: aou_req__feature_name__some_other_title
      :reqtype: Process
      :security: NO
      :safety: ASIL_B
      :status: invalid

      The Feature User shall do xyz to use the feature safely.

Component AoU
-------------

.. code-block:: rst

   .. aou_req:: Next Title
      :id: aou_req__component_name__next_title
      :reqtype: Process
      :security: YES
      :safety: ASIL_B
      :status: invalid

      The Component User shall do xyz to use the component safely/securely

   .. aou_req:: Another Title
      :id: aou_req__component_name__another_title
      :reqtype: Process
      :security: YES
      :safety: ASIL_B
      :status: invalid
      :tags: environment

      The Component shall only be used in a xyz environment to ensure its proper functioning.