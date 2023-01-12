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

GridWorks uses distributed actors to balance the electric grid. What does this mean?
In today's world, more power comes from highly variable power sources such as wind and
solar. And yet, the number of electrons going into the grid must match the number coming
out. This is where GridWorks comes in. GridWorks technology enables electrical devices
with some embedded storage or with flexibility to provide grid balancing. Furthermore,
GridWorks allows these appliances to be more thrifty, using electricity when it is
cheap and green.

To learn how using and contributing to GridWorks can support a cost-effective and rapid transition to a sustainable future:

- Watch the beginning of the GridWorks story in [this 5 minute video](https://www.youtube.com/watch?v=5QFNQcp2Yzs)
- Try some [Hello World](https://gridworks.readthedocs.io/en/latest/hello-gridworks.html) examples
- Walk through this [10 MW simulation](https://gridworks.readthedocs.io/en/latest/story.html) of how GridWorks, if deployed in new heating systems, could cut home heating costs in half while reducing or eliminating the curtailing (i.e. turning off and wasting) of wind power
- Learn the ropes of [GridWorks Communications](https://gridworks.readthedocs.io/en/latest/api-sdk-abi.html)

## Algorand Blockchain Mechanics

Gridworks runs markets between distributed actors acting as avatars for physical devices on the grid. It needs a foundation of trustless, secure, scalabe validation and authentication. Out of the gate, you will need to understand how to work with the Algorand blockchain. If Algorand
development is new to you or you want a refresher, consider starting [here](https://gridworks.readthedocs.io/en/latest/blockchain.html).

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
