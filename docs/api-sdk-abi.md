# APIs,SDKs, and ABIs

The foundational GridWorks package [gridworks](https://pypi.org/project/gridworks/), which is the source of this documentation, is designed to help you set up an API and its corresponding SDK in a development environment and learn the ropes for core GridWorks communication mechanics.

Imagine all the applications in Gridworks as cells in an organism. They have ways of communicating with other cells, and this is captured in their cell membranes. Some of these apps
are GNode actors, but othes (like this tutorial service) are not.

**APIs**
An app's APIs (Application Binary Interface) specify how communication happens at and beyond its cell membranes.

**SDKs**
An app's SDK, on the other hand, is like an internal organelle capable of generating valid messages to send out to other cells.

**ABIs**
Some of the applications in GridWorks are Algorand Smart Contracts. These have ABIs
(application binary interfaces) instead of APIs. We will explain why.

An ABI is a specification for communicating _inwardly_ to, say, the cell's mitochondria. ABIs are familiar to c programmers as a way of arranging memory layout. The Algorand blockchain is like a computer whose guts are spread out across the Internet: a tiny (compared to most ec2 instances), Turing complete computer whose every action is visible for the world to see. Therefore, a method call to an Algorand Smart Contract is much more like a C ABI than a Restful API with a url endpoint.

For more information on Algorand ABIs:

- A [40 minute youtube](https://www.youtube.com/watch?v=mdM6KrGC61k) discussing the launch
  of Algorand ABIs
- [ARC-4](https://arc.algorand.foundation/ARCs/arc-0004), the source of truth for implementation details
- [pyteal ABI support docs](https://pyteal.readthedocs.io/en/stable/abi.html)
- [AlgoBank ABI example](https://github.com/algorand/pyteal/tree/master/examples/application/abi)

**Coherence**
GridWorks applications all have their own APIs. How does this not
turn into a tower of babel? The `TypeName` and `Version` uniquely specify how a particular
serialized json object is validated. This is globally true across all of GridWorks.
For example, the API Type specification for TypeName `ready`, version `001`
is the same in API for this repo[TODO: add link], and in the GNodeFactory[TODO: add link].
Likewise, the python SDK implementations for a specific TypeName/Version is the same
in all repos. COMING SOON: a `gridworks-type-registry` to be the global authority
in case of mismatch.
