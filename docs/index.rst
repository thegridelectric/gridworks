GridWorks
=========

GridWorks uses distributed actors to balance the electric grid. What does this mean?  In today's world, more
power comes from highly variable power sources such as wind and solar. And yet, the number
of electrons going into the grid must match the number coming out.  This is where GridWorks comes in.
GridWorks technology enables electrical devices with some embedded storage or with flexibility to provide grid
balancing. Furthermore, GridWorks allows these appliances to be more thrifty, using electricity when
it is cheap and green.

To learn how using and contributing to GridWorks can support a cost-effective and rapid transition to a sustainable future:

- Try some simple `Hello World <hello-gridworks.html>`_ examples;
- Read the `Millinocket Story <millinocket-demo.html>`_ to learn how to exploit the synergy between wind power and space heating;
- Go through the partner `Millinocket Tutorial <millinocket-tutorial.html>`_.

Blockchain Mechanics
^^^^^^^^^^^^^^^^^^^^^

Gridworks runs markets between distributed actors acting as avatars for physical devices on the grid. It needs a
foundation of trustless, secure, scalable validation and authentication. It heavily uses the Algorand blockchain. If
you want to undestand more about how and why this is, go `here <blockchain.html>`_.

GridWorks SDKs
^^^^^^^^^^^^^^^

 - **gridworks**: `package <https://pypi.org/project/gridworks/>`_ provides basic shared mechanics for  communication and GNode structure. It is used as a package in all of our other repos.


 - **gridworks-atn**:  `package <https://pypi.org/project/gridworks-atn/>`_ and associated `documentation <https://gridworks-atn.readthedocs.io/en/latest/>`_ for the GridWorks Python `AtomicTNodes <atomic-t-node.html>`_  SDK. AtomicTNodes  are the GridWorks actors that make electrical devices *transactive*. This SDK is a great place to learn about blockchain mechanics, as it introduces some of the simpler structures (NFTs, stateless contracts, and then some simple stateful smart contracts constructed using  `beaker <https://github.com/algorand-devrel/beaker>`_) required for establishing the link between physical reality on the electric grid and the actors that play their avatars in GridWorks.  

 - **gridworks-marketmaker**: `package  <https://pypi.org/project/gridworks-marketmaker/>`_ and associated `documentation <https://gridworks-marketmaker.readthedocs.io/en/latest/>`_ for our Python `MarketMaker <market-maker.html>`_ SDK.  GridWorks uses distributed actors to balance the electric grid, and MarketMakers are the actors brokering this grid balancing via the markets they run for energy and balancing services.

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
    :maxdepth: 3
    :caption: Millinocket, ME

    Millinocket Demo <millinocket-demo>
    Millinocket Tutorial <millinocket-tutorial>

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
    AlgoSetup <algo-setup>
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
