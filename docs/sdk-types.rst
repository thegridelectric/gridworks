
SDK for `gridworks <https://pypi.org/project/gridworks/>`_  Types
==================================================================

The Python classes enumerated below provide an interpretation of GridWorks
type instances (serialized JSON) as Python objects. Types are the building
blocks for GridWorks APIs. You can read more about how they work
`here <api-sdk-abi.html>`_, and examine their API specifications `here <apis/types.html>`_.
The Python classes below also come with methods for translating back and
forth between type instances and Python objects.


.. automodule:: gridworks.types

.. toctree::
   :maxdepth: 1
   :caption: TYPE SDKS

    BaseGNodeGt  <types/base-g-node-gt>
    GNodeGt  <types/g-node-gt>
    GNodeInstanceGt  <types/g-node-instance-gt>
    GwCertId  <types/gw-cert-id>
    HeartbeatA  <types/heartbeat-a>
    Ready  <types/ready>
    SimTimestep  <types/sim-timestep>
    SuperStarter  <types/super-starter>
    SupervisorContainerGt  <types/supervisor-container-gt>
