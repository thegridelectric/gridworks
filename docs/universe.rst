Universe
==========

This concept allows for for development and shared simulations. The hybrid universe allows for coupling real and simulated devices, which can support high-fidelity analysis of outcomes before larger rollouts.

It is an `enum <enums.html#gridworks.enums.UniverseType>`_ in the `gridworks SDK <https://pypi.org/project/gridworks/>`_.

Dev
^^^^^

**Simulation running on a single computer.**

- Used for learning and code development.
- Can run without Internet.
- Designed to be run by a single individual on their computer. If you
  are familiar with Algorand, this is like running in `sandbox dev` mode (and requires the `algo sandbox <https://github.com/algorand/sandbox>`_ under the hood).
- Time is not unique. That is, you can run the simulation again, using different parameters,
  and get different data for the same timestamp.
- No security.

Hybrid
^^^^^^^^

**Anything goes.**

- Designed for multiple people/organizations to interact in a non-production environment.
- Requires Internet.
- Financial transactions are simulated.
- Unique global Hybrid GNodeFactory.
- TerminalAssets can be avatars for either **real** or **simulated** Transactive Devices. Put another way, the validation process for TerminalAssets can be real or simulated.
- Multiple WorldInstances.
- Time is unique per WorldInstance.
  - In ex-poste analysis, data from different actors can be trusted to refer to the same events.
  - If all devices are simulated, then WorldInstance time can be decoupled from real time.
  - Evidently, if there are any real devices, WorldInstance time must track real time.
- Non-production code is allowed to run GNode Actors.
- There is some basic security.

Production
^^^^^^^^^^^

**Money at stake.**

- Unique global Production GNodeFactory
- Only one WorldInstance.
- Financial transactions are real.
- Time is real.
- Transactive Devices must be **real**. Put another way, the validation process for a TerminalAsset must be done by a real company that is staking its reputation on the validation.
- Only allows production code to run a GNode Actor.
- Production security.

Back to `Lexicon <lexicon.md>`_
