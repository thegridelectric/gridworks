# AtomicMeteringNode

**AtomicMeteringNode** is a helper [GNodeRole](g-node-role) and [CoreGNodeRole](core-g-node-role). Essentially, it is the larval form of an [AtomicTNode](atomic-t-node).

This GNode for a pending `AtomicTNode` must _exist_ at the time of creation of its `TerminalAsset`, since it is the _parent_ of the `TerminalAsset`. However, it cannot become an `AtomicTNode` until it owns the [TaTradingRights](ta-trading-rights) for the `TerminalAsset`.

_Back to [Lexicon](lexicon)_
