# PriceService (GNodeRole)

A **PriceService** is an actor responsible for providing price forecasts for the markets run by [MarketMakers](market-maker). These services are typically
provided via RabbitMQ using a pubsub pattern. [AtomicTNodes](atomic-t-node)
will subscribe to price services.

Given the importance of good forecasting for the financial performance of
AtomicTNodes, there is very likely a business opportunity in providing
high-quality, localized forecasting.

`Back to Lexicon <lexicon.html>`\_
