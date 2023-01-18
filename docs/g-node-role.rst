GNodeRole
----------

The GNodeRole is an `enum <enums.html#gridworks.enums.GNodeRole>`_ categorizing `GNodes <g-node.html>`_ by
function. The Role will determine, for example, whether the GNode has a code actor representing it
(for example, an AtomicTNode) or whether it is a passive object that is discussed by actors (typically,
the GNodes that represent copper on the Grid or physical devices attached to the grid).  If the GNode has
an actor, its GNodeRole will also typically determine a set of basic messages sent and received by the
GNode. A GNode's role  is determined by the `GNodeFactory <g-node-factory.html>`_ if it represents copper on the grid
(or if it is the World GNode), and otherwise is determined by the GNode's `GNodeRegistry <g-node-registry.html>`_.



    - **GNode** This is a default role when more information is not available
    - `TerminalAsset <terminal-asset.html>`_  **CoreGNodeRole**
    - `AtomicTNode <atomic-t-node.html>`_ **CoreGNodeRole**
    - `MarketMaker <market-maker.html>`_ **CoreGNodeRole**
    - `AtomicMeteringNode <atomic-metering-node.html>`_ **CoreGNodeRole**
    - `ConductorTopologyNode <conductor-topology-node.html>`_ **CoreGNodeRole**
    - `InterconnectionComponent <interconnection-component.html>`_ **CoreGNodeRole**
    - `World <world-role.html>`_
    - `TimeCoordinator <time-coordinator.html>`_
    - `Supervisor <supervisor.html>`_
    - `Scada <scada.html>`_
    - `PriceService <price-service.html>`_
    - `WeatherService <weather-service.html>`_
    - `AggregatedTNode <aggregated-t-node.html>`_


`Back to Lexicon <lexicon.html>`_
