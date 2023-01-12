MarketType
==========

A `MarketMaker <market-maker.html_>` can run several types of Markets. For example, it can run an
hourly real-time market and also an ancillary services market for Regulation.

This is captured by the concept of **MarketType**. Each MarketType has a unique name, and the
list of possible MarketTypes is encoded in the GridWorks enum MarketTypeName.

Additional information about the Market - the duration of the market slots, the duration of
gate closing (the time before the start of a MarketSlot by which all bids must be received) -
is encapsulated in the MarketType dataclass.
