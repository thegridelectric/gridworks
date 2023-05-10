# World (as GNodeRole)

The World is an adminstrative GNode responsible for managing and authorizing which actor instances ( [GNodeInstances](g-node-instance)) are currently representing GNodes.

It gets information about identity (alias, location, private Algorand keys) for its GNodes
from the [GNodeFactory](g-node-factory). It is responsible for instantiating
GNodeInstances and managing the disbursement of their secrets.

For more details on these mechanics go [here](g-node-instance).

_Back to [Lexicon](lexicon)_
