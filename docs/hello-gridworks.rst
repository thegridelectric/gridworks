
Hello World
============


.. note::
    All GridWorks repos assume Python 3.10 or higher, docker, and the Algorand
    `sandbox <https://github.com/algorand/sandbox>`_. Also, For these ```hello world``` examples,
    please clone `this repo <https://github.com/thegridelectric>`_  in order to spin up
    a local rabbit broker.


GridWorks  is message-driven, following `the reactive manifesto <https://www.reactivemanifesto.org/>`_.
The basic building blocks are `GNodes <g-node.html>`_ ('G' stands for the electric grid). GNode
actors communicate via:

  1) Asynchronous message-passing on a RabbitMQ Broker;
  2) API calls via FastAPI interfaces; and
  3) Calls to the Algorand blockchain ledger, typically usually smart contract ABI method calls.


Hello Rabbit
^^^^^^^^^^^^^

Here is a simple example of the first. Before running, start a development world rabbit broker. From
the top level of this repo:

   1) **./arm.sh**  (*if your computer has an arm chip*)
   2) **./x86.sh**   (*x86 chip*)

Wait for the `rabbit admin page <http://0.0.0.0:15672/>`_ to load (username/passwd smqPublic)


.. literalinclude:: ../examples/hello.py



Hello Algorand
^^^^^^^^^^^^^^^

The first Algorand transaction that occurs in any full simulation is the creation of a `TaValidator Certificate <ta-validator.html#tavalidator-certificate>`_.
(For quick context, a TaValidator is an entity involved in establishing the link between GridWorks avatars for real-world devices attached to the electric grid.)

This certificate is an example of an Algorand Non-fungible Token (NFT).  More specifically, an NFT it is an Algorand Standard Asset (ASA) whose
`total <https://developer.algorand.org/docs/get-details/transactions/transactions/#total>`_ is 1 (this is how uniqueness in enforced).
You may have heard about NFTs in the `context of art <https://www.algorand.foundation/nfts>`_. We are using NFTs in a similar way -
s an identifiable object that can only be owned by a single entity.

All ASAs have *creators* -  identified by the Algorand address that pays the fee for the creation transaction
(aka the `sender <https://developer.algorand.org/docs/get-details/transactions/transactions/#sender>`_). One of the criterion for an ASA being a
TaValidator Certificate is that the creator's address  must be a 2-signature MultiSig address.


.. code-block:: python
   :caption: Creating a 2-sig MultiAddress [GnfAdminAddr, ValidatorAddr]

   from gridworks.gw_config import Public
   from gridworks.algo_utils import BasicAccount

   validator_acct = BasicAccount()
   gnf_admin_addr = Public().gnf_admin_addr
   msig = Multisig(
      version=1,
      threshold=2,
      addresses = [gnf_admin_addr, validator_acct.addr]
   )

   print(msig.address())

TODO: code block using algo_util.MultiAccount to crreate the same multi.

TODO: give an example of creating an NFT.
ASAs have unique identifiers on the blockchain. These are called Asset Ids, or Asset Indices, and they are integers.

Hello FastAPI
^^^^^^^^^^^^^^
