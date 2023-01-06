InitialTadeedAlgoTransfer
==========================
Python pydantic class corresponding to  json type ```initial.tadeed.algo.transfer```.

.. autoclass:: gridworks.types.InitialTadeedAlgoTransfer
    :members:

**MicroLat**:
    - Description: . The Latitude of the Transactive Device, times 10^6

**MicroLon**:
    - Description: . The Longitude of the Transactive Device, times 10^6

**ValidatorAddr**:
    - Description: . The Algoand address for the TaValidator who validated the location,
        metering and type of the Transactive Device.
    - Format: AlgoAddressStringFormat

**TaDaemonAddr**:
    - Description: . The Algorand address for the TaDaemon which will own the TaDeed
         and initially the TaTradingRights), as well as holding funds on
        behalf of the TaOwner.
    - Format: AlgoAddressStringFormat

**TaOwnerAddr**:
    - Description: . The Algorand address of the entity owning the Transactive Device, and
        thus also the TerminalAsset
    - Format: AlgoAddressStringFormat

**FirstDeedTransferMtx**:
    - Description: . The half-signed multi transaction for transferring the TaDeed to the
        TaDaemon.
    - Format: AlgoMsgPackEncoded

.. autoclass:: gridworks.types.initial_tadeed_algo_transfer.check_is_algo_address_string_format
    :members:


.. autoclass:: gridworks.types.initial_tadeed_algo_transfer.check_is_algo_msg_pack_encoded
    :members:


.. autoclass:: gridworks.types.InitialTadeedAlgoTransfer_Maker
    :members:
