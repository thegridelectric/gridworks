GridWorks
=========

GridWorks uses distributed actors to balance the electric grid. What does this mean?  In today's world, more
power comes from highly variable power sources such as wind and solar. And yet, the number
of electrons going into the grid must match the number coming out.  This is where GridWorks comes in.
GridWorks technology enables electrical devices with some embedded storage or with flexibility to provide grid
balancing. Furthermore, GridWorks allows these appliances to be more thrifty, using electricity when
it is cheap and green.

To start learning how to use this SDK, and how developing GridWorks actors can support a cost-effective and rapid transition to a sustainable future,
watch the beginning of the GridWorks story in `this 5 minute video <https://www.youtube.com/watch?v=5QFNQcp2Yzs>`_,
and then go through the `demo <story.html>`_ sequence, where we walk through a 10 MW simulation of transactive heating in
and around wind farms in New England - wind farms that are getting curtailed off more than 20% of the year.

To learn how using and contributing to GridWorks can support a cost-effective and rapid transition to a sustainable future:

- Watch the beginning of the GridWorks story in `this 5 minute video <https://www.youtube.com/watch?v=5QFNQcp2Yzs>`_
- Try some `Hello World <hello-gridworks.html>`_ examples
- Walk through this `10 MW simulation <story.html>`_ of how GridWorks, if deployed in new heating systems, could cut home heating costs in half while reducing or eliminating the curtailing (i.e. turning off and wasting) of wind power
- Learn the ropes of `GridWorks Communications <api-sdk-abi.html>`_

Algorand Blockchain Mechanics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gridworks runs markets between distributed actors acting as avatars for physical devices on the grid. It needs a foundation of trustless, secure, scalabe validation and authentication. Out of the gate, you will need to understand how to work with the Algorand blockchain. If Algorand
development is new to you or you want a refresher, consider starting `here <blockchain.html>`_.

**GridWorks SDKs**

This SDK (`gridworks on PyPI <https://pypi.org/project/gridworks/>`_) provides basic shared mechanics for communication and GNode structure. It is used as a package
in all of our other repos. GNodes come in flavors (classified by their `GNodeRole <g-node-role.html>`_), depending
on how they function within GridWorks. Some of these roles should naturally have their own packages.

For example,
`gridworks-atn <https://gridworks-atn.readthedocs.io/en/latest/>`_ is our Python SDK for building
`AtomicTNodes <atomic-t-node.html>`_. These are the GridWorks
actors that make electrical devices *transactive*. This SDK is a great place to learn about blockchain
mechanics, as it introduces some of the simpler structures (NFTs, stateless contracts, and then some
simple stateful smart contracts constructed using  `beaker <https://github.com/algorand-devrel/beaker>`_)
required for establishing the link between physical reality on the electric grid and the actors that play
their avatars in GridWorks.  The `gridworks-marketmaker <https://github.com/thegridelectric/gridworks-marketmaker>`_
repo, used to run the MarketMaker in the demo, will also become a package shortly.

There are several other open source GridWorks repos to explore on `our github page <https://github.com/thegridelectric>`_,
including the code running on the `SCADA systems <https://github.com/thegridelectric/gw-scada-spaceheat-python>`_
that Efficiency Maine is deploying in Millinocket this winter.
The  `GNodeFactory <https://github.com/thegridelectric/g-node-factory>`_ currently hosts the demo,
and  does most of the heavy lifting in terms of identity management and authentication in GridWorks. Finally, since the demo
is a distributed simulation, it needs a method of handling time. That's done by a `TimeCoordinator <https://github.com/thegridelectric/gridworks-timecoordinator>`_ GNode.


Installation
^^^^^^^^^^^^^

.. note::
    gridworks requires python 3.10 or higher.


.. code-block:: console

    (venv)$ pip install gridworks


.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Demo

    Story <story>

.. toctree::
    :hidden:
    :maxdepth: 3
    :caption: Domain

    Physics <physics>
    Economics <economics>
    Transactive Energy <transactive>
    Blockchain <blockchain>

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Code Support

    Hello GridWorks <hello-gridworks>
    APIs, SDKs, ABIs <api-sdk-abi>
    Lexicon <lexicon>

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: API docs

    Type APIs <apis/types>

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: SDK docs

    ActorBase <actor-base>
    AlgoUtils <algo-utils>
    ApiUtils <api-utils>
    Config <gw-config>
    DataClasses <data-classes>
    Enums <enums>
    Types <sdk-types>

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Participate

    Contributing <contributing>
    Code of Conduct <codeofconduct>
    License <license>
