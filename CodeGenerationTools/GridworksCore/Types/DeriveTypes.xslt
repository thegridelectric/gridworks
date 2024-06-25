<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl" xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xsl:output method="xml" indent="yes" />
    <xsl:param name="root" />
    <xsl:param name="codee-root" />
    <xsl:include href="../CommonXsltTemplates.xslt"/>
    <xsl:param name="exclude-collections" select="'false'" />
    <xsl:param name="relationship-suffix" select="''" />
    <xsl:variable name="airtable" select="/" />
    <xsl:variable name="squot">'</xsl:variable>
    <xsl:variable name="init-space">             </xsl:variable>
    <xsl:include href="GnfCommon.xslt"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/">
        <FileSet>
            <FileSetFiles>
                <xsl:for-each select="$airtable//ProtocolTypes/ProtocolType[(normalize-space(ProtocolName) ='gridworks')]">
                <xsl:variable name="versioned-type-id" select="VersionedType"/>
                <xsl:for-each select="$airtable//VersionedTypes/VersionedType[(VersionedTypeId = $versioned-type-id)  and (Status = 'Active' or Status = 'Pending') and (ProtocolCategory= 'Json' or ProtocolCategory = 'GwAlgoSerial')]">
                <xsl:variable name="local-name" select="TypeName" />
                    <xsl:variable name="class-name">
                        <xsl:call-template name="nt-case">
                            <xsl:with-param name="type-name-text" select="$local-name" />
                        </xsl:call-template>
                    </xsl:variable>
                    <xsl:variable name="python-data-class">
                        <xsl:call-template name="python-case">
                            <xsl:with-param name="camel-case-text" select="translate(DataClass,'.','_')"  />
                        </xsl:call-template>
                    </xsl:variable>
                    <xsl:variable name="overwrite-mode">

                    <xsl:if test="not (Status = 'Pending')">
                    <xsl:text>Never</xsl:text>
                    </xsl:if>
                    <xsl:if test="(Status = 'Pending')">
                    <xsl:text>Always</xsl:text>
                    </xsl:if>
                    </xsl:variable>

                    <xsl:variable name="data-class-id">
                        <xsl:call-template name="python-case">
                            <xsl:with-param name="camel-case-text" select="translate(DataClassIdField,'.','_')"  />
                        </xsl:call-template>
                    </xsl:variable>
                    <FileSetFile>
                                <xsl:element name="RelativePath"><xsl:text>../../../src/gridworks/types/</xsl:text>
                                <xsl:value-of select="translate($local-name,'.','_')"/><xsl:text>.py</xsl:text></xsl:element>

                        <OverwriteMode><xsl:value-of select="$overwrite-mode"/></OverwriteMode>
                        <xsl:element name="FileContents">


<xsl:text>"""Type </xsl:text><xsl:value-of select="TypeName"/><xsl:text>, version </xsl:text>
<xsl:value-of select="Version"/><xsl:text>"""
import json
from typing import Any
from typing import Dict</xsl:text>
<xsl:if test="count($airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id) and ((IsEnum = 'true') or (IsList = 'true'))])>0">
<xsl:text>
from typing import List</xsl:text>
</xsl:if>
<xsl:text>
from typing import Literal</xsl:text>

<xsl:if test="count($airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id) and not (IsRequired = 'true')]) > 0">
<xsl:text>
from typing import Optional</xsl:text>
</xsl:if>
<xsl:text>
from pydantic import BaseModel
from pydantic import Field</xsl:text>
<xsl:if test="count($airtable//TypeAttributes/TypeAttribute[VersionedType = $versioned-type-id and (IsOptional='true') or (IsEnum='true' or (IsList='true' and (IsType = 'true' or (IsPrimitive='true'  and normalize-space(PrimitiveFormat) != '') )))]) > 0">
<xsl:text>
from pydantic import validator</xsl:text>
</xsl:if>
<xsl:if test="count($airtable//TypeAxioms/TypeAxiom[MultiPropertyAxiom=$versioned-type-id]) > 0">
<xsl:text>
from pydantic import root_validator</xsl:text>
</xsl:if>


<xsl:if test="count($airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id) and (IsEnum = 'true')]) > 0">
<xsl:text>
from gridworks.message import as_enum
from enum import auto
from gridworks.enums import GwStrEnum</xsl:text>
</xsl:if>


<xsl:if test="MakeDataClass='true'">
<xsl:if test="not(IsComponent = 'true') and not(IsCac = 'true')">
<xsl:text>
from gridworks.data_classes.</xsl:text>
<xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="translate(DataClass,'.','_')"  />
</xsl:call-template>
<xsl:text> import </xsl:text><xsl:value-of select="DataClass"/>

</xsl:if>
</xsl:if>


<xsl:text>
from gridworks.errors import SchemaError</xsl:text>

<xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">


<xsl:if test="(IsType = 'true')">
<xsl:text>
from gridworks.types.</xsl:text>
<xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="translate(SubTypeName,'.','_')"  />
</xsl:call-template>
<xsl:text> import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="type-name-text" select="SubTypeName" />
</xsl:call-template>
<xsl:text>
from gridworks.types.</xsl:text>
<xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="translate(SubTypeName,'.','_')"  />
</xsl:call-template>
<xsl:text> import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="type-name-text" select="SubTypeName" />
</xsl:call-template><xsl:text>_Maker</xsl:text>
</xsl:if>
</xsl:for-each>
<xsl:for-each select="$airtable//GtEnums/GtEnum[(normalize-space(Name) !='')  and (count(TypesThatUse[text()=$versioned-type-id])>0)]">
<xsl:text>
from gridworks.enums import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="type-name-text" select="LocalName" />
</xsl:call-template>
<xsl:if test="(normalize-space(EnumAbbreviation) !='')">
<xsl:text> as </xsl:text>
<xsl:value-of select="EnumAbbreviation"/>
</xsl:if>
</xsl:for-each>

<xsl:for-each select="$airtable//GtEnums/GtEnum[(normalize-space(Name) !='')  and (count(TypesThatUse[text()=$versioned-type-id])>0)]">
<xsl:variable name="enum-name-style" select="PythonEnumNameStyle" />
<xsl:variable name="enum-name">
    <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="Name" />
    </xsl:call-template>
</xsl:variable>
<xsl:variable name="enum-local-name">
    <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="LocalName" />
    </xsl:call-template>
</xsl:variable>
<xsl:variable name="enum-id" select="GtEnumId"/>



<xsl:text>


class </xsl:text><xsl:value-of select="$enum-name"/><xsl:text>SchemaEnum:
    enum_name: str = "</xsl:text>
    <xsl:value-of select="Name"/>
    <xsl:text>"
    symbols: List[str] = [
        </xsl:text>
    <xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id)]">
    <xsl:sort select="Idx" data-type="number"/>
    <xsl:text>"</xsl:text><xsl:value-of select="Symbol"/><xsl:text>",
        </xsl:text>
</xsl:for-each>
<xsl:text>
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class </xsl:text><xsl:value-of select="$enum-name"/>
<xsl:text>(GwStrEnum):
    </xsl:text>

<xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id)]">
<xsl:sort select="Idx" data-type="number"/>
<xsl:if test="$enum-name-style = 'Upper'">
    <xsl:value-of select="translate(translate(LocalValue,'-',''),$lcletters, $ucletters)"/>
</xsl:if>
<xsl:if test="$enum-name-style ='UpperPython'">
    <xsl:value-of select="LocalValue"/>
</xsl:if>

<xsl:text> = auto()
    </xsl:text>
</xsl:for-each>
    <xsl:text>
    @classmethod
    def default(cls) -> "</xsl:text>
    <xsl:value-of select="$enum-name"/>
    <xsl:text>":
        return cls.</xsl:text>
    <xsl:if test="$enum-name-style = 'Upper'">
        <xsl:value-of select="translate(translate(DefaultEnumValue,'-',''),$lcletters, $ucletters)"/>
    </xsl:if>
    <xsl:if test="$enum-name-style ='UpperPython'">
        <xsl:value-of select="DefaultEnumValue"/>
    </xsl:if>
    <xsl:text>

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class </xsl:text><xsl:value-of select="$enum-local-name"/><xsl:text>Map:
    @classmethod
    def type_to_local(cls, symbol: str) -> </xsl:text>
    <xsl:value-of select="$enum-local-name"/>
    <xsl:text>:
        if not </xsl:text><xsl:value-of select="$enum-name"/><xsl:text>SchemaEnum.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to </xsl:text><xsl:value-of select="$enum-name"/>
                <xsl:text> symbols"
            )
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, </xsl:text>
        <xsl:value-of select="$enum-local-name"/><xsl:text>, </xsl:text>
        <xsl:value-of select="$enum-local-name"/><xsl:text>.default())

    @classmethod
    def local_to_type(cls, </xsl:text>
            <xsl:value-of select="translate(LocalName,'.','_')"/><xsl:text>: </xsl:text>
            <xsl:value-of select="$enum-local-name"/>
            <xsl:text>) -> str:
        if not isinstance(</xsl:text>
        <xsl:value-of select="translate(LocalName,'.','_')"/><xsl:text>, </xsl:text>
        <xsl:value-of select="$enum-local-name"/><xsl:text>):
            raise SchemaError(f"{</xsl:text>
                <xsl:value-of select="translate(LocalName,'.','_')"/><xsl:text>} must be of type {</xsl:text>
                    <xsl:value-of select="$enum-local-name"/><xsl:text>}")
        versioned_enum = as_enum(</xsl:text>
        <xsl:value-of select="translate(LocalName,'.','_')"/>
        <xsl:text>, </xsl:text>
        <xsl:value-of select="$enum-name"/><xsl:text>, </xsl:text>
        <xsl:value-of select="$enum-name"/><xsl:text>.default())
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, </xsl:text><xsl:value-of select="$enum-name"/><xsl:text>] = {</xsl:text>
    <xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id)]">
    <xsl:sort select="Idx" data-type="number"/>
        <xsl:text>
        "</xsl:text><xsl:value-of select="Symbol"/><xsl:text>": </xsl:text>
        <xsl:value-of select="$enum-name"/><xsl:text>.</xsl:text>
        <xsl:if test="$enum-name-style = 'Upper'">
            <xsl:value-of select="translate(translate(LocalValue,'-',''),$lcletters, $ucletters)"/>
        </xsl:if>
        <xsl:if test="$enum-name-style ='UpperPython'">
            <xsl:value-of select="LocalValue"/>
        </xsl:if>
    <xsl:text>,</xsl:text>
    </xsl:for-each>
    <xsl:text>
    }

    versioned_enum_to_type_dict: Dict[</xsl:text><xsl:value-of select="$enum-name"/><xsl:text>, str] = {
        </xsl:text>
    <xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id)]">
    <xsl:sort select="Idx" data-type="number"/>
    <xsl:value-of select="$enum-name"/><xsl:text>.</xsl:text>
    <xsl:if test="$enum-name-style = 'Upper'">
        <xsl:value-of select="translate(translate(LocalValue,'-',''),$lcletters, $ucletters)"/>
    </xsl:if>
    <xsl:if test="$enum-name-style ='UpperPython'">
        <xsl:value-of select="LocalValue"/>
    </xsl:if>
    <xsl:text>: "</xsl:text>
    <xsl:value-of select="Symbol"/><xsl:text>",
        </xsl:text>
    </xsl:for-each>
    <xsl:text>
    }</xsl:text>


</xsl:for-each>

<xsl:if test="count(PropertyFormatsUsed)>0">
<xsl:for-each select="$airtable//PropertyFormats/PropertyFormat[(normalize-space(Name) !='')  and (count(TypesThatUse[text()=$versioned-type-id])>0)]">

    <xsl:if test="Name='IsoFormat'">
    <xsl:text>


def check_is_iso_format(v: str) -> None:
    import datetime

    try:
        datetime.datetime.fromisoformat(v.replace("Z", "+00:00"))
    except:
        raise ValueError(f"{v} is not IsoFormat")</xsl:text>
    </xsl:if>

    <xsl:if test="Name='MarketSlotNameLrdFormat'">
    <xsl:text>


def check_is_market_type_name_lrd_format(v: str) -> None:
    from gridworks.enums import MarketTypeName
    try:
        x = v.split(".")
    except AttributeError:
        raise ValueError(f"{v} failed to split on '.'")
    if not x[0] in MarketTypeName.values():
        raise ValueError(f"{v} not recognized MarketType")
    g_node_alias = ".".join(x[1:])
    check_is_left_right_dot(g_node_alias)


def check_is_market_slot_name_lrd_format(v: str) -> None:
    """
    MaketSlotNameLrdFormat: the format of a MarketSlotName.
      - The first word must be a MarketTypeName
      - The last word (unix time of market slot start) must
      be a 10-digit integer divisible by 300 (i.e. all MarketSlots
      start at the top of 5 minutes)
      - More strictly, the last word must be the start of a
      MarketSlot for that MarketType (i.e. divisible by 3600
      for hourly markets)
      - The middle words have LeftRightDot format (GNodeAlias
      of the MarketMaker)
    Example: rt60gate5.d1.isone.ver.keene.1673539200

    """
    from gridworks.data_classes.market_type import MarketType
    try:
        x = v.split(".")
    except AttributeError:
        raise ValueError(f"{v} failed to split on '.'")
    slot_start = x[-1]
    if len(slot_start) != 10:
        raise ValueError(f"slot start {slot_start} not of length 10")
    try:
        slot_start = int(slot_start)
    except ValueError:
        raise ValueError(f"slot start {slot_start} not an int")
    if slot_start % 300 != 0:
        raise ValueError(f"slot start {slot_start} not a multiple of 300")

    market_type_name_lrd = ".".join(x[:-1])
    try:
        check_is_market_type_name_lrd_format(market_type_name_lrd)
    except ValueError as e:
        raise ValueError(f"e")

    market_type = MarketType.by_id[market_type_name_lrd.split(".")[0]]
    if not slot_start % (market_type.duration_minutes * 60) == 0:
        raise ValueError(
            f"market_slot_start_s mod {(market_type.duration_minutes * 60)} must be 0"
        )</xsl:text>
    </xsl:if>


    <xsl:if test="Name='AlgoAddressStringFormat'">
    <xsl:text>


def check_is_algo_address_string_format(v: str) -> None:
    """
    AlgoAddressStringFormat format: The public key of a private/public Ed25519
    key pair, transformed into an  Algorand address, by adding a 4-byte checksum
    to the end of the public key and then encoding in base32.

    Raises:
        ValueError: if not AlgoAddressStringFormat format
    """
    import algosdk
    at = algosdk.abi.AddressType()
    try:
        result = at.decode(at.encode(v))
    except Exception as e:
        raise ValueError(f"Not AlgoAddressStringFormat: {e}")</xsl:text>
    </xsl:if>


    <xsl:if test="Name='AlgoMsgPackEncoded'">
    <xsl:text>


def check_is_algo_msg_pack_encoded(v: str) -> None:
    """
    AlgoMSgPackEncoded format: the format of an  transaction sent to
    the Algorand blockchain.

    Raises:
        ValueError: if not AlgoMSgPackEncoded  format
    """
    import algosdk
    try:
        algosdk.encoding.future_msgpack_decode(v)
    except Exception as e:
        raise ValueError(f"Not AlgoMsgPackEncoded format: {e}")</xsl:text>
    </xsl:if>


    <xsl:if test="Name='HexChar'">
    <xsl:text>


def check_is_hex_char(v: str) -> None:
    """
    HexChar format: single-char string in '0123456789abcdefABCDEF'

    Raises:
        ValueError: if not HexChar format
    """
    if not isinstance(v, str):
        raise ValueError(f"{v} must be a hex char, but not even a string")
    if len(v) > 1:
        raise ValueError(f"{v} must be a hex char, but not of len 1")
    if v not in "0123456789abcdefABCDEF":
        raise ValueError(f"{v} must be one of '0123456789abcdefABCDEF'")</xsl:text>
    </xsl:if>


    <xsl:if test="Name='LeftRightDot'">
    <xsl:text>


def check_is_left_right_dot(v: str) -> None:
    """
    LeftRightDot format: Lowercase alphanumeric words separated by periods,
    most significant word (on the left) starting with an alphabet character.

    Raises:
        ValueError: if not LeftRightDot format
    """
    from typing import List

    try:
        x: List[str] = v.split(".")
    except:
        raise ValueError(f"Failed to seperate {v} into words with split'.'")
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(f"Most significant word of {v} must start with alphabet char.")
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of {v} split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of {v} must be lowercase.")</xsl:text>

    </xsl:if>

    <xsl:if test="Name='ReasonableUnixTimeS'">
    <xsl:text>


def check_is_reasonable_unix_time_s(v: int) -> None:
    """
    ReasonableUnixTimeS format: time in unix seconds between Jan 1 2000 and Jan 1 3000

    Raises:
        ValueError: if not ReasonableUnixTimeS format
    """
    from datetime import datetime, timezone
    start_date = datetime(2000, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(3000, 1, 1, tzinfo=timezone.utc)

    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    if v &lt; start_timestamp:
        raise ValueError(f"{v} must be after Jan 1 2000")
    if v > end_timestamp:
        raise ValueError(f"{v} must be before Jan 1 3000")</xsl:text>

    </xsl:if>

    <xsl:if test="Name='ReasonableUnixTimeMs'">
    <xsl:text>


def check_is_reasonable_unix_time_ms(v: str) -> None:
    """
    ReasonableUnixTimeMs format: time in unix milliseconds between Jan 1 2000 and Jan 1 3000

    Raises:
        ValueError: if not ReasonableUnixTimeMs format
    """
    from datetime import datetime, timezone
    start_date = datetime(2000, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(3000, 1, 1, tzinfo=timezone.utc)

    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    if v &lt; start_timestamp * 1000:
        raise ValueError(f"{v} must be after Jan 1 2000")
    if v > end_timestamp * 1000:
        raise ValueError(f"{v} must be before Jan 1 3000")</xsl:text>


    </xsl:if>

    <xsl:if test="Name='UuidCanonicalTextual'">
    <xsl:text>


def check_is_uuid_canonical_textual(v: str) -> None:
    """
    UuidCanonicalTextual format:  A string of hex words separated by hyphens
    of length 8-4-4-4-12.

    Raises:
        ValueError: if not UuidCanonicalTextual format
    """
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}")
    if len(x) != 5:
        raise ValueError(f"{v} split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            raise ValueError(f"Words of {v} are not all hex")
    if len(x[0]) != 8:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[1]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[2]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[3]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[4]) != 12:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")</xsl:text>


    </xsl:if>

    <xsl:if test="Name='WorldInstanceNameFormat'">
    <xsl:text>


def check_is_world_instance_name_format(v: str) -> None:
    """
    WorldInstanceName format: A single alphanumerical word starting
    with an alphabet char (the root GNodeAlias) and an integer,
    seperated by '__'. For example 'd1__1'

    Raises:
        ValueError: if not WorldInstanceNameFormat format
    """
    try:
        words = v.split("__")
    except:
        raise ValueError(f"{v} is not split by '__'")
    if len(words) != 2:
        raise ValueError(f"{v} not 2 words separated by '__'")
    try:
        int(words[1])
    except:
        raise ValueError(f"{v} second word not an int")

    root_g_node_alias = words[0]
    first_char = root_g_node_alias[0]
    if not first_char.isalpha():
        raise ValueError(f"{v} first word must be alph char")
    if not root_g_node_alias.isalnum():
        raise ValueError(f"{v} first word must be alphanumeric")</xsl:text>
    </xsl:if>


</xsl:for-each>
</xsl:if>
<xsl:text>


class </xsl:text>
<xsl:value-of select="$class-name"/>
<xsl:text>(BaseModel):
    """</xsl:text>
    <xsl:value-of select="Title"/>
    <xsl:if test="(normalize-space(Description) != '')">
    <xsl:text>.

    </xsl:text>
    <xsl:value-of select="Description"/>
    </xsl:if>
    <xsl:if test="(normalize-space(Url) != '')">
    <xsl:text>
    [More info](</xsl:text>
        <xsl:value-of select="normalize-space(Url)"/>
        <xsl:text>).</xsl:text>
    </xsl:if>
    <xsl:text>
    """
    </xsl:text>
<xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
<xsl:sort select="Idx" data-type="number"/>


<xsl:if test="(IsPrimitive = 'true') and (IsRequired = 'true') and not (IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: </xsl:text>
    <xsl:call-template name="python-type">
        <xsl:with-param name="gw-type" select="PrimitiveType"/>
    </xsl:call-template> <xsl:text> = </xsl:text>
</xsl:if>


<xsl:if test="(IsPrimitive = 'true') and (IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: List[</xsl:text>
    <xsl:call-template name="python-type">
        <xsl:with-param name="gw-type" select="PrimitiveType"/>
    </xsl:call-template>
<xsl:text>] = </xsl:text>
</xsl:if>

<xsl:if test = "(IsEnum = 'true') and not(IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: </xsl:text>
    <xsl:call-template name="nt-case">
                    <xsl:with-param name="type-name-text" select="EnumLocalName" />
    </xsl:call-template> <xsl:text> = </xsl:text>
</xsl:if>

<xsl:if test = "(IsEnum = 'true') and (IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: List[</xsl:text>
    <xsl:call-template name="nt-case">
                    <xsl:with-param name="type-name-text" select="EnumLocalName" />
    </xsl:call-template>
<xsl:text>] = </xsl:text>
</xsl:if>

<xsl:if test="(IsType = 'true') and  not (IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: </xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="SubTypeName" />
    </xsl:call-template>
        <xsl:text> = </xsl:text>
</xsl:if>

<xsl:if test="(IsType = 'true') and (IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: List[</xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="SubTypeName" />
    </xsl:call-template>
    <xsl:text>] = </xsl:text>
 </xsl:if>

 <xsl:if test="not (IsRequired = 'true') and (IsPrimitive = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: Optional[</xsl:text>
    <xsl:call-template name="python-type">
        <xsl:with-param name="gw-type" select="PrimitiveType"/>
    </xsl:call-template>
<xsl:text>] = </xsl:text>
</xsl:if>



<xsl:text>Field(
        title="</xsl:text>
        <xsl:if test="normalize-space(Title)!=''">
        <xsl:value-of select="Title"/>
        </xsl:if>
        <xsl:if test="normalize-space(Title)=''">
        <xsl:value-of select="Value"/>
        </xsl:if>
        <xsl:text>",</xsl:text>

    <xsl:if test="(normalize-space(Description) !='') or (normalize-space(Url) != '')">
        <xsl:text>
        description="</xsl:text>
        <xsl:value-of select="normalize-space(Description)"/>
        <xsl:if test = "(normalize-space(Url) != '')">
        <xsl:text> [More info](</xsl:text>
        <xsl:value-of select="normalize-space(Url)"/>
        <xsl:text>).</xsl:text>
        </xsl:if>
        <xsl:text>",</xsl:text>
    </xsl:if>

    <xsl:if test="(normalize-space(DefaultValue) !='')">
        <xsl:text>
        default=</xsl:text>
         <xsl:if test="IsEnum='true'">
             <xsl:call-template name="nt-case">
                    <xsl:with-param name="type-name-text" select="EnumLocalName" />
            </xsl:call-template><xsl:text>.</xsl:text>
         </xsl:if>
        <xsl:value-of select="DefaultValue"/>
        <xsl:text>,</xsl:text>
    </xsl:if>

    <xsl:if test="not (IsRequired = 'true') and (IsPrimitive = 'true')">
        <xsl:text>
        default=None,</xsl:text>
    </xsl:if>

    <xsl:if test="(normalize-space(PydanticFormat) = 'PositiveInteger') and (IsList != 'true')">
        <xsl:text>
        ge=0,</xsl:text>
    </xsl:if>

    <xsl:text>
    )
    </xsl:text>

</xsl:for-each>


<xsl:text>TypeName: Literal["</xsl:text><xsl:value-of select="TypeName"/><xsl:text>"] = "</xsl:text><xsl:value-of select="TypeName"/><xsl:text>"
    </xsl:text>
<xsl:text>Version: str = "</xsl:text>
<xsl:value-of select="Version"/><xsl:text>"</xsl:text>
    <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
    <xsl:sort select="Idx" data-type="number"/>
    <xsl:variable name="property-id" select="TypeAttributeId" />
    <xsl:if test="(IsRequired='true') and not (IsList='true') and (IsPrimitive='true') and ((normalize-space(PrimitiveFormat) != '') or (Axiom != ''))">
    <xsl:text>

    @validator("</xsl:text><xsl:value-of select="Value"/><xsl:text>")
    def </xsl:text>

    <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 0">
    <xsl:text>_</xsl:text>
    </xsl:if>
    <xsl:text>check_</xsl:text><xsl:call-template name="python-case">
        <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>(cls, v: </xsl:text>
        <xsl:call-template name="python-type">
            <xsl:with-param name="gw-type" select="PrimitiveType"/>
        </xsl:call-template>
        <xsl:text>) -> </xsl:text>
        <xsl:call-template name="python-type">
            <xsl:with-param name="gw-type" select="PrimitiveType"/>
        </xsl:call-template>
        <xsl:text>:</xsl:text>
        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 1">
        <xsl:text>
        """
        Axioms </xsl:text>
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>
        <xsl:value-of select="AxiomNumber"/>
                <xsl:if test="position() != count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)])">
                <xsl:text>, </xsl:text>
                </xsl:if>
        </xsl:for-each>
        <xsl:text>:</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 1">
        <xsl:text>
        """</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) =1">
        <xsl:text>
        Axiom </xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) >1">
        <xsl:text>

        Axiom </xsl:text>
        </xsl:if>

        <xsl:value-of select="AxiomNumber"/><xsl:text>: </xsl:text>
        <xsl:value-of select="Title"/><xsl:text>.
        </xsl:text>
        <xsl:value-of select="Description"/>
        <xsl:if test="normalize-space(Url)!=''">
        <xsl:text>
        [More info](</xsl:text><xsl:value-of select="Url"/>
        <xsl:text>)</xsl:text>

        </xsl:if>

        </xsl:for-each>
        <xsl:text>
        """</xsl:text>
        </xsl:if>
        <xsl:text>
        try:
            check_is_</xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="translate(PrimitiveFormat,'.','_')"  />
                </xsl:call-template>
        <xsl:text>(v)
        except ValueError as e:
            raise ValueError(f"</xsl:text><xsl:value-of select="Value"/><xsl:text> failed </xsl:text>
            <xsl:value-of select="PrimitiveFormat"/>
            <xsl:text> format validation: {e}")</xsl:text>
        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:text>
        raise NotImplementedError("Implement axiom(s)")</xsl:text>
        </xsl:if>
        <xsl:text>
        return v</xsl:text>
    </xsl:if>


    <xsl:if test="(IsRequired = 'true') and (IsEnum='true') and not (IsList='true')">
        <xsl:text>

    @validator("</xsl:text><xsl:value-of select="Value"/><xsl:text>")
    def </xsl:text>

    <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 0">
    <xsl:text>_</xsl:text>
    </xsl:if>
    <xsl:text>check_</xsl:text><xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="Value"  />
    </xsl:call-template><xsl:text>(cls, v: </xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="EnumLocalName" />
    </xsl:call-template>
    <xsl:text>) -> </xsl:text>
        <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="EnumLocalName" />
    </xsl:call-template>
    <xsl:text>:</xsl:text>


        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:text>
        raise NotImplementedError("Implement axiom(s)")</xsl:text>
        </xsl:if>

        <xsl:text>
        return as_enum(v, </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="EnumLocalName" />
        </xsl:call-template>
        <xsl:text>, </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="EnumLocalName" />
        </xsl:call-template>
        <xsl:text>.</xsl:text>
        <xsl:if test= "PythonEnumNameStyle = 'Upper'">
            <xsl:value-of select="translate(translate(DefaultEnumValue,'-',''),$lcletters, $ucletters)"/>
        </xsl:if>
        <xsl:if test="PythonEnumNameStyle ='UpperPython'">
            <xsl:value-of select="DefaultEnumValue"/>
        </xsl:if>
        <xsl:text>)</xsl:text>
    </xsl:if>


    <xsl:if test="(IsRequired = 'true') and (IsPrimitive='true') and (IsList='true') and normalize-space(PrimitiveFormat) != ''">
                <xsl:text>

    @validator("</xsl:text><xsl:value-of select="Value"/><xsl:text>")
    def </xsl:text>

    <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 0">
    <xsl:text>_</xsl:text>
    </xsl:if>
    <xsl:text>check_</xsl:text><xsl:call-template name="python-case">
        <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>(cls, v: List) -> List:</xsl:text>
        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 1">
        <xsl:text>
        """
        Axioms </xsl:text>
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>
        <xsl:value-of select="AxiomNumber"/>
                <xsl:if test="position() != count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)])">
                <xsl:text>, </xsl:text>
                </xsl:if>
        </xsl:for-each>
        <xsl:text>:</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 1">
        <xsl:text>
        """</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) =1">
        <xsl:text>
        Axiom </xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) >1">
        <xsl:text>

        Axiom </xsl:text>
        </xsl:if>

        <xsl:value-of select="AxiomNumber"/><xsl:text>: </xsl:text>
        <xsl:value-of select="Title"/><xsl:text>.
        </xsl:text>
        <xsl:value-of select="Description"/>
        <xsl:if test="normalize-space(Url)!=''">
        <xsl:text>
        [More info](</xsl:text><xsl:value-of select="Url"/>
        <xsl:text>)</xsl:text>

        </xsl:if>

        </xsl:for-each>
        <xsl:text>
        """</xsl:text>
        </xsl:if>
        <xsl:text>
        for elt in v:
            try:
                check_is_</xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="translate(PrimitiveFormat,'.','_')"  />
            </xsl:call-template>
        <xsl:text>(elt)
            except ValueError as e:
                raise ValueError(f"</xsl:text><xsl:value-of select="Value"/><xsl:text> element {elt} failed </xsl:text>
                <xsl:value-of select="PrimitiveFormat" />
                <xsl:text> format validation: {e}")</xsl:text>
        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:text>
        raise NotImplementedError("Implement axiom(s)")</xsl:text>
        </xsl:if>
        <xsl:text>
        return v</xsl:text>
    </xsl:if>

    <xsl:if test=" (IsRequired = 'true') and (IsEnum='true') and (IsList='true')">
        <xsl:text>

    @validator("</xsl:text><xsl:value-of select="Value"/><xsl:text>")
    def </xsl:text>

    <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 0">
    <xsl:text>_</xsl:text>
    </xsl:if>
    <xsl:text>check_</xsl:text><xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="Value"  />
    </xsl:call-template><xsl:text>(cls, v: </xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="EnumName" />
    </xsl:call-template>
    <xsl:text>) -> [</xsl:text>
        <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="EnumName" />
    </xsl:call-template>
    <xsl:text>]:</xsl:text>
        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 1">
        <xsl:text>
        """
        Axioms </xsl:text>
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>
        <xsl:value-of select="AxiomNumber"/>
                <xsl:if test="position() != count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)])">
                <xsl:text>, </xsl:text>
                </xsl:if>
        </xsl:for-each>
        <xsl:text>:</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 1">
        <xsl:text>
        """</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) =1">
        <xsl:text>
        Axiom </xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) >1">
        <xsl:text>

        Axiom </xsl:text>
        </xsl:if>

        <xsl:value-of select="AxiomNumber"/><xsl:text>: </xsl:text>
        <xsl:value-of select="Title"/><xsl:text>.
        </xsl:text>
        <xsl:value-of select="Description"/>
        <xsl:if test="normalize-space(Url)!=''">
        <xsl:text>
        [More info](</xsl:text><xsl:value-of select="Url"/>
        <xsl:text>)</xsl:text>

        </xsl:if>

        </xsl:for-each>
        <xsl:text>
        """</xsl:text>
        </xsl:if>
        <xsl:text>
        if not isinstance(v, List):
            raise ValueError("</xsl:text><xsl:value-of select="Value"/><xsl:text> must be a list!")
        enum_list = []
        for elt in v:
            enum_list.append(as_enum(elt, </xsl:text>
        <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="EnumLocalName" />
    </xsl:call-template>
        <xsl:text>, </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="EnumLocalName" />
        </xsl:call-template>
        <xsl:text>.</xsl:text><xsl:value-of select="DefaultEnumValue"/>
        <xsl:text>))</xsl:text>
        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:text>
        raise NotImplementedError("Implement axiom(s)")</xsl:text>
        </xsl:if>
        <xsl:text>
        return enum_list</xsl:text>
    </xsl:if>

    <xsl:if test="(IsRequired = 'true') and (IsType = 'true') and (IsList = 'true')">
        <xsl:text>

    @validator("</xsl:text><xsl:value-of select="Value"/><xsl:text>")
    def </xsl:text>

    <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 0">
    <xsl:text>_</xsl:text>
    </xsl:if>
    <xsl:text>check_</xsl:text><xsl:call-template name="python-case">
        <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>(cls, v: List) -> List:</xsl:text>
        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 1">
        <xsl:text>
        """
        Axioms </xsl:text>
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>
        <xsl:value-of select="AxiomNumber"/>
                <xsl:if test="position() != count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)])">
                <xsl:text>, </xsl:text>
                </xsl:if>
        </xsl:for-each>
        <xsl:text>:</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 1">
        <xsl:text>
        """</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) =1">
        <xsl:text>
        Axiom </xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) >1">
        <xsl:text>

        Axiom </xsl:text>
        </xsl:if>

        <xsl:value-of select="AxiomNumber"/><xsl:text>: </xsl:text>
        <xsl:value-of select="Title"/><xsl:text>.
        </xsl:text>
        <xsl:value-of select="Description"/>
        <xsl:if test="normalize-space(Url)!=''">
        <xsl:text>
        [More info](</xsl:text><xsl:value-of select="Url"/>
        <xsl:text>)</xsl:text>

        </xsl:if>

        </xsl:for-each>
        <xsl:text>
        """</xsl:text>
        </xsl:if>
        <xsl:text>
        for elt in v:
            if not isinstance(elt, </xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="SubTypeName" />
    </xsl:call-template>
        <xsl:text>):
                raise ValueError(
                        f"elt {elt} of </xsl:text><xsl:value-of select="Value"/>
            <xsl:text> must have type </xsl:text>
                <xsl:call-template name="nt-case">
                        <xsl:with-param name="type-name-text" select="SubTypeName" />
        </xsl:call-template>
                <xsl:text>."
                    )</xsl:text>
        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:text>
        raise NotImplementedError("Implement axiom(s)")</xsl:text>
        </xsl:if>
        <xsl:text>
        return v</xsl:text>
    </xsl:if>



    <xsl:if test=" not(IsRequired = 'true') and (IsPrimitive='true') and not (IsList='true') and normalize-space(PrimitiveFormat) != ''">
    <xsl:text>

    @validator("</xsl:text><xsl:value-of select="Value"/><xsl:text>")
    def </xsl:text>

    <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 0">
    <xsl:text>_</xsl:text>
    </xsl:if>
    <xsl:text>check_</xsl:text>
    <xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="Value"  />
    </xsl:call-template>
    <xsl:text>(cls, v: Optional[</xsl:text>
    <xsl:call-template name="python-type">
        <xsl:with-param name="gw-type" select="PrimitiveType"/>
    </xsl:call-template>
    <xsl:text>]) -> Optional[</xsl:text>
    <xsl:call-template name="python-type">
        <xsl:with-param name="gw-type" select="PrimitiveType"/>
    </xsl:call-template>
    <xsl:text>]:</xsl:text>
        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 1">
        <xsl:text>
        """
        Axioms </xsl:text>
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>
        <xsl:value-of select="AxiomNumber"/>
                <xsl:if test="position() != count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)])">
                <xsl:text>, </xsl:text>
                </xsl:if>
        </xsl:for-each>
        <xsl:text>:</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) = 1">
        <xsl:text>
        """</xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]">
        <xsl:sort select="AxiomNumber" data-type="number"/>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) =1">
        <xsl:text>
        Axiom </xsl:text>
        </xsl:if>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) >1">
        <xsl:text>

        Axiom </xsl:text>
        </xsl:if>

        <xsl:value-of select="AxiomNumber"/><xsl:text>: </xsl:text>
        <xsl:value-of select="Title"/><xsl:text>.
        </xsl:text>
        <xsl:value-of select="Description"/>
        <xsl:if test="normalize-space(Url)!=''">
        <xsl:text>
        [More info](</xsl:text><xsl:value-of select="Url"/>
        <xsl:text>)</xsl:text>

        </xsl:if>

        </xsl:for-each>
        <xsl:text>
        """</xsl:text>
        </xsl:if>
        <xsl:text>
        if v is None:
            return v
        try:
            check_is_</xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="translate(PrimitiveFormat,'.','_')"  />
            </xsl:call-template>
        <xsl:text>(v)
        except ValueError as e:
            raise ValueError(f"</xsl:text>
           <xsl:value-of select="Value"/><xsl:text> failed </xsl:text>
           <xsl:value-of select="PrimitiveFormat"/><xsl:text> format validation: {e}")</xsl:text>

        <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[(normalize-space(SinglePropertyAxiom)=$property-id)]) > 0">
        <xsl:text>
        raise NotImplementedError("Implement axiom(s)")</xsl:text>
        </xsl:if>

        <xsl:text>
        return v</xsl:text>
    </xsl:if>


    <xsl:if test="not (IsRequired = 'true') and (normalize-space(SubTypeDataClass) != '') and not(IsList = 'true')">
        <xsl:text>
        if self.</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>Id:
            if not isinstance(self.</xsl:text><xsl:value-of select="Value"/><xsl:text>Id, str):
                errors.append(
                    f"</xsl:text><xsl:value-of select="Value"/><xsl:text>Id {self.</xsl:text>
                <xsl:value-of select="Value"/><xsl:text>Id} must have type str."
                )
            if not property_format.is_uuid_canonical_textual(self.</xsl:text><xsl:value-of select="Value"/><xsl:text>Id):
                errors.append(
                    f"</xsl:text><xsl:value-of select="Value"/><xsl:text>Id {self.</xsl:text>
                    <xsl:value-of select="Value"/><xsl:text>Id}"
                    " must have format UuidCanonicalTextual"
                )</xsl:text>
    </xsl:if>


        </xsl:for-each>


    <xsl:if test="count($airtable//TypeAxioms/TypeAxiom[MultiPropertyAxiom=$versioned-type-id]) > 0">
    <xsl:for-each select="$airtable//TypeAxioms/TypeAxiom[MultiPropertyAxiom=$versioned-type-id]">
    <xsl:sort select="AxiomNumber" data-type="number"/>
    <xsl:text>

    @root_validator</xsl:text>
    <xsl:if test="CheckFirst='true'">
     <xsl:text>(pre=True)</xsl:text>
    </xsl:if>
    <xsl:text>
    def check_axiom_</xsl:text><xsl:value-of select="AxiomNumber"/><xsl:text>(cls, v: dict) -> dict:
        """
        Axiom </xsl:text><xsl:value-of select="AxiomNumber"/><xsl:text>: </xsl:text>
        <xsl:value-of select="Title"/>
        <xsl:text>.
        </xsl:text><xsl:value-of select="Description"/>
        <xsl:if test="normalize-space(Url)!=''">
        <xsl:text>
        [More info](</xsl:text>
        <xsl:value-of select="normalize-space(Url)"/>
        <xsl:text>)</xsl:text>
        </xsl:if>

        <xsl:text>
        """
        raise NotImplementedError("Implement check for axiom </xsl:text><xsl:value-of select="AxiomNumber"/><xsl:text>")</xsl:text>

    </xsl:for-each>
    </xsl:if>
    <xsl:text>

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()</xsl:text>

        <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
        <xsl:sort select="Idx" data-type="number"/>

        <xsl:if test="(IsType = 'true') and not (IsList = 'true')">
        <xsl:text>
        d["</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>"] = self.</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>.as_dict()</xsl:text>
        </xsl:if>

    <xsl:if test="(IsEnum = 'true')">

        <xsl:variable name="enum-local-name">
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="EnumLocalName" />
            </xsl:call-template>
        </xsl:variable>
        <xsl:variable name="enum-name">
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="EnumName" />
            </xsl:call-template>
        </xsl:variable>

        <xsl:if test="not (IsList = 'true')">
    <xsl:text>
        del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]
        </xsl:text><xsl:value-of select="Value"/>
        <xsl:text> = as_enum(self.</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>, </xsl:text><xsl:value-of select="$enum-local-name"/>
        <xsl:text>, </xsl:text>
        <xsl:value-of select="$enum-local-name"/><xsl:text>.default())
        d["</xsl:text>
        <xsl:call-template name="nt-case">
                        <xsl:with-param name="type-name-text" select="Value" />
        </xsl:call-template>
        <xsl:text>GtEnumSymbol"] = </xsl:text><xsl:value-of select="$enum-local-name"/>
        <xsl:text>Map.local_to_type(</xsl:text><xsl:value-of select="Value"/><xsl:text>)</xsl:text>
        </xsl:if>


        <xsl:if test="(IsList = 'true')">
        <xsl:text>
        del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template> <xsl:text> = []
        for elt in self.</xsl:text>
        <xsl:value-of select="Value"/><xsl:text>:
            </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>.append(</xsl:text>
        <xsl:value-of select="$enum-local-name"/><xsl:text>Map.local_to_type(elt))
        d["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        </xsl:if>

    </xsl:if>


    <xsl:if test="(IsType = 'true') and (IsList = 'true')">
        <xsl:text>

        # Recursively call as_dict() for the SubTypes
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = []
        for elt in self.</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>:
            </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>.append(elt.as_dict())
        d["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
    </xsl:if>

    <xsl:if test="not (IsRequired = 'true')">
        <xsl:text>
        if d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"] is None:
            del d["</xsl:text><xsl:value-of select="Value"/><xsl:text>"]</xsl:text>
    </xsl:if>

    </xsl:for-each>
    <xsl:text>
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class </xsl:text>
<xsl:value-of select="$class-name"/>
<xsl:text>_Maker:
    type_name = "</xsl:text><xsl:value-of select="TypeName"/><xsl:text>"
    version = "</xsl:text><xsl:value-of select="Version"/><xsl:text>"

    def __init__(self</xsl:text>
    <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
    <xsl:sort select="Idx" data-type="number"/>

        <xsl:if test="(IsRequired='true') and (IsPrimitive = 'true') and not (IsList = 'true')">
                <xsl:text>,
                    </xsl:text>
                <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>: </xsl:text>
        <xsl:call-template name="python-type">
            <xsl:with-param name="gw-type" select="PrimitiveType"/>
        </xsl:call-template>
        </xsl:if>

        <xsl:if test="(IsRequired='true') and (IsPrimitive = 'true') and (IsList = 'true')">
                <xsl:text>,
                    </xsl:text>
            <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>: List[</xsl:text>
        <xsl:call-template name="python-type">
            <xsl:with-param name="gw-type" select="PrimitiveType"/>
        </xsl:call-template><xsl:text>]</xsl:text>
        </xsl:if>


        <xsl:if test="(IsRequired='true') and (IsEnum = 'true') and not (IsList = 'true')">
                <xsl:text>,
                    </xsl:text>
                <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>: </xsl:text>
        <xsl:call-template name="nt-case">
                        <xsl:with-param name="type-name-text" select="EnumLocalName" />
        </xsl:call-template>
        </xsl:if>

        <xsl:if test="(IsRequired='true') and (IsEnum = 'true') and (IsList = 'true')">
                <xsl:text>,
                    </xsl:text>
                <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>: List[</xsl:text>
        <xsl:call-template name="nt-case">
                        <xsl:with-param name="type-name-text" select="EnumLocalName" />
        </xsl:call-template><xsl:text>]</xsl:text>
        </xsl:if>

        <xsl:if test="(IsRequired='true') and (IsType = 'true') and not (IsList = 'true')">
                <xsl:text>,
                    </xsl:text>
                    <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template><xsl:text>: </xsl:text>
                <xsl:call-template name="nt-case">
                    <xsl:with-param name="type-name-text" select="SubTypeName" />
                </xsl:call-template>
        </xsl:if>

        <xsl:if test="(IsRequired='true') and (IsType = 'true') and (IsList = 'true')">
                <xsl:text>,
                    </xsl:text>
                <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template><xsl:text>: List[</xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="SubTypeName" />
            </xsl:call-template>
                <xsl:text>]</xsl:text>
        </xsl:if>


        <xsl:if test=" not (IsRequired='true') and (IsPrimitive = 'true') ">
                <xsl:text>,
                    </xsl:text>
                <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template><xsl:text>: Optional[</xsl:text>
            <xsl:call-template name="python-type">
            <xsl:with-param name="gw-type" select="PrimitiveType"/>
            </xsl:call-template><xsl:text>]</xsl:text>
        </xsl:if>

        <xsl:if test="not (IsRequired='true') and not(normalize-space(SubTypeDataClass) = '')">
                <xsl:text>,
                    </xsl:text>
            <xsl:call-template name="python-case">
        <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>_id: Optional[str]</xsl:text>
        </xsl:if>
        </xsl:for-each>
    <xsl:text>):

        self.tuple = </xsl:text><xsl:value-of select="$class-name"/>
        <xsl:text>(
            </xsl:text>
        <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
        <xsl:sort select="Idx" data-type="number"/>
        <xsl:value-of select="Value"/><xsl:text>=</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>,
            </xsl:text>

    </xsl:for-each>
    <xsl:text>#
        )

    @classmethod
    def tuple_to_type(cls, tuple: </xsl:text><xsl:value-of select="$class-name"/>
    <xsl:text>) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> </xsl:text><xsl:value-of select="$class-name"/>
<xsl:text>:
        """
        Given a serialized JSON type object, returns the Python class object
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> </xsl:text><xsl:value-of select="$class-name"/>
<xsl:text>:
        d2 = dict(d)</xsl:text>
<xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
<xsl:sort select="Idx" data-type="number"/>

<xsl:if test = "(IsRequired = 'true') and (IsPrimitive='true')">
<xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/><xsl:text>" not in d2.keys():
            raise SchemaError(f"dict {d2} missing </xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>")</xsl:text>

</xsl:if>


<xsl:if test="(IsRequired = 'true') and (IsType = 'true') and not (IsList = 'true')">
<xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/><xsl:text>" not in d2.keys():
            raise SchemaError(f"dict {d2} missing </xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>")
        if not isinstance(d2["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"], dict):
            raise SchemaError(f"d['</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>'] {d2['</xsl:text><xsl:value-of select="Value"/>
            <xsl:text>']} must be a </xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="SubTypeName" />
            </xsl:call-template>
            <xsl:text>!")
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="SubTypeName" />
        </xsl:call-template>
        <xsl:text>_Maker.dict_to_tuple(d2["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"])
        d2["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
</xsl:if>



<xsl:if test="(IsType = 'true') and (IsList = 'true')">
    <xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/><xsl:text>" not in d2.keys():
            raise SchemaError(f"dict {d2} missing </xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>")
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = []
        if not isinstance(d2["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"], List):
            raise SchemaError("</xsl:text>
                <xsl:value-of select="Value"/>
                <xsl:text> must be a List!")
        for elt in d2["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"elt {elt} of </xsl:text>
                    <xsl:value-of select="Value"/>
                    <xsl:text> must be "
                    "</xsl:text>
                    <xsl:call-template name="nt-case">
                        <xsl:with-param name="type-name-text" select="SubTypeName" />
                    </xsl:call-template>
                    <xsl:text> but not even a dict!"
                )
            </xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template>
            <xsl:text>.append(
                </xsl:text>
                <xsl:call-template name="nt-case">
                    <xsl:with-param name="type-name-text" select="SubTypeName" />
                </xsl:call-template>
                <xsl:text>_Maker.dict_to_tuple(elt)
            )
        d2["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>

</xsl:if>


<xsl:if test="(IsEnum = 'true') and  not (IsList = 'true')">
<xsl:text>
        if "</xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="Value" />
        </xsl:call-template><xsl:text>GtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing </xsl:text>
            <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="Value" />
        </xsl:call-template>
            <xsl:text>GtEnumSymbol")
        if d2["</xsl:text> <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="Value" />
        </xsl:call-template><xsl:text>GtEnumSymbol"] in </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="EnumName" />
        </xsl:call-template>
        <xsl:text>SchemaEnum.symbols:
            d2["</xsl:text> <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="Value" />
        </xsl:call-template><xsl:text>"] = </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="EnumLocalName" />
        </xsl:call-template>
        <xsl:text>Map.type_to_local(d2["</xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="Value" />
        </xsl:call-template><xsl:text>GtEnumSymbol"])
        else:
            d2["</xsl:text> <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="Value" />
        </xsl:call-template><xsl:text>"] = </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="type-name-text" select="EnumLocalName" />
        </xsl:call-template>
        <xsl:text>.default()</xsl:text>
    </xsl:if>


<xsl:if test="(IsEnum = 'true') and (IsList = 'true')">
<xsl:text>
        if "</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>" not in d2.keys():
            raise SchemaError(f"dict {d2} missing </xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>")
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = []
        if not isinstance(d2["</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>"], List):
                raise SchemaError("</xsl:text>
                    <xsl:value-of select="Value"/>
                    <xsl:text> must be a List!")
        for elt in d2["</xsl:text>
        <xsl:value-of select="Value"/>
        <xsl:text>"]:
            if elt in </xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="EnumName" />
            </xsl:call-template>
            <xsl:text>SchemaEnum.symbols:
                v = </xsl:text>
                <xsl:call-template name="nt-case">
                    <xsl:with-param name="type-name-text" select="EnumLocalName" />
                </xsl:call-template>
                <xsl:text>Map.type_to_local(elt)
            else:
                v = </xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="type-name-text" select="EnumName" />
            </xsl:call-template>
            <xsl:text>.</xsl:text><xsl:value-of select="DefaultEnumValue"/><xsl:text> #

            </xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template>
            <xsl:text>.append(v)
        d2["</xsl:text><xsl:value-of select="Value"/>
        <xsl:text>"] = </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
</xsl:if>

<xsl:if test="(IsPrimitive = 'true') and not(IsRequired = 'true')">
<xsl:text>
        if "</xsl:text><xsl:value-of select="Value"/><xsl:text>" not in d2.keys():
            d2["</xsl:text>
            <xsl:value-of select="Value"/>
            <xsl:text>"] = None</xsl:text>
</xsl:if>
</xsl:for-each>
<xsl:text>
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return </xsl:text><xsl:value-of select="$class-name"/><xsl:text>(
            </xsl:text>
        <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
        <xsl:sort select="Idx" data-type="number"/>
        <xsl:value-of select="Value"/><xsl:text>=d2["</xsl:text>
        <xsl:value-of select="Value"/><xsl:text>"],
            </xsl:text>
        </xsl:for-each>
            <xsl:text>TypeName=d2["TypeName"],
            Version="</xsl:text><xsl:value-of select="Version"/><xsl:text>",
        )
</xsl:text>
    <xsl:if test="(MakeDataClass='true')">
    <xsl:text>
    @classmethod
    def tuple_to_dc(cls, t: </xsl:text><xsl:value-of select="$class-name"/>
    <xsl:text>) -> </xsl:text><xsl:value-of select="DataClass"/><xsl:text>:
        if t.</xsl:text><xsl:value-of select="DataClassIdField"/><xsl:text> in </xsl:text>
        <xsl:value-of select="DataClass"/><xsl:text>.by_id.keys():
            dc = </xsl:text><xsl:value-of select="DataClass"/><xsl:text>.by_id[t.</xsl:text>
            <xsl:value-of select="DataClassIdField"/><xsl:text>]
        else:
            dc = </xsl:text><xsl:value-of select="DataClass"/><xsl:text>(
            </xsl:text>
        <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
        <xsl:sort select="Idx" data-type="number"/>

            <xsl:if test="(normalize-space(SubTypeName) !='')">
                <xsl:call-template name="python-case">
                    <xsl:with-param name="camel-case-text" select="Value"  />
                </xsl:call-template><xsl:text>=</xsl:text>
                        <xsl:call-template name="nt-case">
                            <xsl:with-param name="type-name-text" select="SubTypeName" />
                        </xsl:call-template>
                <xsl:text>_Maker.tuple_to_dc(t.</xsl:text>
        <xsl:value-of select="Value"/><xsl:text>),
            </xsl:text>
            </xsl:if>

            <xsl:if test="(normalize-space(SubTypeName)='')">
                <xsl:call-template name="python-case">
                    <xsl:with-param name="camel-case-text" select="Value"  />
                </xsl:call-template><xsl:text>=t.</xsl:text>
        <xsl:value-of select="Value"/><xsl:text>,
            </xsl:text>
            </xsl:if>

    </xsl:for-each>
            <xsl:text>
            )

        return dc

    @classmethod
    def dc_to_tuple(cls, dc: </xsl:text><xsl:value-of select="DataClass"/><xsl:text>) -> </xsl:text><xsl:value-of select="$class-name"/><xsl:text>:
        t = </xsl:text><xsl:value-of select="$class-name"/><xsl:text>_Maker(
            </xsl:text>
        <xsl:for-each select="$airtable//TypeAttributes/TypeAttribute[(VersionedType = $versioned-type-id)]">
        <xsl:sort select="Idx" data-type="number"/>

        <xsl:if test="(normalize-space(SubTypeName) ='')">
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>=dc.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>,
            </xsl:text>
        </xsl:if>


        <xsl:if test="(normalize-space(SubTypeName)!='')">
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>=</xsl:text><xsl:call-template name="nt-case">
                            <xsl:with-param name="type-name-text" select="SubTypeName" />
                        </xsl:call-template>
                <xsl:text>_Maker.dc_to_tuple(dc.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>),
            </xsl:text>
        </xsl:if>
        </xsl:for-each>
        <xsl:text>
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> </xsl:text><xsl:value-of select="DataClass"/><xsl:text>:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: </xsl:text><xsl:value-of select="DataClass"/><xsl:text>) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> </xsl:text><xsl:value-of select="DataClass"/><xsl:text>:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
</xsl:text>
</xsl:if>




                        </xsl:element>
                     </FileSetFile>
                </xsl:for-each>
                </xsl:for-each>
            </FileSetFiles>
        </FileSet>
    </xsl:template>


</xsl:stylesheet>
