# Contract State Management

## Overview

The GridWorks system manages constraints on the electric grid by using market mechanisms running at all potential constraints.

## Design Principles

### Layered Bid Approach
The system uses layered bids rather than position replacement for several key advantages:
- Resilient to message delivery issues and out-of-order arrival
- Maintains comprehensive audit trail of decisions and actions
- Natural alignment with blockchain smart contract patterns
- Supports partial fulfillment and modifications
- Scales to complex use cases like regulation services

### Contract State Model

```python
class MarketContract:
    """Represents an active Market Contract"""
    ContractId: UUID4Str  # Derived from original bid message id
    MarketSlotName: MarketSlotName
    StartUnixS: int
    DurationMinutes: int
    AvgPowerWatts: int
```

During the transition to a full database implementation, contract state is temporarily persisted to `.env` as JSON. This enables SCADAs to maintain contract state through reboots or communication interruptions.

## Contract Lifecycle

1. **Bid Submission**
   - ATN submits bid to MarketMaker
   - MarketMaker acknowledges receipt, establishing initial smart contract

2. **Contract Activation**
   - Market price publication makes contract binding
   - ATN sends EnergyInstruction to SCADA
   - SCADA persists contract state

3. **Execution & Monitoring**
   - Both parties monitor contract fulfillment
   - Contract completion/failure determined by metered data

## SCADA Startup Sequence

When initializing, a SCADA:
1. Reads any persisted contracts from storage
2. Evaluates which contracts are currently live
3. Establishes appropriate operational mode based on live contracts

## Future Enhancements

This architecture provides a foundation for:
- Migration to blockchain-based smart contracts
- Management of multiple thermal storage resources
- Integration of resistive elements
- Support for grid regulation services

The layered approach ensures reliable operation in the present while enabling smooth evolution toward these more sophisticated capabilities.
