# AggregatedTNode

An **AggregatedTNode** ("T" for Transactive) is an aggregation of [AtomicTNodes](atomic-t-node).

The individual AtomicTNodes within the AggregatedTNode must share the same [MarketMaker](market-maker) GNode.
The MarketMaker for an AtomicTNode is the first MarketMaker encountered when walking up the GNodeTree branch
from the AtomicTNode - that is, the youngest MarketMaker ancestor of the AtomicTNode).

An AtomicTNode cannot participate in a market run by the MarketMaker if it is part of an AggregatedTNode that
is also participating in that market. That is, it can't buy (or sell) energy twice.

When an AggregatedTNode takes over the market participation, it must handle the dispatch of its AtomicTNodes out of the market.

AggregatedTNodes may be created by businesses that prefer to have a coarser-grained bidding strategy (although
they will still be responsible for providing the granular, metered consumption data for settlement).

Another reason to create an AggregatedTNode is if a MarketMaker has a minimum size requirement for market
participation. While the default MarketMakers provided by GridWorks will not have this restriction, the
design of the system allows for it.

_Back to [Lexicon](lexicon.md)_
