CoreGNodeRole
-------------

The CoreGNodeRole are a pared-down version of `GNodeRole <g-node-role>`_, restricted to:

- `TerminalAsset <terminal-asset.html>`_
- `AtomicTNode <atomic-t-node.html>`_
- `MarketMaker <market-maker.html>`_
- `AtomicMeteringNode <atomic-metering-node.html>`_
- `ConductorTopologyNode <conductor-topology-node.html>`_
- `InterconnectionComponent <interconnection-component.html>`_

and Other (to be used for all other GNodeRoles). These are the roles that perform crucial functions in establishing the grid topology and running the markets.
In order to be assigned any of these roles, the GNodeFactory must authorize the assignment.

For other roles, the GNodeFactory only needs to authorize the *creation* of the GNode (and assigns
it a default CoreGNodeRole of **other**).

GridWorks is designed to have a single GNodeFactory, which concerns itself with mapping out the
copper grid and the validation of metering.

However, GridWorks encourages the formation of *multiple* GNodeRegistries, each of which
can create their own breakdown of GNodeRoles.



`Back to Lexicon <lexicon.html>`_
