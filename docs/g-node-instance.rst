GNodeInstance
=============

A **GNodeInstance** is the one of the layers of abstraction connecting a GNode with a running app in
a Docker container.  At any point in time, a GNode can be represented by only
one GNodeInstance.

Every GNodeInstance is subordinate to a `Supervisor <supervisor.html>`_ GNodeInstance which
runs a SupervisorContainer - typically a docker container running in the cloud. The SupervisorContainers are managed and spawned
by a `World <world-role.html>`_ GNodeInstance, which sits at the top of the GNodeTree
and is responsible for staying in touch in with the `GNodeFactory <g-node-factory.html>`_
for lifecycle status and private keys of its GNodes.

The Supervisor monitors the health of its subordinates with heartbeats, and
is responsible for killing and re-spawning any subordinate that fails to receive
or send messages in a reasonable timeframe.


GNodeInstanceId
^^^^^^^^^^^^^^^^

One of the primary ways GNode actors communicate with each other is via RabbitMQ messages. The actors share
their GNodeInstanceId in these messages in order to establish their credentials.

At the initiation of a conversation, a GNode's conversation partner can check in with the World Actor about
the credentials of the inbound message by getting a verification that the GNodeInstanceId matches the GNodeAlias.

Most actors find their GNodeInstance because they are on a docker instance that was started
by the World Actor, and the World Actor has placed a file with the relevant GNodeInstance data in the container.
If and when that container dies, a new GNodeInstance will be created for the GNode.

Scada GNodeInstanceId
^^^^^^^^^^^^^^^^^^^^^^

A Scada actor live on a Scada device that is sensing and controlling a Transactive Device. The Scada's process for getting assigned
to a GNodeInstance is therefore slightly different.

At the time of its installation, a SCADA device's GNodeAlias is naturally determined by the GNodeAlias of its
TerminalAsset (by appending `scada`).

But the system needs to  proof that a SCADA actor showing up with that GNodeAlias is in fact running on
the physical device.

Note that the `TaOwner <ta-owner.html>`_ holds  a `TaDeed <ta-deed.html>`_ establishing their ownership
of the associated TerminalAsset (in GridWorks) and Transactive Device (in the real world).
This means if the TaOwner signs a message with their private key, anybody can check that the entity that signed that
message owned the TerminalAsset.

The TaOwner therefore creates an Algorand account for
the Scada actor, puts that account's secret key on the Scada device, and then sends a signed request to the
GNodeFactory to create the Scada GNode with an associated ScadaAlgoAddr (the public address of the Scada's
Algorand account). When the Scada is establishing its identity with the DispatchContract it signs its
messages with this key.




`Back to Lexicon <lexicon.html>`_
