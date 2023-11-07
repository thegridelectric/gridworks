# Code Generation

We use the [aicapture](https://github.com/effortlessapi/aicapture) open source command line package manager to translate information we store in [airtable](https://github.com/effortlessapi/aicapture) into automatically generated code.

Basic flow is:

- Add new data to the airtable tables for the
- run `aic -build` from `CodeHomeDir/CodeGenerationTools/`

##

TODO: Update with information about how to update table structure via the [effortless API](https://effortlessapi.com/auth/login)

The [ssot.me](https://explore.ssot.me/app/#!/publicTranspilers) site has documentation with a list of
transpilers available for the ssotme tool. For example, I added an odxml-to-entities transpiler by:

1. looking at the syntax on [that site](https://explore.ssot.me/app/#!/viewTranspiler/odxml42/ODXMLToEntitiesJson)
2. running the command `ssotme odxml-to-entities-json -i ODXML/DataSchema.odxml -o SSoT/Entities.json -install`
3. moving the additional block in aicapture.json to just above the `airtable-to-xml` transpiler (which requires Entities.json to be updated)

## More about types

When working with the GridWorks ecosystem, a "type" means a set of validations for a serialized message
getting passed between software agents/applications within the ecosystem. The authority for these validations is the Gridworks Type
registry (not yet built). Typically these messages are JSON but the registry does allow for different serializations.

Some of these validations are simple and syntactical in nature -
for example a JSON attribute "Description" may have type "string." Others capture embedded semantic meaning. This can involve axioms
that involve multiple attributes within the type. It also involves the use of GridWorks enums across multiple types whose meanings
are conveyed both in how they are used across multiple software actors and also in their corresponding documentation. One way
to think about this is that Domain Driven Design requires a mechanism for maintaining evolution and clarity about the _meaning_ of
messages, not just their syntax. The place where this starts is in a mechanism for managing enums.

The GridWorks registry manages authority for three types of objects, in increasing order of complexity:

- **PropertyFormats**
  Examples:

```
 LeftRightDot  (defn): Lowercase alphanumeric words separated by periods,
 most significant word (on the left) starting with an alphabet character.
```

```
GwVersion (defn): A three-character string, where each character is a numeric digit, and the first character must not be 0.
```

- **Enums**

  - Each enum is defined by a `LeftRightDot` formatted Name and a `GwVersion` formatted Version. The combination of these components is represented as VersionedName f"{name}.{version}".
  - Once an element belongs to an Enum version, it must belong to all future versions. For example if the enum `rochambeau.throw.000` includes "Rock" then
    "Rock" must belong to `rochambeau.throw.001` as well.
  - Each enum also has a default value. If an inbound message has an unrecognized
    enum value, the SDK will interpret that enum value as the default.
  - An Enum's elements are represented as 8-digit hex strings, known as `EnumSymbols`, when transmitted as serial messages. In addition, each `EnumSymbol` is associated with a `LocalValue`, which is a human-readable string. The purpose of `LocalValues` is to convey the meaning of the enum element and is intended to be interpreted by software agents utilizing native enums. For instance, "Rock" might serve as the `LocalValue`, while its corresponding `EnumSymbol` could be "1ea112b9". For a more comprehensive explanation, please refer to the documentation provided below [TODO: ADD LINK]

- **Types**
  - As with enums, each type is defined by a `LeftRightDot` formatted TypeName and a `GwVersion` formatted Version. The combination of these components is represented as VersionedName f"{TypeName}.{Version}".

This registry will eventually have an open-source tool command line tool (like ssotme itself)
which will take the place of the xslt tools in `CodeGenerationTools/GridworksCore that can be accessed by any repository using GridWorks Types in
order to build or start using the GridWorks types. But until that happens there is near-replication in the CodeGenerationTools/GridworksCore
folders.

All instances of GridWorks types must include a TypeName which is recognized by the GridWorks Type Registry. The format of the TypeName is LeftRightDot

Every type comes in versions. These versions are strings of three numerals and increment in numerical order. Starting with "000", then "001" etc.

If you ask query the Gridworks Type Registry for information about a TypeName, it will either tell you there is no such TypeName or it will return information about how to evaluate whether a serial message is an example of that type (message validation). . This is specifically intended for situations where bandwidth is limited and the messages have pretty minimal content.

The message validation includes:

1. attribute-specific validations
   1a. type (string, integer, boolean, float, another gridworks type)
   1b. format (various simple formats like left-right-dot format, or a GridWorks Enum)
   1c. additional simple pydantic checks (greater than 0)

2. more complex validations called axioms that are expected to be hand-coded. Some of these involve multiple attributes.

## New type built from airtable

## New type built from scratch

This is instructions for if you want to build a type with minimal interaction with the
code derivation machinery.

- In the airtable [TypeRoots](https://airtable.com/appgibWM6WZW20bBx/tblqEaRL8i0IiFfqF/viwra3fA7SUpxNhiz?blocks=hide) table:
  - Put TypeName in
    [ProtocolTypes](https://airtable.com/appgibWM6WZW20bBx/tblnyHLmbF5ihZoM1/viwyweGPAEhKuNpBB?blocks=hide)
-

## Why make the EnumSymbols unreadable?
