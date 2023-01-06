GNodeInstance
=============

A **GNodeInstance** is the one of the layers of abtraction connecting a GNode with a running app in
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


.. module:: gridworks.types

.. automodule:: gridworks.types.g_node_instance_gt
    :members:

.. autoclass:: GNodeInstanceGt
    :members:

.. module:: gridworks.types

.. autoclass:: SupervisorContainerGt
    :members:

.. automodule:: gridworks.types.supervisor_container_gt
    :members:

.. module:: gridworks.types

.. autoclass:: SupervisorContainerGt
    :members:


.. automodule:: gridworks.types.heartbeat_a
    :members:

.. autoclass:: HeartbeatA
    :members:

`Back to Lexicon <lexicon.html>`_
