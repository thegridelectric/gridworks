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
                <xsl:variable name="schema-id" select="Type"/>
                <xsl:for-each select="$airtable//Schemas/Schema[(SchemaId = $schema-id)  and (Status = 'Active' or Status = 'Pending') and (ProtocolCategory= 'Json' or ProtocolCategory = 'GwAlgoSerial')]">
                <xsl:variable name="local-alias" select="AliasRoot" />
                    <xsl:variable name="class-name">
                        <xsl:call-template name="nt-case">
                            <xsl:with-param name="mp-schema-text" select="$local-alias" />
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
                                <xsl:element name="RelativePath"><xsl:text>../../../src/gridworks/schemata/</xsl:text>
                                <xsl:value-of select="translate($local-alias,'.','_')"/><xsl:text>.py</xsl:text></xsl:element>

                        <OverwriteMode><xsl:value-of select="$overwrite-mode"/></OverwriteMode>
                        <xsl:element name="FileContents">


<xsl:text>"""Type </xsl:text><xsl:value-of select="AliasRoot"/><xsl:text>, version </xsl:text>
<xsl:value-of select="SemanticEnd"/><xsl:text>"""
import json
from typing import Any
from typing import Dict</xsl:text>
<xsl:if test="count($airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and ((IsEnum = 'true') or (IsList = 'true'))])>0">
<xsl:text>
from typing import List</xsl:text>
</xsl:if>
<xsl:text>
from typing import Literal</xsl:text>

<xsl:if test="count($airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and not (IsRequired = 'true')]) > 0">
<xsl:text>
from typing import Optional</xsl:text>
</xsl:if>
<xsl:text>
from pydantic import BaseModel</xsl:text>
<xsl:if test="count($airtable//SchemaAttributes/SchemaAttribute[Schema = $schema-id and (IsOptional='true') or (IsEnum='true' or (IsList='true' and (IsType = 'true' or (IsPrimitive='true'  and normalize-space(PrimitiveFormat) != '') )))]) > 0">
<xsl:text>
from pydantic import validator</xsl:text>
</xsl:if>




<xsl:if test="count($airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and (IsEnum = 'true')]) > 0">
<xsl:text>
from gridworks.message import as_enum
from enum import auto
from fastapi_utils.enums import StrEnum</xsl:text>
</xsl:if>
<xsl:if test="count($airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and ((normalize-space(SubTypeDataClass) != '') or (normalize-space(PrimitiveFormat) != ''))]) > 0">
<xsl:text>
import gridworks.property_format as property_format</xsl:text>
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

<xsl:if test="count($airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id) and (IsRequired = 'true') and (IsPrimitive='true') and not (IsList='true') and normalize-space(PrimitiveFormat) != '']) > 0">
<xsl:text>
from gridworks.property_format import predicate_validator</xsl:text>
</xsl:if>
<xsl:text>
from gridworks.errors import SchemaError
</xsl:text>

<xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">


<xsl:if test="(IsType = 'true')">
<xsl:text>
from gridworks.schemata.</xsl:text>
<xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="translate(SubMessageFormatAliasRoot,'.','_')"  />
</xsl:call-template>
<xsl:text> import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
</xsl:call-template>
<xsl:text>
from gridworks.schemata.</xsl:text>
<xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="translate(SubMessageFormatAliasRoot,'.','_')"  />
</xsl:call-template>
<xsl:text> import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
</xsl:call-template><xsl:text>_Maker</xsl:text>
</xsl:if>
</xsl:for-each>
<xsl:for-each select="$airtable//GtEnums/GtEnum[(normalize-space(Alias) !='')  and (count(TypesThatUse[text()=$schema-id])>0)]">
<xsl:text>
from gridworks.enums import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="mp-schema-text" select="LocalName" />
</xsl:call-template>
<xsl:if test="(normalize-space(EnumAbbreviation) !='')">
<xsl:text> as </xsl:text>
<xsl:value-of select="EnumAbbreviation"/>
</xsl:if>
</xsl:for-each>

<xsl:for-each select="$airtable//GtEnums/GtEnum[(normalize-space(Alias) !='')  and (count(TypesThatUse[text()=$schema-id])>0)]">
<xsl:variable name="enum-alias" select="Alias" />
<xsl:variable name="enum-name-style" select="PythonEnumNameStyle" />
<xsl:variable name="enum-name">
    <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="Alias" />
    </xsl:call-template>
</xsl:variable>
<xsl:variable name="enum-local-name">
    <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="LocalName" />
    </xsl:call-template>
</xsl:variable>
<xsl:variable name="enum-id" select="GtEnumId"/>



<xsl:text>

class </xsl:text><xsl:value-of select="$enum-name"/><xsl:text>SchemaEnum:
    enum_name: str = "</xsl:text>
    <xsl:value-of select="Alias"/>
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
<xsl:text>(StrEnum):
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

<xsl:text>


class </xsl:text>
<xsl:value-of select="$class-name"/>
<xsl:text>(BaseModel):
    </xsl:text>
<xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
<xsl:sort select="Idx" data-type="number"/>

<xsl:if test="(IsPrimitive = 'true') and (IsRequired = 'true') and not (IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: </xsl:text>
    <xsl:call-template name="python-type">
        <xsl:with-param name="gw-type" select="PrimitiveType"/>
    </xsl:call-template>
    <xsl:if test="(normalize-space(DefaultValue) !='')">
        <xsl:text> = </xsl:text>
        <xsl:value-of select="DefaultValue"/>
    </xsl:if>
<xsl:text>  #
    </xsl:text>
</xsl:if>


<xsl:if test="(IsPrimitive = 'true') and (IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: List[</xsl:text>
    <xsl:call-template name="python-type">
        <xsl:with-param name="gw-type" select="PrimitiveType"/>
    </xsl:call-template>
<xsl:text>]</xsl:text>
    <xsl:if test="(normalize-space(DefaultValue) !='')">
        <xsl:text> = </xsl:text>
        <xsl:value-of select="DefaultValue"/>
    </xsl:if>
    <xsl:text>  #
    </xsl:text>
</xsl:if>


<xsl:if test = "(IsEnum = 'true') and not(IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: </xsl:text>
    <xsl:call-template name="nt-case">
                    <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
    </xsl:call-template>
    <xsl:if test="(normalize-space(DefaultValue) !='')">
        <xsl:text> = </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
    </xsl:call-template><xsl:text>.</xsl:text>
        <xsl:value-of select="DefaultValue"/>
    </xsl:if>
<xsl:text>  #
    </xsl:text>
</xsl:if>


<xsl:if test = "(IsEnum = 'true') and (IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: List[</xsl:text>
    <xsl:call-template name="nt-case">
                    <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
    </xsl:call-template>
<xsl:text>]
    </xsl:text>
    <xsl:if test="(normalize-space(DefaultValue) !='')">
        <xsl:text> = </xsl:text>
        <xsl:value-of select="DefaultValue"/>
    </xsl:if>
    <xsl:text>  #
    </xsl:text>
</xsl:if>


<xsl:if test="(IsType = 'true') and  not (IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: </xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
    </xsl:call-template>
    <xsl:if test="(normalize-space(DefaultValue) !='')">
        <xsl:text> = </xsl:text>
        <xsl:value-of select="DefaultValue"/>
    </xsl:if>
    <xsl:text>  #
    </xsl:text>
</xsl:if>

<xsl:if test="(IsType = 'true') and (IsList = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: List[</xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
    </xsl:call-template>
    <xsl:text>]
    </xsl:text>
    <xsl:if test="(normalize-space(DefaultValue) !='')">
        <xsl:text> = </xsl:text>
        <xsl:value-of select="DefaultValue"/>
    </xsl:if>
    <xsl:text>  #
    </xsl:text>
 </xsl:if>
 <xsl:if test="not (IsRequired = 'true') and (IsPrimitive = 'true')">
    <xsl:value-of select="Value"/><xsl:text>: Optional[</xsl:text>
    <xsl:call-template name="python-type">
        <xsl:with-param name="gw-type" select="PrimitiveType"/>
    </xsl:call-template>
<xsl:text>] = None
    </xsl:text>
</xsl:if>

</xsl:for-each>


<xsl:text>TypeName: Literal["</xsl:text><xsl:value-of select="AliasRoot"/><xsl:text>"] = "</xsl:text><xsl:value-of select="AliasRoot"/><xsl:text>"
    </xsl:text>
<xsl:text>Version: str = "</xsl:text>
<xsl:value-of select="SemanticEnd"/><xsl:text>"</xsl:text>
    <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
    <xsl:sort select="Idx" data-type="number"/>

    <xsl:if test="(IsRequired = 'true') and (IsPrimitive='true') and not (IsList='true') and normalize-space(PrimitiveFormat) != ''">
            <xsl:text>

    _validator_</xsl:text>
        <xsl:call-template name="python-case">
        <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
    <xsl:text> = predicate_validator("</xsl:text>
        <xsl:value-of select = "Value"/><xsl:text>", property_format.is_</xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="translate(PrimitiveFormat,'.','_')"  />
                </xsl:call-template>
        <xsl:text>)</xsl:text>
    </xsl:if>


    <xsl:if test="(IsRequired = 'true') and (IsEnum='true') and not (IsList='true')">
        <xsl:text>

    @validator("</xsl:text><xsl:value-of select="Value"/><xsl:text>")
    def _validator_</xsl:text><xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="Value"  />
    </xsl:call-template><xsl:text>(cls, v: </xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
    </xsl:call-template>
    <xsl:text>) -> </xsl:text>
        <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
    </xsl:call-template>
    <xsl:text>:
        return as_enum(v, </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
        </xsl:call-template>
        <xsl:text>, </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
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
    def _validator_</xsl:text><xsl:call-template name="python-case">
        <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_</xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="translate(PrimitiveFormat,'.','_')"  />
            </xsl:call-template>
        <xsl:text>(elt):
                raise ValueError(f"failure of predicate is_</xsl:text>
                <xsl:call-template name="python-case">
                    <xsl:with-param name="camel-case-text" select="translate(PrimitiveFormat,'.','_')"  />
                </xsl:call-template>

                <xsl:text>() on elt {elt} of </xsl:text><xsl:value-of select="Value"/>
            <xsl:text>")
        return v</xsl:text>
    </xsl:if>

    <xsl:if test=" (IsRequired = 'true') and (IsEnum='true') and (IsList='true')">
        <xsl:text>

    @validator("</xsl:text><xsl:value-of select="Value"/><xsl:text>")
    def _validator_</xsl:text><xsl:call-template name="python-case">
    <xsl:with-param name="camel-case-text" select="Value"  />
    </xsl:call-template><xsl:text>(cls, v: </xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="EnumName" />
    </xsl:call-template>
    <xsl:text>) -> [</xsl:text>
        <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="EnumName" />
    </xsl:call-template>
    <xsl:text>]:
        if not isinstance(v, List):
            raise ValueError("</xsl:text><xsl:value-of select="Value"/><xsl:text> must be a list!")
        enum_list = []
        for elt in v:
            enum_list.append(as_enum(elt, </xsl:text>
        <xsl:call-template name="nt-case">
        <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
    </xsl:call-template>
        <xsl:text>, </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
        </xsl:call-template>
        <xsl:text>.</xsl:text><xsl:value-of select="DefaultEnumValue"/>
        <xsl:text>))
        return enum_list</xsl:text>
    </xsl:if>

    <xsl:if test="(IsRequired = 'true') and (IsType = 'true') and (IsList = 'true')">
        <xsl:text>

    @validator("</xsl:text><xsl:value-of select="Value"/><xsl:text>")
    def _validator_</xsl:text><xsl:call-template name="python-case">
        <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>(cls, v: List) -> List:
        for elt in v:
            if not isinstance(elt, </xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
    </xsl:call-template>
        <xsl:text>):
                raise ValueError(
                        f"elt {elt} of </xsl:text><xsl:value-of select="Value"/>
            <xsl:text> must have type </xsl:text>
                <xsl:call-template name="nt-case">
                        <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
        </xsl:call-template>
                <xsl:text>."
                    )
        return v</xsl:text>
    </xsl:if>



    <xsl:if test=" not(IsRequired = 'true') and (IsPrimitive='true') and not (IsList='true') and normalize-space(PrimitiveFormat) != ''">
    <xsl:text>

    @validator("</xsl:text><xsl:value-of select="Value"/><xsl:text>")
    def _validator_</xsl:text>
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
    <xsl:text>]:
        if v is None:
            return v
        if not property_format.is_</xsl:text>
            <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="translate(PrimitiveFormat,'.','_')"  />
            </xsl:call-template>
        <xsl:text>(v):
            raise ValueError(f"</xsl:text>
           <xsl:value-of select="Value"/><xsl:text> {v} must have </xsl:text>
           <xsl:value-of select="PrimitiveFormat"/><xsl:text>")
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

    <xsl:text>

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()</xsl:text>

        <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
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
                <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
            </xsl:call-template>
        </xsl:variable>
        <xsl:variable name="enum-name">
            <xsl:call-template name="nt-case">
                <xsl:with-param name="mp-schema-text" select="EnumName" />
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
                        <xsl:with-param name="mp-schema-text" select="Value" />
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
    type_name = "</xsl:text><xsl:value-of select="AliasRoot"/><xsl:text>"
    version = "</xsl:text><xsl:value-of select="SemanticEnd"/><xsl:text>"

    def __init__(self</xsl:text>
    <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
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
                        <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
        </xsl:call-template>
        </xsl:if>

        <xsl:if test="(IsRequired='true') and (IsEnum = 'true') and (IsList = 'true')">
                <xsl:text>,
                    </xsl:text>
                <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>: List[</xsl:text>
        <xsl:call-template name="nt-case">
                        <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
        </xsl:call-template><xsl:text>]</xsl:text>
        </xsl:if>

        <xsl:if test="(IsRequired='true') and (IsType = 'true') and not (IsList = 'true')">
                <xsl:text>,
                    </xsl:text>
                    <xsl:call-template name="python-case">
                <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template><xsl:text>: </xsl:text>
                <xsl:call-template name="nt-case">
                    <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
                </xsl:call-template>
        </xsl:if>

        <xsl:if test="(IsRequired='true') and (IsType = 'true') and (IsList = 'true')">
                <xsl:text>,
                    </xsl:text>
                <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
            </xsl:call-template><xsl:text>: List[</xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
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
        <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
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
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> </xsl:text><xsl:value-of select="$class-name"/>
<xsl:text>:
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
<xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
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
                <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
            </xsl:call-template>
            <xsl:text>!")
        </xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text> = </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
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
                        <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
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
                    <xsl:with-param name="mp-schema-text" select="SubMessageFormatAliasRoot" />
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
            <xsl:with-param name="mp-schema-text" select="Value" />
        </xsl:call-template><xsl:text>GtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing </xsl:text>
            <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="Value" />
        </xsl:call-template>
            <xsl:text>GtEnumSymbol")
        if d2["</xsl:text> <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="Value" />
        </xsl:call-template><xsl:text>GtEnumSymbol"] in </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="EnumName" />
        </xsl:call-template>
        <xsl:text>SchemaEnum.symbols:
            d2["</xsl:text> <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="Value" />
        </xsl:call-template><xsl:text>"] = </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
        </xsl:call-template>
        <xsl:text>Map.type_to_local(d2["</xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="Value" />
        </xsl:call-template><xsl:text>GtEnumSymbol"])
        else:
            d2["</xsl:text> <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="Value" />
        </xsl:call-template><xsl:text>"] = </xsl:text>
        <xsl:call-template name="nt-case">
            <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
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
                <xsl:with-param name="mp-schema-text" select="EnumName" />
            </xsl:call-template>
            <xsl:text>SchemaEnum.symbols:
                v = </xsl:text>
                <xsl:call-template name="nt-case">
                    <xsl:with-param name="mp-schema-text" select="EnumLocalName" />
                </xsl:call-template>
                <xsl:text>Map.type_to_local(elt)
            else:
                v = </xsl:text>
            <xsl:call-template name="nt-case">
                <xsl:with-param name="mp-schema-text" select="EnumName" />
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
        <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
        <xsl:sort select="Idx" data-type="number"/>
        <xsl:value-of select="Value"/><xsl:text>=d2["</xsl:text>
        <xsl:value-of select="Value"/><xsl:text>"],
            </xsl:text>
        </xsl:for-each>
            <xsl:text>TypeName=d2["TypeName"],
            Version="</xsl:text><xsl:value-of select="SemanticEnd"/><xsl:text>",
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
        <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
        <xsl:sort select="Idx" data-type="number"/>
            <xsl:text></xsl:text>
                <xsl:call-template name="python-case">
                    <xsl:with-param name="camel-case-text" select="Value"  />
                </xsl:call-template><xsl:text>=t.</xsl:text>
        <xsl:value-of select="Value"/><xsl:text>,
            </xsl:text>
    </xsl:for-each>
            <xsl:text>
            )

        return dc

    @classmethod
    def dc_to_tuple(cls, dc: </xsl:text><xsl:value-of select="DataClass"/><xsl:text>) -> </xsl:text><xsl:value-of select="$class-name"/><xsl:text>:
        t = </xsl:text><xsl:value-of select="$class-name"/><xsl:text>_Maker(
            </xsl:text>
        <xsl:for-each select="$airtable//SchemaAttributes/SchemaAttribute[(Schema = $schema-id)]">
        <xsl:sort select="Idx" data-type="number"/>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template><xsl:text>=dc.</xsl:text>
        <xsl:call-template name="python-case">
            <xsl:with-param name="camel-case-text" select="Value"  />
        </xsl:call-template>
        <xsl:text>,
            </xsl:text>
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
