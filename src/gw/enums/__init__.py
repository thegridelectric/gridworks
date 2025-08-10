"""
Enums from the GridWorks Application Shared Language (ASL)

The GridWorks ASL enables peer-to-peer shared vocabulary between energy system actors like 
SCADA devices, trading nodes, and market makers. Enums serve as the "controlled vocabulary" 
foundation that ensures everyone speaks the same language.

Key characteristics:
 - Immutable evolution: Enum values can be added but never changed or removed, ensuring 
   backwards compatibility across distributed systems
 - Transport-agnostic: Same enums work with RabbitMQ, HTTP APIs, Kafka, or any message delivery
 - Organizational autonomy: Each organization can build exactly the sophistication they need
   on top of shared foundations
 - Constitutional governance: Follow naming conventions (left.right.dot format) and 
   ownership rules defined in the ASL registryThan

Enums are the semantic building blocks that enable organizations to collaborate without 
compromising their independence. Unlike APIs where one party controls the vocabulary, 
ASL enums evolve through community governance while maintaining stability.

Application Shared Languages represent an evolution beyond traditional APIs - enabling 
true peer-to-peer collaboration where organizations maintain autonomy while sharing 
vocabulary, rather than client/server relationships where one party dictates the interface.

For more information:
 - [Why GridWorks ASL Exists](https://gridworks-asl.readthedocs.io/motivation/)
 - [ASL Rules and Guidelines](https://gridworks-asl.readthedocs.io/rules-and-guidelines/) 
 - [GridWorks ASL Overview](https://gridworks-asl.readthedocs.io/)

 """

from gw.enums.gw_str_enum import GwStrEnum
from gw.enums.market_price_unit import MarketPriceUnit
from gw.enums.market_quantity_unit import MarketQuantityUnit
from gw.enums.market_type_name import MarketTypeName
from gw.enums.message_category import MessageCategory
from gw.enums.message_category_symbol import MessageCategorySymbol
from gw.enums.recognized_currency_unit import RecognizedCurrencyUnit


__all__ = [
    "GwStrEnum",
    "MarketPriceUnit",
    "MarketQuantityUnit",
    "MarketTypeName",
    "MessageCategory",
    "MessageCategorySymbol",
    "RecognizedCurrencyUnit",
]
