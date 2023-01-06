APIs,SDKs, and ABIs
=====================

The foundational GridWorks package `gridworks <https://pypi.org/project/gridworks/>`_, which is the source of this documentation,
is designed to help you set up a sample GridWorks API and its corresponding SDK in a
development environment, to help learn the ropes for core GridWorks communication mechanics.

Imagine a GridWorks application (say, a GNode actor) as a cell in a larger organism. It has ways of communicating,
and this is captured in its cell membrane.

- **APIs** The Application Programming Interface specifies how communication happens at and beyond its cell membranes.
- **SDKs** A GridWorks Software Development Kit, on the other hand, is like an internal organelle capable of generating valid messages to send out to other cells.
- **ABIs** The application might be an Algorand Smart Contract - for example, a [DispatchContract](dispatch-contract). Then it has an Algorand Application
  Binary Interface instead of an API.

**More on Algorand ABIs**

We describe the historical precedent for Application Binary Interfaces. Continuing the cell analogy, an ABI is a specification for
a cell communicating _inwardly_ to, say, its mitochondria. ABIs are familiar to c programmers as a way of arranging memory layout.

The Algorand blockchain is like a smallish, Turing-complete computer whose guts are spread out across the Internet, whose every
internal action in compiler code is visible for the world to see. A method call to an Algorand Smart Contract
is much more like a C ABI than a Restful API with a url endpoint.

For more information on Algorand ABIs:

- A `40 minute youtube <https://www.youtube.com/watch?v=mdM6KrGC61k>`_ discussing the launch
  of Algorand ABIs
- `ARC-4 <https://arc.algorand.foundation/ARCs/arc-0004>`_, the source of truth for implementation details
- `pyteal ABI support docs <https://pyteal.readthedocs.io/en/stable/abi.html>`_
- `AlgoBank ABI example <https://github.com/algorand/pyteal/tree/master/examples/application/abi>`_

GridWorks APIs
^^^^^^^^^^^^^^^

In order to explore how GridWorks APIs work, please start up a version of the ```gridworks``` package API:

```
uvicorn gridworks.rest_api:app --reload  --port 8000
```

navigate to

```
http://127.0.0.1:8001/docs#
```

You can then try out POSTS to various API endpoints. These endpoints will return a valid response if the
GridWorks type provided has no errors, and will otherwise return a list of one or more errors.

`GridWorks types <apis/types.html>`_ are the building blocks for GridWorks APIs: they articulate
*what* is getting sent without specifying *where and how* (i.e., a Post to a Restful API endpoint,
or a message published to an exchange on a rabbit broker).

As a first pass, you can make the slightly incorrect assumption that all Gridworks types must
be  serialized JSON - the lingua franca of APIs. Note that JSON  is NOT a programming language. It is a multi-dimensional
graph structure, and a greatest common denominator for articulating the WHAT
of data that programming languages use and manipulate in separate but interacting
applications. For example, a JSON "int"does not articulate anything about memory -
it is just an arbitrarily long sequence of `0123456789` characters.

The `Type SDK objects <sdk-types.html>`_ provide a Pythonic method of creating valid instances of these types, and for
interpretting payloads as natural Python objects.

**Examples of sending valid payloads to GridWorks APIS**

COMING SOON
