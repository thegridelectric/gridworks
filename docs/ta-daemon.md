# TaDaemon

A TaDaemon (Ta for [TerminalAsset](terminal-asset)) is a piece of code devoted to serving
its [TaOwner](ta-owner) (usually a human). You can think of it as a combined butler, money
manager and personal lawyer. The TaDaemon has an Algorand address
(TaDaemonAddr). The TaOwner's ownership of the TerminalAsset is established
by the ownership of a [TaDeed](ta-deed) by the TaDaemonAddr.

The TaDaemon has two main functions.

- It keeps the TaDeed and [TaTradingRights](ta-trading-rights) up to date
- It enters into a representation contract at the behest of its TaOwner.

The first task is managed in coordination with the [GNodeFactory](g-node-factory), and is fairly
simple: when the GNodeFactory makes a new TaDeed for its TerminalAsset, the
TaDaemon returns the old TaDeed and opts into the new TaDeed.

The second task is more complex. It involves providing the TaTradingRights
to an [AtomicTNode](atomic-t-node), and entering into a long-term financial agreement that
involves both receiving and sending money in a triangle involving
the AtomicTNode and its [MarketMaker](market-maker).

_Back to [Lexicon](lexicon.md)_
