# Conductor Topology Node

The interior nodes of the copper spanning tree are places where multiple lines come together. Often, there will also be some sort of voltage transformation. These can be circuit breaker panels in houses, transformers on poles, or substations. These are all examples of **ConductorTopologyNodes**, or `CTN` for short. When a `CTN` becomes the focal point of a constraint on power flow - like Keene Rd in our demo - the corresponding GNode can get its role upgraded by the [GNodeFactory](g-node-factory) from ConductorTopologyNode to
[MarketMaker](market-maker).

GNodes with this role are **copper GNodes**, and they typically are _passive_ - that is, they do not have actors, but instead serve the function of helping track the grid topology.

_Back to [Lexicon](lexicon)_
