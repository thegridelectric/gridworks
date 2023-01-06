GNodeStatus
============
GNodeStatus is an `Enum <enums.html#gridworks.enums.GNodeStatus>`_ for managing GNode lifecycle.

Pending
^^^^^^^^
The GNode exists but cannot be used yet. The GNodeId and GNodeAlias are reserved at this point.

Used for example when a TerminalAsset has been created but does not yet have its TaDeed.

Active
^^^^^^^

For passive GNodes that represent physical objects, like TerminalAssets, a Status of active means there is evidence supporting the existence of the TerminalAsset. A GNodeStatus of active is required in order for any contract to be entered to that requires trading rights for and/or a deed for a passive GNode.

For GNodes with actors, a Status of active is required for any authorized actor to send a message representing itself as that GNode.

If a GNode is Active, its parent GNode MUST ALSO be active.

PermanentalyDeactivated
^^^^^^^^^^^^^^^^^^^^^^^^
For passive GNodes, like TerminalAssets, this designation means no contracts may be entered into and no deed may be held for this GNode.  For active GNodes, no message may be sent from this GNode. Once a GNode is PermanentlyDeactivated it can have no other status in the future.


Suspended
^^^^^^^^^^
The GNode cannot be used, but may become active in the future. This is used,
for example, if certification for a TerminalAsset has lapsed.



`Back to Lexicon <lexicon.html>`_
