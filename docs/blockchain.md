# The Algorand Blockchain

Working knowledge of some basic Algorand tech is necessary to start developing with GridWorks:

- [py-algorand-sdk](https://pypi.org/project/py-algorand-sdk/), the Algorand Python SDK
- [Algorand Standard Assets](https://developer.algorand.org/docs/get-details/asa/)
- [Algorand Smart Signatures](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/frontend/smartsigs/)

These tools are used for establishing the link between GNodes and Physical Devices. For example, in order to create TerminalAssets and AtomicTNodes you will need to get [TaDeeds](ta-deed) and [TaTradingRights](ta-trading-rights) from the GNodeFactory. Jump down to Creating a TaDeed to
start working through this.

As you explore more, for example if you are digging into the mechanics of the [demo](story),
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
