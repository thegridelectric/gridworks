TavalidatorcertAlgoTransfer
==========================
Python pydantic class corresponding to  json type ```tavalidatorcert.algo.transfer```.

.. autoclass:: gridworks.types.TavalidatorcertAlgoTransfer
    :members:



**ValidatorAddr**: The address of the pending TerminalAsset validator.

**HalfSignedCertTransferMtx**: This string is an encoded (algosdk.encoding.msgpack_encode) multiSigTransaction (mtx) signed by the pendingValidator. The mtx.txn is a AssetTransfer for a created ValidatorCertificate for the pendingValidator that the pendingValidator has opted in to.

.. autoclass:: gridworks.types.TavalidatorcertAlgoTransfer_Maker
    :members:
