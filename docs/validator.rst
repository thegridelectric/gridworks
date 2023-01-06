
Validator
============


A **Validator** is an entity authorized to validate Transactive Devices.
Anyone can become a validator, once they have gone through the
Validator Certification process with the GNodeFactory.

A Validator's credentials can be checked on-chain by the existence
of their Validator Certificate in a two-signature-required multi account
with the GnfAdminAddress.

.. image:: images/validator-cert-flow.png
   :alt: Validator Cert Flow
   :align: left

The Validator role is a key in establishing the link of trust between a
`Transactive Device <transactive-device.html>`_ and its `TerminalAsset <terminal-asset.html>`_. In the `Millinocket demo <story>`_, the first step is a fictitious entity called
Molly Metermaid going through the validation certification process.

.. image:: images/mollymetermaid-actor-artifact-v1.png
   :alt: Molly Metermaid
   :align: left

Who is likely to become a Validator? Organizations that provide Measurement and Verification
services to utilities and grid operators are likely candidates. These are organizations involved
in evaluating efficiency progams and Demand Response progams.


.. image:: images/core-actor-triangle-artifact-v1.png
   :alt: Triangle of Validation
   :align: left


TODO: add link to the relevant APIs and SDKs

`Back to Lexicon <lexicon.html>`_
