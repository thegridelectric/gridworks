# AtomicTNode

At a high level, an **AtomicTNode** is the GNode responsible for the behavior of a [TerminalAsset](terminal-asset) most of the time. It meets the
primary needs of the `TerminalAsset` (like providing heat, if the asset is a heating system), and it looks at future price and weather forecasts in order to optimize the participation of the TerminalAsset in electricity markets.

The AtomicTNode has a good internal model of how the TerminalAsset works, adjusting and double-checking this getting real-time data from the SCADA.

The owner of the TerminalAsset (TaOwner) chooses the AtomicTNode by entering into a multi-party Representation Contract.

The AtomicTNode has a close working relationship with the SCADA. In a nutshell, whenever the two are successfully communicating,
the SCADA lets the AtomicTNode call all the shots on how the TerminalAsset uses (or provides) electrical power.

**AtomicTNode** is a fundamental [GNodeRole](g-node-role) and [CoreGNodeRole](core-g-node-role).

_Back to [Lexicon](lexicon.md)_
