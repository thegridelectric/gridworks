GNodeGt
==========================
Python pydantic class corresponding to  json type ```g.node.gt```.

.. autoclass:: gridworks.types.GNodeGt
    :members:

**GNodeId**:
    - Description: Immutable identifier for GNode
    - Format: UuidCanonicalTextual

**Alias**:
    - Description: Structured mutable identifier for GNode. The GNode Aliases are used for organizing how actors in Gridworks communicate. Together, they also encode the known topology of the electric grid.  `More info <https://gridworks.readthedocs.io/en/latest/g-node-alias.html>`_
    - Format: LeftRightDot

**Status**:
    - Description: Lifecycle indicator

**Role**:
    - Description: Role within Gridworks. `More info <https://gridworks.readthedocs.io/en/latest/g-node-role.html>`_

**GNodeRegistryAddr**:
    - Description: Algorand address for GNodeRegistry. For actors in a Gridworks world, the GNodeRegistry is the Single Source of Truth for existence and updates to GNodes. `More info <https://gridworks.readthedocs.io/en/latest/g-node-registry.html>`_
    - Format: AlgoAddressStringFormat

**PrevAlias**:
    - Description: Previous GNodeAlias. As the topology of the grid updates, GNodeAliases will change to reflect that. This may happen a handful of times over the life of a GNode.
    - Format: LeftRightDot

**GpsPointId**:
    - Description: Lat/lon of GNode. Some GNodes, in particular those acting as avatars for physical devices that are part of or are attached to the electric grid, have physical locations. These locations are used to help validate the grid topology.
    - Format: UuidCanonicalTextual

**ComponentId**:
    - Description: Component Id. Used if a GNode is an avatar for a physical device. The serial number of a device is different from its make/model. The ComponentId captures the specific instance of the device.
    - Format: UuidCanonicalTextual

**DisplayName**:
    - Description: Display Name

**OwnershipDeedNftId**:
    - Description: Algorand Id of ASA Deed. Part of establishing the link of trust between GNodes that are avatars and their physical devices. For example, TerminalAssets have TaDeeds. These deeds can come in two flavors: Algorand Standard Assets (ASA), or Algorand Smart Signatures. The ASA is easier to understand but has limitations.   `More info <https://gridworks.readthedocs.io/en/latest/ta-deed.html>`_

**OwnerAddr**:
    - Description: Algorand address of the deed owner
    - Format: AlgoAddressStringFormat

**OwnershipDeedValidatorAddr**:
    - Description: Algorand address of Validator. Deeds are issued by the GNodeFactory, in partnership with third party Validators.  `More info <https://gridworks.readthedocs.io/en/latest/ta-validator.html>`_
    - Format: AlgoAddressStringFormat

**DaemonAddr**:
    - Description: Algorand address of the daemon app. Some GNodes have Daemon applications associated to them to handle blockchain operations.
    - Format: AlgoAddressStringFormat

**TradingRightsNftId**:
    - Description: Algorand Id of ASA TradingRights

.. autoclass:: gridworks.types.g_node_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gridworks.types.g_node_gt.check_is_left_right_dot
    :members:


.. autoclass:: gridworks.types.g_node_gt.check_is_algo_address_string_format
    :members:


.. autoclass:: gridworks.types.GNodeGt_Maker
    :members:
