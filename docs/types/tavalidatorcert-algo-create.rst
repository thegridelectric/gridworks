TavalidatorcertAlgoCreate
==========================
Python pydantic class corresponding to  json type ```tavalidatorcert.algo.create```.

.. autoclass:: gridworks.types.TavalidatorcertAlgoCreate
    :members:



**HalfSignedCertCreationMtx**: This string is an encoded (algosdk.encoding.msgpack_encode) multiSigTransaction (mtx) signed by the pendingValidator. The mtx.txn is a AssetCreateTxn with sender=multi, total=1, frozen=False, manager=gnf.admin, unit_name="VLDTR", asset_name=valid asset name (str <= 32 char) chosen by pendingValidator, url= string chosen by pendingValidator.

**ValidatorAddr**: The address of the pending TerminalAsset validator.

.. autoclass:: gridworks.types.TavalidatorcertAlgoCreate_Maker
    :members:
