TaTradingRights
================

A TaTradingRights certificate (`Ta` for `TerminalAsset <terminal-asset.html>`_) is an Algorand
blockchain object that provides an `AtomicTNode <atomic-t-node.html>`_ with the authority to:

   - enter in to a `DispatchContract <dispatch-contract.html>`_ with a `SCADA <scada.html>`_; and
   - participate in `MarketMaker <market-maker.html>`_ markets on behalf of the TerminalAsset.


TaTradingRights technical details
^^^^^^^^^^^^^^^^^^^^^^^^

As with `TaDeeds <ta-deed.html>`_, TaTradingRights can either be  Algorand Standards Assets (ASAs), or
Algorand Smart Contracts. In both cases, the
TaTradingRights makes publicly available the `GNodeAlias <g-node-alias.html>`_ of the TerminalAsset, and the
Algorand address of the `TaValidator <ta-validator.html>`_.

ASA TaTradingRights specs
^^^^^^^^^^^^^^^^^

An ASA TaTradingRights certificate is an Algorand Standard Asset where:
 - `Creator (aka Sender) <https://developer.algorand.org/docs/get-details/transactions/transactions/#sender>`_ is `GnfAdminAddr <g-node-factory.html#gnfadminaddr>`_
 - `Total <https://developer.algorand.org/docs/get-details/transactions/transactions/#total>`_ is 1
 - `UnitName <https://developer.algorand.org/docs/get-details/transactions/transactions/#unitname>`_ is "TATRADE"
 - `ManagerAddr <https://developer.algorand.org/docs/get-details/transactions/transactions/#manageraddr>`_ is GnfAdminAddr
 - `AssetName <https://developer.algorand.org/docs/get-details/transactions/transactions/#assetname>`_ has the LeftRightDot format, and is no more than 32 characters


SmartSignature TaDeed specs
^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Back to `Lexicon <lexicon.html>`_*
