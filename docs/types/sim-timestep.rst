SimTimestep
==========================
Python class corresponding to the GridWorks type sim.timestep.000 (VersionedTypeName).

.. autoclass:: gridworks.types.SimTimestep
    :members:

**FromGNodeAlias**:
    - Description: The GNodeAlias of the sender. The sender should always be a GNode Actor of role TimeCoordinator.
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: The GNodeInstanceId of the sender
    - Format: UuidCanonicalTextual

**TimeUnixS**:
    - Description: Current time in unix seconds
    - Format: ReasonableUnixTimeS

**TimestepCreatedMs**:
    - Description: The real time created, in unix milliseconds
    - Format: ReasonableUnixTimeMs

**MessageId**:
    - Description: MessageId
    - Format: UuidCanonicalTextual

.. autoclass:: gridworks.types.sim_timestep.check_is_reasonable_unix_time_s
    :members:


.. autoclass:: gridworks.types.sim_timestep.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gridworks.types.sim_timestep.check_is_left_right_dot
    :members:


.. autoclass:: gridworks.types.sim_timestep.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gridworks.types.SimTimestep_Maker
    :members:
