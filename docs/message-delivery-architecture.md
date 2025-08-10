# Message Delivery Mechanisms: A Layer Above the ASL

GridWorks Application Shared Language (ASL) defines the vocabulary - the named types, enums, and formats that enable organizations to communicate. But vocabulary alone isn't enough; organizations, services and people need to be clear on how messages are delivered.

This document explains how GridWorks implements message delivery as a separate layer above ASL types, enabling the same vocabulary to work across different transport mechanisms.

## 1. ASL Types vs. Delivery Mechanisms

**ASL Types are transport-agnostic vocabulary:**

- `power.watts` - power measurement meant to be sent asynchronously and _without_ a timestamp
- `slow.dispatch.contract` - represents the specifications of an hourly dispatch contract between a Scada and its LeafTransactiveNode (ltn)
- `report` -  smallish (5 minute) batch of timestamped telemetry data

**Delivery Mechanisms add routing intelligence:**
- What actor/actors receive this message?
- Does the message need an acknowledgment, and if so how is that handled?
- What goes on the "outside of the envelope" (topic, routing key, URL)?

Within the GridWorks Message Delivery Mechanisms, a message may be
- Sent directly from one actor to another over a message broker (`JsonDirect`)
- Broadcast for all actors who signed up to listen (`JsonBroadcast`)
- Sent over a broker but wrapped with acknowledgment requirements (`ScadaWrapped`). This is specific for SCADA's, as they tend to be at locations where Internet can go down and key data may need to be resent.
- Posted to a REST API endpoint (`HTTP`)

### Example: `latest.price` posted by MarketMaker via FastAPI

```python
# MarketMaker providing price via an API
from fastapi import FastAPI
from named_types import LatestPrice

app = FastAPI()

@app.get("/api/hw1-keene/latest-price")
async def ... TODO FINISH
```

**Notice**: The `latest.price` ASL type is identical whether sent via RabbitMQ messages or HTTP API calls. Only the delivery envelope changes.

## 2. Message Categories

GridWorks uses four core message categories:

### JsonDirect
Point-to-point messages between specific actors. Used for commands, responses, and targeted data delivery.

**Use cases:**
- LeafTransactiveNode sends bid to MarketMaker
- MarketMaker sending acknowledgement of bid back to market participant
- Direct coordination between MarketMakers
- SCADA sends `power.watts` to LeafTransactiveNode (FUTURE)

### JsonBroadcast
One-to-many messages broadcast to multiple recipients on a shared "radio channel."

**Use cases:**
- Market price updates to all participants (general broadcast)
- Grid status announcements
- Weather forecasts to all interested actors
- Targeted broadcasts using radio channels (e.g., `rt60gate5` for specific market timing)

### ScadaWrapped
Messages using the `gw` wrapper pattern that includes both Header and Payload. Currently used by SCADA systems when acknowledgment tracking is required.

**Use cases:**
- Critical commands requiring delivery confirmation
- Messages needing correlation tracking
- Legacy integration during migration period

### Serial
Placeholder for future bandwidth-constrained scenarios where bit-level serialization optimization becomes necessary.

**Future use cases:**
- Wireless sensor networks with limited bandwidth
- High-frequency trading scenarios requiring minimal latency
- Edge computing with resource constraints

**Note**: Serial is not currently implemented but reserved for scenarios where JSON overhead becomes prohibitive.

## 3. GridWorks RabbitMQ Infrastructure

GridWorks RabbitMQ infrastructure uses a **two-exchange pattern** for each actor role:

### Exchange Topology

**Each actor role has two exchanges:**
- **Consume Exchange**: `{class}_tx` - where this role receives messages
- **Publish Exchange**: `{class}mic_tx` - where this role publishes messages

**Examples:**
- `LeafTransactiveNode` consumes from `ltn_tx`, publishes to `ltnmic_tx`
- MarketMaker consumes from `marketmaker_tx`, publishes to `marketmakermic_tx`

**Important Counterexample**

The [GridWorks SCADA systems](https://github.com/thegridelectric/gridworks-scada) use MQTT for edge simplicity while participating in the broader RabbitMQ ecosystem. MQTT's lightweight publish/subscribe model is ideal for SCADA deployments - it requires minimal configuration, has lower overhead than AMQP, and works well on resource-constrained edge devices like Raspberry Pi systems. RabbitMQ bridges this gap through its MQTT plugin, which accepts MQTT clients and maps their topic-based messages to the **amq.topic exchange**.

### Message Flow Pattern

```
Sender Class → {sender_class}mic_tx → (routing) → {receiver_class}_tx → Receiver Class
```

**Example**: The LeafTransactiveNode `hw1.keene.beech` sending a bid to its MarketMaker `hw1.keene`:
```
hw1.keene.beech → ltnmic_tx → (routing logic) → marketmaker_tx → hw1.keene
```

### Routing Logic

RabbitMQ bindings connect the exchanges based on routing key patterns. In this case, there is a binding that takes any message arriving at the `ltnmic_tx` exchange whose routing key matches the pattern

```
*.*.ltn.*.marketmaker.*
```
and passes it onto the `marketmaker_tx` exchange.

In addition, each actor will set up a queue on its receiver exchange that binds to any
message meant for it specifically. In this example, the MarketMaker `hw1.keene` will
set up a queue and create a binding that matches

```
*.*.*.*.*.hw1-keene
```



## 4. Routing Key Patterns

### JsonDirect (`rj`)

**Pattern:**
```
rj.{from-alias}.{from-class}.{type-name}.{to-class}.{to-alias}
```

**Example from ASL registry:**
```
rj.hw1-keene-beech-scada.scada.power-watts.ltn.hw1-keene-beech
```

**Breakdown:**
- `rj` = JsonDirect message category symbol
- `hw1-keene-beech-scada` = sender's GNode alias (dots → hyphens)
- `scada` = sender's role
- `power-watts` = ASL type name (dots → hyphens)
- `ltn` = receiver's role
- `hw1-keene-beech` = receiver's GNode alias

### JsonBroadcast (`rjb`)

**Pattern:**

```
rjb.{from-alias}.{from-class}.{type-name}
```
**or**
```
rjb.{from-alias}.{from-class}.{type-name}.{radio-channel}
```


(i.e., optional radio channel)

**Examples from ASL registry:**
```
rjb.hw1-keene.marketmaker.market-list
rjb.hw1-keene.marketmaker.latest-price.rt60gate5
```

**Breakdown:**
- `rjb` = JsonBroadcast message category symbol
- `hw1-keene` = sender's GNode alias
- `marketmaker` = sender's role
- `market-list` / `latest-price` = ASL type being broadcast
- No radio channel (general broadcast) / `rt60gate5` = specific radio channel for targeted scope

### ScadaWrapped (`gw`)

**Pattern:**
```
gw.{from-alias}.{from-role}.{type-name}.{to-role}.{to-alias}
```

**Example from ASL registry:**
```
gw.hw1-keene-beech-scada.to.ltn.power-watts
```

**Structure:**
Same as JsonDirect but uses `gw` symbol and includes wrapper envelope with Header/Payload structure.

**Structure:**
```json
{
  "Header": {
    "Src": "hw1-keene-beech-scada",
    "Dst": "ltn",
    "MessageType": "power.watts",
    "MessageId": "12345678-abcd-1234-abcd-123456789012",
    "AckRequired": false
  },
  "Payload": {
    "Watts": 6743,
    "TypeName": "power.watts",
    "Version": "000"
  },
  "TypeName": "gw"
}
```


## 5. Current SCADA Usage of ScadaWrapped

Right now SCADA uses ScadaWrapped for all of its messages. Plan to migrate to _only_ using ScadaWrapped for messages requiring delivery confirmation.


**Use JsonDirect/JsonBroadcast for:**
- Telemetry data that doesn't require acknowledgment
- High-frequency measurements where wrapper overhead matters
- New integrations that can use simpler patterns

## 6. Evolution Toward Simpler Patterns

### The Vision: Envelope-Based Routing

GridWorks is moving toward a simpler model where **the envelope tells you what you're looking at**:

**RabbitMQ routing key contains:**
- Message category (`rj`, `rjb`)
- Sender and receiver identification
- ASL type name

**MQTT topic contains:**
- Hierarchical addressing
- Message type identification
- Delivery semantics

**API endpoint contains:**
- Resource identification
- Operation semantics
- Type expectations

### Benefits of Simpler Patterns

**Reduced Complexity**: No need to unwrap messages to understand their purpose - the routing envelope contains the metadata.

**Better Performance**: Eliminate JSON parsing overhead for message routing decisions.

**Clearer Semantics**: Routing behavior is explicit in the delivery mechanism rather than hidden in message content.

**Transport Flexibility**: Same ASL types work across RabbitMQ, MQTT, HTTP APIs, and future transports.

### Migration Strategy

**Phase 1** (Current): Support both patterns
- SCADA continues using `ScadaWrapped` for all messages and expects the same from its `ltn`.
- New development uses `JsonDirect`/`JsonBroadcast` for all actor-to-actor comms except for SCADA <-> LeafTransactiveNode


**Phase 2** (Near-term): Minimize wrapper usage
- `Scada` and `LeafTransactiveNode` mostly use the JsonDirect pattern
- Clear documentation of when each pattern applies

**Phase 3** (Future): Transport evolution
- RabbitMQ → Kafka migration maintains ASL types
- API integration provides alternative delivery mechanisms
- Acknowledgment handled at transport level rather than application level

## 7. Choosing the Right Pattern

### Decision Matrix

**Use JsonDirect when:**
- Sending to a specific actor
- Point-to-point communication required
- No acknowledgment tracking needed

**Use JsonBroadcast when:**
- Multiple actors need the same information
- Pub/sub semantics appropriate
- Loose coupling desired between sender and receivers
- Can optionally use radio channels for targeted broadcasts

**Use ScadaWrapped when:**
- Acknowledgment tracking is critical
- Legacy integration requires wrapper format
- Message correlation needed across request/response cycles

**Use Serial when:**
- Bandwidth constraints are severe (future)
- Minimal latency required (future)
- Bit-level optimization necessary (future)

---

*This architecture enables GridWorks to maintain consistent ASL vocabulary while adapting delivery mechanisms to specific operational requirements, from real-time grid coordination to market participation and regulatory reporting.*
