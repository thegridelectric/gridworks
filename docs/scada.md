# SCADA

In the context of GridWorks, SCADA refers to:

1.  A device, and software, that monitors and controls a TerminalAsset
2.  A GNode representing the above.

SCADA is also a more generalized industry term for any device capable of supervisory control and data acquisition.

The functions of the SCADA are pretty straightforward and obvious, given the goals of transactive energy. A SCADA needs to:

1. Sense and report information relevant to the performance of the TerminalAsset, including but not limited to the power and energy metering;
2. Let its AtomicTNode call the shots on how the TerminalAsset uses (or provides) electrical power, whenever the two are communicating; and
3. Do a decent job of running the TerminalAsset on its own when it loses communications with its AtomicTNode.

Go [here](https://github.com/thegridelectric/gw-scada-spaceheat-python) to
examine an example of SCADA software for a thermal storage heating system.

_Back to [Lexicon](lexicon.md)_
