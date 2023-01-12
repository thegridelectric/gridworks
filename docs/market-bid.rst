Market Bid
===========

Bidders in MarketMaker markets can be GNodes with the following roles:
   - AtomicTNode
   - MarketMaker
   - AggregatedTNode

To start understanding how this works, you can assume that the bidder is an AtomicTNode.
(The other roles allow for different ways of aggregation and scaling).

In most commodity exchanges, participants can provide *bids* (participants who want to buy
the commodity) or they can provide *offers* (participants who want to sell the commodity).

For GridWorks, both sides submit the same kind of bid, in the form of an `atn.bid` object.

The fundamental part of the `atn.bid` is a BidList, which is a set of unitless price/quantity
pairs. The bid also includes the units in question, for example price in USDPer Mwh and quantity
in AvgMW. Since there is not a clear convention about whether positive power means *injecting*
or *withdrawing*, there is also a boolean toggle for this (InjectionIsPositive).

We describe the convention and meaning assigned to these messages, and give a few examples.
TODO: add!

`Back to Lexicon <lexicon.html>`_
