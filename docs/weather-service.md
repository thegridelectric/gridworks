# WeatherService (GNodeRole)

A **WeatherService** is an actor responsible for providing weather forecasts. These services are typically provided via RabbitMQ using a pubsub pattern. [AtomicTNodes](atomic-t-node)
with [TradingRights] for [TransactiveDevices](transactive-device) whose electricity use is weather dependant (like heating systems) will subscribe to weather services.

_Back to [Lexicon](lexicon.md)_
