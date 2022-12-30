GNode
-----

A **GNode** is the fundamental building block of GridWorks. The `G` stands for grid.

Many of the lead roles in the `demo <story.html>`_ are GNodes: the
`SCADA <scada.html>`_, the `TerminalAsset <terminal-asset.md>`_,
the `MarketMaker <market-maker.md>`_ and the `AtomicTNodes <atomic-t-node.md>`_.


GNodes are organized in a tree structure that roughly tracks a natural hierarchy of voltage on the grid:


.. image:: images/g-node-tree.png
   :alt: g-node-tree
   :align: center


Some of the GNodes are **Copper GNodes**, which means they represent physical copper on the grid. The Copper GNodes
form a spanning tree of the known topoogy of the electric grid, and a sub-tree of the GNode Tree.

GridWorks has a dataclass for GNodes:

.. module:: gridworks.data_classes.g_node

.. autoclass:: GNode
    :members:




There is also a GridworksSchema of type ```g.node.gt``` used to send messages about GNodes:

.. module:: gridworks.schemata

.. autoclass:: GNodeGt
    :members:

`Back to Lexicon <lexicon.html>`_
