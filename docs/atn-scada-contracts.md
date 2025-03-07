# ATN-SCADA Contracts: Overview

The relationship between an Atomic Transactive Node (ATN) and a Supervisory Control and Data Acquisition (SCADA) system represents a critical partnership in delivering heat to building occupants while supporting a balanced electric griid.

While these systems may be operated by different entities with distinct responsibilities, they must work in concert to:

 1. Maintain comfortable temperatures for building occupants
 2. Optimize electricity costs through market participation
 3. Ensure reliable system operation
 4. Provide transparent accountability

The relationship is managed by a set of **contracts**. These contracts come in two categories
  1) **DispatchContracts** These are contracts that last the duration of an energy market period. For example, the initial Millinocket project has `SlowDispatchContracts` that specify using a certain amount of electrical energy within a time period, but do not have any particular power contraints.
  2) **RepresentationContracts**  These are long-lasting contracts (multi-year) that reflect the relationship between a homeowner and an aggregator. They signal the long-standing agreement by the owner of the TerminalAsset to 
    - have their Scada **agree** to DispatchContracts provided by the Aggregator's AtomicTNode
    - have the Atn enter into market positions on their behalf
  This contract is designed to be backed by an Algorand blockchain `TaTradingDeed` - a 
  non fungible token that the owner of the heating system provides to an Aggregator.

## Distinct Responsibilities
The ATN and SCADA have separate but complementary roles:

**ATN**
 - Participates in electricity markets
 - Optimizes energy costs
 - Responsible for Service Level Agreement except in edge cases
 - Holds trading rights granted by homeowner
 - Issues dispatch contracts to SCADA

**SCADA**
 - Controls physical heating equipment
 - Final backstop for homeowner safety and comfort 
 - Monitors system performance
 - Executes dispatch contracts from ATN


**Blockchain Umpire**

To ensure fair and transparent operation, a blockchain-based umpire serves as the authoritative arbiter of contract states. The umpire does not actively control system operation, but rather serves as a trusted source of truth for Contract status (Created, Active, Completed, etc.) and other forms of performance verification. This will help provide a trusted foundation for dispute resolution and trading rights validation.

**Message Sequencing**

The ATN-SCADA communication protocol is designed to create an unforgeable record of all interactions through:

 1. Cross-linked message validation - each message must reference the specific digit from the counterparty's last message
 2. Cryptographic signatures - covering both the message content and the cross-linking information

This simple but powerful mechanism ensures that neither party can fabricate or modify the historical record, protecting both the service providers and the homeowners they serve.