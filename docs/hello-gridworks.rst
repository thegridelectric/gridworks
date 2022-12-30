
Hello World
============


.. note::
    All GridWorks repos assume Python 3.10 or higher, docker, and the Algorand
    `sandbox <https://github.com/algorand/sandbox>`_. Also, For these ```hello world``` examples,
    please clone `this repo <https://github.com/thegridelectric>`_  in order to spin up
    a local rabbit broker.


GridWorks  is message-driven, following `the reactive manifesto <https://www.reactivemanifesto.org/>`_.
The basic building blocks are `GNodes <g-node.html>`_ ('G' stands for the electric grid). GNode
actors communicate via:

  1) Asynchronous message-passing on a RabbitMQ Broker;
  2) API calls via FastAPI interfaces; and
  3) Calls to the Algorand blockchain ledger, typically usually smart contract ABI method calls.


Hello Rabbit
^^^^^^^^^^^^

Here is a simple example of the first. Before running, start a development world rabbit broker. From
the top level of this repo:

   1) **./arm.sh**  (*if your computer has an arm chip*)
   2) **./x86.sh**   (*x86 chip*)

Wait for the `rabbit admin page <http://0.0.0.0:15672/>`_ to load (username/passwd smqPublic)


.. literalinclude:: ../examples/hello.py



Hello Algorand
^^^^^^^^^^^^

Hello FastAPI
^^^^^^^^^^^^
