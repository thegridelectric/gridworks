# Application Shared Languages (ASL)

Application Shared Languages provide a framework for peer-to-peer communication between software entities, departing from traditional client-server API architectures. Instead of defining service contracts where one entity primarily issues commands to another, ASLs establish a shared vocabulary that enables rich bidirectional communication.

## Core Principles

### Words in the Shared Language

Every word in an ASL is expressed as either a Named Type or Named Enum with:
- **TypeName/EnumName**: A unique LeftRightDot identifier (e.g., `layout.lite`) where:
  - Words are lowercase alphanumeric, with the first leter of the first word being a letter
  - Words are separated by dots
- **Version**: Semantic version string (e.g., "000", "004")
- **Structure**: JSON-serializable format for types, value set for enums
- **Ownership**: Single maintainer responsible for versioning and updates

Note: The LeftRightDot format is also used for GNodeAliases in GridWorks, where dots do indicate parent-child relationships (e.g., `d1.iso.me.apple` is a child of `d1.iso.me`), but this hierarchical meaning does not apply to TypeNames.

Example of a Named Type in JSON format:
```json
{
    "FromGNodeAlias": "d1.isone.me.versant.keene.orange",
    "FromGNodeInstanceId": "ac07fd9c-c34b-4d69-8e5a-d5e13e9af320",
    "MessageCreatedMs": 1703862000000,
    "Strategy": "House0",
    "ZoneList": ["down", "up"],
    "TotalStoreTanks": 3,
    "ShNodes": [...],
    "DataChannels": [...],
    "SynthChannels": [...],
    "TankModuleComponents": [...],
    "FlowModuleComponents": [...],
    "Ha1Params": {
        "AlphaTimes10": 15,
        "BetaTimes100": 250,
        "GammaEx6": 1000000,
        "IntermediatePowerKw": 5.5,
        "IntermediateRswtF": 120,
        "DdPowerKw": 3.2,
        "DdRswtF": 110,
        "DdDeltaTF": 20,
        "MaxEwtF": 130
    },
    "I2cRelayComponent": {...},
    "TypeName": "layout.lite",
    "Version": "002"
}
```

Example of a Named Enum with versioned values:

```python
class TelemetryName(GwStrEnum):
    # Version 000
    Unknown = auto()
    PowerW = auto()
    RelayState = auto()
    WaterTempCTimes1000 = auto()
    WaterTempFTimes1000 = auto()
    GpmTimes100 = auto()

    # Version 001
    VoltageRmsMilliVolts = auto()
    CurrentRmsMicroAmps = auto()
    GallonsTimes100 = auto()
    MicroHz = auto()
    AirTempCTimes1000 = auto()
    AirTempFTimes1000 = auto()
    ThermostatState = auto()
    MicroVolts = auto()

    # Version 002
    VoltsTimesTen = auto()

    # Version 003
    WattHours = auto()

    # Version 004
    StorageLayer = auto()

    @classmethod
    def default(cls) -> "TelemetryName":
        return cls.Unknown

    @classmethod
    def enum_name(cls) -> str:
        return "spaceheat.telemetry.name"

    @classmethod
    def enum_version(cls) -> str:
        return "004"

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
```

### Shared Vocabulary vs Service Contract

Traditional APIs often create inherent asymmetry, where one entity (the server) defines most of the possible expressions while other entities (clients) are limited in how they can respond. ASLs instead establish a shared vocabulary where all participating entities have equal expressive capability through the shared language.

### Cross-Language Support

ASLs maintain language independence by:
- Defining types in terms of their JSON structure
- Using consistent PascalCase for type names in the shared definition
- Allowing implementation languages to use their native conventions
- Providing code generation tools for language-specific implementations
- Validating at the JSON level against shared schemas

### Design Philosophy

ASL development emphasizes:
1. **Clarity over Convenience**: Types should be explicit and self-documenting
2. **Bounded Creativity**: Well-defined structures that enable rather than restrict
3. **Organic Evolution**: Versioned changes that support natural growth
4. **Peer Communication**: Equal expressive capability for all participants

## Type Registry

The Type Registry maintains the canonical definitions of all Named Types in an ASL. For each type it records:
- The TypeName and current Version
- The owning entity responsible for updates
- The JSON schema defining its structure
- Version history and compatibility information

## Breaking Changes

When evolving an ASL:
1. Create new Named Types rather than modifying existing ones when adding significant new concepts
2. Use versioning to maintain compatibility with existing implementations
3. Provide migration paths when breaking changes are necessary
4. Consider the impact on all participating entities equally

## Best Practices

- Focus on expressing concepts clearly rather than optimizing for implementation
- Keep Named Types focused and self-contained
- Version thoughtfully to support gradual adoption
- Consider bidirectional commu

## Type Completeness

ASL types can be either "complete" or "extensible":


### Complete Types
- Fully specify all allowed attributes
- Attributes must be one of:
  - Singletons
  - Optional fields
  - Lists of complete types
  - Enums
  - Well-known JSON objects
- Reject any additional attributes not in specification
- Use when precise structure is required

### Extensible Types
- Specify required attributes but allow additional fields
- Support organic growth of the type
- Use when flexibility is more important than strict structure
- Common in types that may need to evolve frequently


## Enum Evolution

ASL enums follow specific rules to maintain compatibility:

1. **Default Values**: Every enum must define a default value that implementations use when encountering unknown values
2. **Value Permanence**: Once an enum value has been added to the ASL, it cannot be removed
3. **SDK Behavior**: All SDK implementations must handle unknown enum values by returning the defined default
4. **Versioning**: Adding new enum values does not require a version change as backward compatibility is maintained through default values

Example:
```python
class MainAutoState(GwStrEnum):
    HomeAlone = auto()  # Version 000, Default value
    Atn = auto()       # Version 000
    Dormant = auto()   # Version 000

    @classmethod
    def default(cls) -> "MainAutoState":
        return cls.HomeAlone

    @classmethod
    def enum_version(cls) -> str:
        return "000"
