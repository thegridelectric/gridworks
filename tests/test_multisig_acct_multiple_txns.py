import algosdk
import pytest

import gridworks.algo_utils as algo_utils
import gridworks.dev_utils.algo_setup as algo_setup
import gridworks.gw_config as config


# def testSendMultipleTxns():
#     acct0: algo_utils.BasicAccount = algo_utils.BasicAccount()
#     acct1: algo_utils.BasicAccount = algo_utils.BasicAccount()
#     addresses = [acct0.addr, acct1.addr]

#     multi = algo_utils.MultisigAccount(version=1, threshold=1, addresses=addresses)
#     msig = algosdk.future.transaction.Multisig(version=1, threshold=1, addresses=addresses)

#     algo_setup.devFundAccount(
#         settingsAlgo=config.Algo(), toAddr=multi.addr, microAlgoAmount=1_000_000
#     )
#     #######################################################
#     # Testing that a MultisigAccount can be used to sign multiple transactions
#     ######################################################

#     # A key differene between a MultisigAccount and a Multisig is that the
#     # Multisig changes as it signs transactions because it adds the signature
#     # for its latest transaction to the related subsig.

#     # Practically speaking, this means the same MultisigAccount can be
#     # used to send multiple transactions - which is not true for a Multisig

#     # Multisig CANNOT RELIABLY SIGN MULTIPLE TRANSACTIONS

#     client = algo_utils.get_algod_lient(settingsAlgo=config.Algo())
#     txn0 = algosdk.future.transaction.AssetCreateTxn(
#         sender=msig.address(),
#         total=1,
#         decimals=0,
#         default_frozen=False,
#         asset_name="THING0",
#         sp=client.suggested_params(),
#     )
#     mtx0 = algosdk.future.transaction.MultisigTransaction(txn0, msig)

#     assert msig.subsigs[0].signature is None
#     mtx0.sign(acct0.sk)

#     init_subsig0 = msig.subsigs[0].signature
#     assert init_subsig0 is not None

#     txn1 = algosdk.future.transaction.AssetCreateTxn(
#         sender=msig.address(),
#         total=1,
#         decimals=0,
#         default_frozen=False,
#         asset_name="THING1",
#         sp=client.suggested_params(),
#     )
#     mtx1 = algosdk.future.transaction.MultisigTransaction(txn1, msig)
#     mtx1.sign(acct1.sk)
#     assert init_subsig0 == msig.subsigs[0].signature

#     with pytest.raises(algosdk.error.AlgodHTTPError):
#         client.send_transaction(mtx1)

#     # IN CONTRAST, the same thing evidently works with MultisigAccount,
#     # since the public addressed do not change
#     txn0 = algosdk.future.transaction.AssetCreateTxn(
#         sender=multi.address(),
#         total=1,
#         decimals=0,
#         default_frozen=False,
#         asset_name="THING0",
#         sp=client.suggested_params(),
#     )
#     mtx0 = multi.create_mtx(txn0)
#     mtx0.sign(acct0.sk)
#     client.send_transaction(mtx0)

#     txn1 = algosdk.future.transaction.AssetCreateTxn(
#         sender=multi.address(),
#         total=1,
#         decimals=0,
#         default_frozen=False,
#         asset_name="THING1",
#         sp=client.suggested_params(),
#     )
#     mtx1 = multi.create_mtx(txn1)
#     mtx1.sign(acct1.sk)
#     client.send_transaction(mtx1)
