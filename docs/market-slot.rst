MarketSlot
==========

A `MarketMaker <market-maker.html_>` can run several types of Markets. For example, it can run an
hourly real-time market and also an ancillary services market for Regulation.

This is captured by the concept of `MarketType <market-type.html>`_.

A given MarketType partitions time into MarketSlots. For example, an hourly
market will have a new MarketSlot that starts at the top of each hour.

MarketSlotName
^^^^^^^^^^^^^^^
The MarketSlotName encodes:
  - The MarketType (the first word)
  - The start of that MarketSlot (last word)
  - The GNodeAlias of its MarketMaker (middle words)

Example: rt60gate5.d1.isone.ver.keene.1673539200

`Back to Lexicon <lexicon.html>`_
