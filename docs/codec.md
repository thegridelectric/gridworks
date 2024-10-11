# GridWorks serializing/deserializing

Strings of bytes passed via RabbitMQ or MQTT are what we mean by _serialized_. Instances of Pydantic classes are the fully _deserialized_ objects.

A main point of the Type Registry is that the outermost identifier of a message - its name for example if its in a file, or its topic if its an mqtt/rabbit message, or the API url if its a post - includes a **TypeName** that uniquely specifies both how to serialize/deserialize, and also how to check that the object is a valid instance of the Type. 

As an example, consider the SuperStarter type. An instance of the type is the following bytestring:

msg = b'{"SupervisorContainer": {"SupervisorContainerId": "995b0334-9940-424f-8fb1-4745e52ba295", "WorldInstanceName": "d1__1", "SupervisorGNodeInstanceId": "20e7edec-05e5-4152-bfec-ec21ddd2e3dd", "SupervisorGNodeAlias": "d1.isone.ver.keene.super1", "TypeName": "supervisor.container.gt", "Version": "000", "StatusGtEnumSymbol": "f48cff43"}, "GniList": [], "AliasWithKeyList": [], "KeyList": [], "TypeName": "super.starter", "Version": "000"}'


s = SuperStarter_Maker.type_to_tuple(msg) 

s is an instance of SuperStarter.


s.as_type()
This method calls the as_dict() method, which differs from the native python dict() in the following key ways:
- Enum Values: Translates between the values used locally by the actor to the symbol
sent in messages.
- Removes any key-value pairs where the value is None for a clearer message, especially in cases with many optional attributes.

It also applies these changes recursively to sub-types.


Its near-inverse is SuperStarter_Maker.type_to_tuple(). If the type (or any sub-types) includes an enum, then the type_to_tuple will map an unrecognized symbol to the default enum value. This is why these two methods are only 'near' inverses.


Serialize to the base.g.node.gt.002 representation.

        Recursively encodes enums as intentionally hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.

        Instances in the class are python-native representations of base.g.node.gt.002
        objects, while the actual base.g.node.gt.002 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is BaseGNodeGt_Maker.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.