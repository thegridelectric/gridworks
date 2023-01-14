DispatchContract
==================

The DispatchContract is an Algorand Smart Contract between the
`AtomicTNode <atomic-t-node.html>`_ and `Scada <scada.html>`_ GNode Actors serving the
same `Transactive Device <transactive-device.html>`_.

It:
  - Helps the SCADA initially determines *what* credentials an AtomicTNode must provide
  in messages in order for the SCADA to accept dispatch commands
  - Is the *eventual* source of authority on the state of its global True/False variable `AtnInCommand`
  - Is the primary source of audit data for power and energy injection/withdrawal by the TransactiveDevice.




*Back to `Lexicon <lexicon.html>`_*
