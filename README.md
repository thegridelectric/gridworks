# Gridworks

[![PyPI](https://img.shields.io/pypi/v/gridworks.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/gridworks.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/gridworks)][python version]
[![License](https://img.shields.io/pypi/l/gridworks)][license]

[![Read the documentation at https://gridworks.readthedocs.io/](https://img.shields.io/readthedocs/gridworks/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/thegridelectric/gridworks/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/thegridelectric/gridworks/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/gridworks/
[status]: https://pypi.org/project/gridworks/
[python version]: https://pypi.org/project/gridworks
[read the docs]: https://gridworks.readthedocs.io/
[tests]: https://github.com/thegridelectric/gridworks/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/thegridelectric/gridworks
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

GridWorks uses distributed actors to balance the electric grid. What does this mean?  In today's world, more
power comes from highly variable power sources such as wind and solar. And yet, the number
of electrons going into the grid must match the number coming out.  This is where GridWorks comes in.
GridWorks technology enables electrical devices with some embedded storage or with flexibility to provide grid
balancing. Furthermore, GridWorks allows these appliances to be more thrifty, using electricity when
it is cheap and green.

To learn how using and contributing to GridWorks can support a cost-effective and rapid transition to a sustainable future:

- Try some simple [Hello World](https://gridworks.readthedocs.io/en/latest/hello-gridworks.html) examples;
- Read the [Millinocket Story](https://gridworks.readthedocs.io/en/latest/millinocket-demo.html) to learn how to exploit the synergy between wind power and space heating;
- Go through the partner [Millinocket Tutorial](https://gridworks.readthedocs.io/en/latest/millinocket-tutorial.html).

## Blockchain Mechanics


Gridworks runs markets between distributed actors acting as avatars for physical devices on the grid. It needs a
foundation of trustless, secure, scalable validation and authentication. It heavily uses the Algorand blockchain. If
you want to undestand more about how and why this is, go [here](blockchain.html).

## GridWorks SDKs

 - **gridworks**: [package](https://pypi.org/project/gridworks/) provides basic shared mechanics for  communication and GNode structure. It is used as a package in all of our other repos.

 - **gridworks-atn**:  [package](https://pypi.org/project/gridworks-atn/) and associated [documentation](https://gridworks-atn.readthedocs.io/en/latest/) for the GridWorks Python [AtomicTNodes](https://gridworks.readthedocs.io/en/latest/atomic-t-node.html)  SDK. AtomicTNodes  are the GridWorks actors that make electrical devices *transactive*. This SDK is a great place to learn about blockchain mechanics, as it introduces some of the simpler structures (NFTs, stateless contracts, and then some simple stateful smart contracts constructed using  [beaker](https://github.com/algorand-devrel/beaker) ) required for establishing the link between physical reality on the electric grid and the actors that play their avatars in GridWorks.  

 - **gridworks-marketmaker**: [package](https://pypi.org/project/gridworks-marketmaker/) and associated [documentation](https://gridworks-marketmaker.readthedocs.io/en/latest/)  for our Python [MarketMaker](https://gridworks.readthedocs.io/en/latest/market-maker.html) SDK.  GridWorks uses distributed actors to balance the electric grid, and MarketMakers are the actors brokering this grid balancing via the markets they run for energy and balancing services.

There are several other open source GridWorks repos to explore on [our github page](https://github.com/thegridelectric),
including the code running on the [SCADA systems](https://github.com/thegridelectric/gw-scada-spaceheat-python)
that Efficiency Maine is deploying in Millinocket this winter.
The  [GNodeFactory](https://github.com/thegridelectric/g-node-factory) currently hosts the demo,
and  does most of the heavy lifting in terms of identity management and authentication in GridWorks. Finally, since the demo
is a distributed simulation, it needs a method of handling time. That's done by a [TimeCoordinator](https://github.com/thegridelectric/gridworks-timecoordinator) GNode.


## Usage

`pip install gridworks` to install the foundational package.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Gridworks_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/thegridelectric/gridworks/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/thegridelectric/gridworks/blob/main/LICENSE
[contributor guide]: https://github.com/thegridelectric/gridworks/blob/main/CONTRIBUTING.md
[command-line reference]: https://gridworks.readthedocs.io/en/latest/usage.html
