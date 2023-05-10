# GNodeRegistry

While there is a single [GNodeFactory](g-node-factory), GridWorks encourages the formation of
multiple GNodeRegistries. Upon creation by the GNodeFactory, each GNode is
assigned to a unique GNodeRegistry.

That GNodeRegistry is the authority for information about the GNode that is beyond the
concern of the GNodeFactory.

**GNodeRole Assignment**

If the GNodeFactory has assigned a [CoreGNodeRole](core-g-node-role) different
than the default `Other` to a GNode (such as [TerminalAsset](terminal-asset),
[AtomicTNode](atomic-t-node), etc) then the GNodeRegistry's [GNodeRole](g-node-role)
for the GNode must match that CoreGNodeRole. These are the Roles critical for
tracking the copper of the electric grid. However, the GNodeRegistry may assign
a GNodeRole of its choosing (such as [TimeCoordinator](time-coordinator)) to any
GNode whose CoreGNodeRole is `Other`.

**Device data**

AtomicTNode GNode actors need to maintain realistic models of their
Transactive Devices in order to do a good job of buying energy and meeting the Service Level
Agreement of their device. For example, if a
heating system adds additional storage capacity or has a significant change in its
heat distribution system, the AtomicTNode needs some way of tracking this. Certain
changes to the underlying Transactive Device will actually provoke the retirement
of that AtomicTNode/TerminalAsset pair (for example, if the heating system is replaced
by a heating system with 3 times the power capacity). Others will just require adjustments
to how the AtomicTNode operates.

The SCADA GNode actors have additional requirements, since they run on their associated physical
device. For example, a SCADA needs to know _how_ it is sensing power, and this depends
of course on its device (e.g. does it have an embedded power meter or is it connected to
an [eGauge meter](https://store.egauge.net/meters) using modbus over TCP with the eGauge protocol).

Organizing and maintaining this information is the job of the GNodeRegistry. There is
significant discretion in this organization process, and different GNodeRegistries may
choose how they do it. [GridWorks Energy Consulting](https://github.com/thegridelectric)
has designed one, focused initially on serving thermal storage space heat. A company designing
AtomicTNodes and/or SCADA systems for an entirely different class of Transactive Device may choose to
collaborate with GridWorks Energy Consulting to expand the scope of the GridWorks
GNodeRegistry, or design their own.

_Back to [Lexicon](lexicon)_
