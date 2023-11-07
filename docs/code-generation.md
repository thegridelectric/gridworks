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

## How to create a new type

The types are managed by the Gridworks Type Registry through a standard Restful API (not built yet).
In addition, the xslt tools in `CodeGenerationTools/GridworksCore` will be made into an open source command line tool (like ssotme itself)
that can be accessed by any repository using GridWorks Types. But until that happens there is near-replication in the CodeGenerationTools/GridworksCore
folders.

All instances of GridWorks types must include a TypeName which is recognized by the GridWorks Type Registry.

Every type comes in versions. These versions are strings of three numerals and increment in numerical order. Starting with "000", then "001" etc.

If you ask query the Gridworks Type Registry for information about a TypeName, it will either tell you there is no such TypeName or it will return information about how to evaluate whether a serial message is an example of that type (message validation). Almost all messages are JSON but the registry allows for different serializations. This is specifically intended for situations where bandwidth is limited and the messages have pretty minimal content.

The message validation includes:

1.
