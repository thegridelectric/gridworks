TavalidatorcertAlgoCreate
==========================
Python pydantic class corresponding to  json type ```tavalidatorcert.algo.create```.

.. autoclass:: gridworks.types.TavalidatorcertAlgoCreate
    :members:

**ValidatorAddr**:
    - Description: The address of the pending TaValidator
    - Format: AlgoAddressStringFormat

**HalfSignedCertCreationMtx**:
    - Description: Algo multi-transaction for certificate creation, with 1 of 2 signatures
    - Format: AlgoMsgPackEncoded

.. autoclass:: gridworks.types.tavalidatorcert_algo_create.check_is_algo_address_string_format
    :members:


.. autoclass:: gridworks.types.tavalidatorcert_algo_create.check_is_algo_msg_pack_encoded
    :members:


.. autoclass:: gridworks.types.TavalidatorcertAlgoCreate_Maker
    :members:
