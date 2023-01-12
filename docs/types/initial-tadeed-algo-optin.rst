InitialTadeedAlgoOptin
==========================
Python pydantic class corresponding to  json type ```initial.tadeed.algo.optin```.

.. autoclass:: gridworks.types.InitialTadeedAlgoOptin
    :members:

**TerminalAssetAlias**:
    - Description: The GNodeAlias of the TerminalAsset
    - Format: LeftRightDot

**TaOwnerAddr**:
    - Description: The Algorand address of the owner for the TerminalAsset
    - Format: AlgoAddressStringFormat

**ValidatorAddr**:
    - Description: Address of the TaValidator. The Algorand address of the TaValidator who has validated the location, device type, and power metering of the TerminalAsset.
    - Format: AlgoAddressStringFormat

**SignedInitialDaemonFundingTxn**:
    - Description: . Funding transaction for the TaDaemon account, signed by the TaOwner.
    - Format: AlgoMsgPackEncoded

.. autoclass:: gridworks.types.initial_tadeed_algo_optin.check_is_algo_address_string_format
    :members:


.. autoclass:: gridworks.types.initial_tadeed_algo_optin.check_is_algo_msg_pack_encoded
    :members:


.. autoclass:: gridworks.types.InitialTadeedAlgoOptin_Maker
    :members:
