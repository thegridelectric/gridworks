# The Algorand Blockchain

Gridworks is building a platform enabling distributed, decentralized, secure, and trustless transactions so that potentially millions of Transactive Energy Resources can interact with each other, the Grid Operator, and end users.

By `trustless`, what we mean is that counterparties do not need to rely on some central third party to broker their contract.
In fact, Gridworks foundations for a scalable, decentralized trustless market structure is based in establishing _links of trust_:
blockchain ASAs and/or SmartSigs establishing the rights of a GNode Actor to act as an avatar for a physical device. For example,
a) (and its relationship to a TaValidatorCert) bridges the gap between a third-party inspector evaluating the accuracy
of an electricity meter at a house, and the [TerminalAsset](terminal-asset) [GNode](g-node) avatar of the [Transactive Device](transactive-device) behind that meter.
For more information on this, read about why we call a TaDeed a [Link of Trust](https://gridworks.readthedocs.io/en/latest/ta-deed.html#link-of-trust).

Working knowledge of some basic Algorand tech is necessary to start developing with GridWorks:

- [py-algorand-sdk](https://pypi.org/project/py-algorand-sdk/), the Algorand Python SDK
- [Algorand Standard Assets](https://developer.algorand.org/docs/get-details/asa/)
- [Algorand Smart Signatures](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/frontend/smartsigs/)

These are the tools used for establishing the link between GridWorks and the real world. For example, in order to use an AtomicTNode
it a larger GridWorks simulation (including anytime you are outside of the [dev environment](universe)), the AtomicTNode's
GNode actor will need to own [TaTradingRights](ta-trading-rights) for its associated TerminalAsset. These foundational
GridWorks certificates and
their creation/transfer process are interlinked and have an initiatic sequencing. For example, TaValidatorCert -> TaDeed ->
TaTradingRights: (The TaValidatorCert for a TaValidator account must be created prior to the creation of a TaDeed, which
must be created prior to the creation of TaTradingRights.)
The first couple sections of the [Millinocket tutorial](millinocket-tutorial) walk through this process.

If you have never worked with blockchain before, it may take some time to get used to
the blockchain mechanics that show up in the first part of the tutorial. But once you get the hang of it, they become
simple to understand and use, and you can realize that these certificates are actually just the welcome mat into
the house.

Although these initial certificates are simple, they are also the single most essential part of blockchain used by
GridWOrks. Without something like the above for establishing proof of _when_, _where_ and _how much_ a device uses, Transactive
resources do not work at scale.

Once this trust is established, one can operate within the world of code: a system of distributed actors, their blockchain
holdings and/or identities, the rules governing how these actors and blockchain entities communicate, and the data they
create. This is what we typically mean by `GridWorks`. Even before using blockchain, GridWorks was built on a system
of contracts. The initial, most important contract is the [DispatchContract](dispatch-contract) between an AtomicTNode
and a SCADA both serving the same TerminalAsset. Note that this contract truly is an agreement between two code entities.
In the [Millinocket demo](millinocket-demo), the DispatchContract is monitoring and establishing the state of comms between
two actors working together to keep a house warm, where one of these actors lives behind a residential router in a
rural area of Maine. Built on top of the DispatchContract is the
[RepresentationContract](representation-contract), a multi-party contract used to establish the provision of a service
to a human or business customer (warmth as a service, in Millinocket) as well as the financial terms going along with
this. Unlike the DispatchContract, the RepresentationContract will involve _both_ code actors (AtomicTNode, MarketMaker)
_and_ humans/human businesses (HomeOwner, Aggregator, Grid Operator).

DispatchContract and the RepresentationContract
you will need to learn about Algorand Smart Contracts, written in Pyteal using Beaker. This
is the technology used in GridWorks for operating simple foundational contracts between GNodes and the entities (human or otherwise) that own or use them:

- TaDaemon App
- DispatchContract
- RepresentationContract

In addition, GridWorks is working on:

- **A Smart Contract implementation of MarketMaker GNodes** These second-generation MarketMakers will behave somewhat like the blockchain Automated Market Makers, or AMMs (see this [demo Algo example in beaker](https://github.com/algorand-devrel/beaker/tree/master/examples/amm)) to solve the Optimal Power Flow problems traditionally solved in centralized ways by Grid Operators to determine market clearing prices. The catch is that, unlike the liquidity pools of AMMs, this tree-like hierarchy of GNode MarketMakers must coordinate with each other, since they are solving a problem that is globally connected by the laws of physics (in particular, Kirchoff's laws).
- **A Smart Contract implementation of the GNodeFactory** The GNodeFactory is the Single Source
  of Truth in GridWorks for the known topology of the electric grid. At present, this information
  is stored in a database belonging to a centralized application. At scale, this topology and some the data used to back it up needs to be on-chain.

## Creating a TaDeed
