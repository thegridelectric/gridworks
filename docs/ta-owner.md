# TaOwner

The **TaOwner** is the entity who owns a [Transactive Device](transactive-device) in the real world,
and its associated [TerminalAsset](terminal-asset) in GridWorks. Ownership of a
TerminalAsset by the TaOwner is established by a [TaDeed](ta-deed),
which is an Algorand object.

The TaDeed for a TerminalAsset will change from time to time, for example
as the [GNodeAlias](g-node-alias) for the TerminalAsset changes. The GNodeAlias is a structured
identifier that helps capture the topology of the electric grid, and as such
it is mutable, perhaps changing a handful of times over the lifetime of the
GNode.

The TaOwner will often be a human. It is not appropriate, therefore, to expect an
action from the TaOwner when the TaDeed changes. This is done by putting the
TaDeed into the care of a [TaDaemon](ta-daemon) application.

_Back to [Lexicon](lexicon)_
