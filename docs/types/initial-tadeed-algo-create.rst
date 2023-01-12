InitialTadeedAlgoCreate
==========================
Python pydantic class corresponding to  json type ```initial.tadeed.algo.create```.

.. autoclass:: gridworks.types.InitialTadeedAlgoCreate
    :members:

**ValidatorAddr**:
    - Description: Address of the TaValidator. The Algorand address of the TaValidator who is going to validate the location, device type, and power metering of the TerminalAsset.
    - Format: AlgoAddressStringFormat

**HalfSignedDeedCreationMtx**:
    - Description: Algo mulit-transaction for TaDeed creation
    - Format: AlgoMsgPackEncoded

.. autoclass:: gridworks.types.initial_tadeed_algo_create.check_is_algo_address_string_format
    :members:


.. autoclass:: gridworks.types.initial_tadeed_algo_create.check_is_algo_msg_pack_encoded
    :members:


.. autoclass:: gridworks.types.InitialTadeedAlgoCreate_Maker
    :members:
