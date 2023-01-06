
SDK for Gridworks Types
=======================

Types are the building blocks for GridWorks APIs: they articulate
*what* is getting sent without specifying the *where* (i.e.,
a Restful API endpoint, or a queue in a rabbit broker) or *how* (i.e.,
specifying that a Restful POST requires *this* type, or returns *that* type).

As you are learning, you can assume that all Gridworks types are serialized JSON.
Json is the lingua franca of APIs. It is not a programming language,
it is more like a multi-dimensional graph structure.

The API specs for these GridWorks types is `here <apis/types.html>`_. The Python Type
SDKs provide a Pythonic method of creating valid instances of these types, and for
interpretting payloads as  natural Python objects.

You will notice massive overlap in the API specs and the SDK documentation for types.
Why is that?

Imagine the actors in GridWorks as cells in an organism. They have ways of communicating,
and this is captured in their cell membranes. An actor's APIs specify how it communicates
at and beyond its cell membranes. An SDK, in contrast,  is like an internal organelle
capable of generating valid messages to be sent out of the membrane.

The Purpose of This SDK
^^^^^^^^^^^^^^^^^^^^^^^^
This SDK, paired with its `API <apis/types.html>`_, is part of a Gridworks tutorial
application designed to teach the basic mechanics of communication in GridWorks.
Go `here <api-sdk-abi.html>`_ for instructions.

.. automodule:: gridworks.types

.. toctree::
   :maxdepth: 1
   :caption: TYPE SDKS

    GNodeGt  <types/g-node-gt>
    GNodeInstanceGt  <types/g-node-instance-gt>
    HeartbeatA  <types/heartbeat-a>
    Ready  <types/ready>
    SimTimestep  <types/sim-timestep>
    SuperStarter  <types/super-starter>
    SupervisorContainerGt  <types/supervisor-container-gt>
    TavalidatorcertAlgoCreate  <types/tavalidatorcert-algo-create>
    TavalidatorcertAlgoTransfer  <types/tavalidatorcert-algo-transfer>
