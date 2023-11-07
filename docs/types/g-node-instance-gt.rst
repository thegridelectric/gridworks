GNodeInstanceGt
==========================
Python class corresponding to the GridWorks type g.node.instance.gt.000 (VersionedTypeName).

.. autoclass:: gridworks.types.GNodeInstanceGt
    :members:

**GNodeInstanceId**:
    - Description: Immutable identifier for GNodeInstance (Gni)
    - Format: UuidCanonicalTextual

**GNode**:
    - Description: The GNode represented by the Gni

**Strategy**:
    - Description: Used to determine the code running in a GNode actor application

**Status**:
    - Description: Lifecycle Status for Gni

**SupervisorContainerId**:
    - Description: The Id of the docker container where the Gni runs
    - Format: UuidCanonicalTextual

**StartTimeUnixS**:
    - Description: When the gni starts representing the GNode. Specifically, when the Status changes from Pending to Active. Note that this is time in the GNode's World, which may not be real time if it is a simulation.
    - Format: ReasonableUnixTimeS

**EndTimeUnixS**:
    - Description: When the gni stops representing the GNode. Specifically, when the Status changes from Active to Done.

**AlgoAddress**:
    - Description: Algorand address for Gni
    - Format: AlgoAddressStringFormat

.. autoclass:: gridworks.types.g_node_instance_gt.check_is_reasonable_unix_time_s
    :members:


.. autoclass:: gridworks.types.g_node_instance_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gridworks.types.g_node_instance_gt.check_is_algo_address_string_format
    :members:


.. autoclass:: gridworks.types.GNodeInstanceGt_Maker
    :members:
