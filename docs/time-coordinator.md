# TimeCoordinator (GNodeRole)

A TimeCoordinator is a GNode responsible for managing time in simulation. Typically, a simulation will have a single TimeCoordinator which is a direct
descendant of the WorldGNode. For example, `d1.time` is the alias of the
TimeCoordinator in the [Millinocket demo](story), using
[this gridworks repo](https://github.com/thegridelectric/gridworks-timecoordinator).

It is also possible to have a hierarchy of TimeCoordinators working together. This could be useful in a simulation where a loosely tied sub-grid requires
higher time resolution in order for the networks simulations to converge.

_Back to [Lexicon](lexicon.md)_
