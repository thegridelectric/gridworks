GNode
-----

A **GNode** is the fundamental building block of GridWorks. The `G` stands for grid.

Many of the lead roles in the `demo <story.html>`_ are GNodes: the
`SCADA <scada.html>`_, the `TerminalAsset <terminal-asset.html>`_,
the `MarketMaker <market-maker.html>`_ and the `AtomicTNodes <atomic-t-node.html>`_.


GNodes are organized in a tree structure that roughly tracks a natural hierarchy of voltage on the grid:


.. image:: images/g-node-tree.png
   :alt: g-node-tree
   :align: center


Some of the GNodes are **Copper GNodes**, which means they represent physical copper on the grid. The Copper GNodes
form a spanning tree of the known topoogy of the electric grid, and a sub-tree of the GNode Tree.

In SDK:

  - TODO: hyperlink to GNode dataclass inside the SDK  `Data Classes <data-classes.html>`_
  - TODO: hyperlink to GNodeGt inside the SDK `Types <types.html>`_
