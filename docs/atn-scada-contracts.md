# ATN-SCADA Contracts: Overview

The relationship between an Atomic Transactive Node (ATN) and a Supervisory Control and Data Acquisition (SCADA) system represents a critical partnership in delivering heat to building occupants while reducing heating costs (and providing grid balancing) through electricity market participation.

While these systems may be operated by different entities with distinct responsibilities, they must work in concert to maintain comfortable temperatures for building occupants.

The relationship is managed by a set of **contracts**. These contracts come in two categories.

**DispatchContracts** These are contracts that last the duration of an energy market period. For example, the initial Millinocket project has `SlowDispatchContracts` that specify using a certain amount of electrical energy within a time period, but do not have any particular power contraints.

**RepresentationContracts**  These are long-lasting contracts (multi-year) articulating the relationship between a homeowner and an aggregator. They signal the agreement by the owner of the TerminalAsset to:
- have their Scada **agree** to DispatchContracts provided by the Aggregator's ATN, and
- have the ATN enter into market positions on their behalf.

This contract is designed to be backed by an blockchain Non-Fungible Token that the owner of the heating system provides to an Aggregator.

## Distinct Responsibilities
The ATN and SCADA have separate but complementary roles:

**ATN**
 - Participates in electricity markets
 - Optimizes energy costs
 - Responsible for Service Level Agreement except in edge cases
 - Holds trading rights granted by owner of the heating system (`TaTradingRights`, the Algorand NFT)
 - Issues dispatch contracts to SCADA

**SCADA**
 - Controls physical heating equipment
 - Final backstop for homeowner safety and comfort 
 - Monitors system performance
 - Executes dispatch contracts from ATN


**Blockchain Umpire**

A blockchain-based umpire serves as the authoritative arbiter of contract states. The umpire does not actively control system operation, but rather serves as a trusted source of truth for Contract status (Created, Active, Completed, etc.) and other forms of performance verification. This will help provide a trusted foundation for dispute resolution and trading rights validation.

**Message Sequencing**

The ATN-SCADA communication protocol is designed to create an unforgeable record of all interactions through:

 1. Cross-linked message validation - each message must reference the specific digit from the counterparty's last message
 2. Cryptographic signatures - covering both the message content and the cross-linking information

This simple but powerful mechanism ensures that neither party can fabricate or modify the historical record, protecting both the service providers and the homeowners they serve.