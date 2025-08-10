<?xml version="1.0" encoding="utf-8"?>
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
                <xsl:for-each select="$airtable//ProtocolEnums/ProtocolEnum[(normalize-space(ProtocolName) ='gridworks') and not (NoVersions = 'true')]">
                <xsl:variable name="enum-id" select="GtEnumId"/>
                <xsl:variable name="enum-version" select="EnumVersion"/>
                <xsl:variable name="enum-name" select="EnumName"/>
                <xsl:variable name="local-name" select="LocalName"/>
                <xsl:for-each select="$airtable//GtEnums/GtEnum[GtEnumId=$enum-id]">
                    <xsl:variable name="enum-type" select="EnumType" />
                    <xsl:variable name="enum-description" select="normalize-space(Description)" />
                    <FileSetFile>
                        <xsl:element name="RelativePath"><xsl:text>../../../../type_definitions/enums/</xsl:text>
                        <xsl:value-of select="$enum-name"/><xsl:text>.yaml</xsl:text></xsl:element>

                        <OverwriteMode>Always</OverwriteMode>
                        <xsl:element name="FileContents">

<xsl:text>$schema: "https://json-schema.org/draft/2020-12/schema"
$id: "https://schemas.gridworks.energy/enums/</xsl:text><xsl:value-of select="$enum-name"/><xsl:text>"

# For comprehensive ASL documentation, see: https://gridworks-asl.readthedocs.io/
title: "</xsl:text><xsl:value-of select="$enum-name"/><xsl:text>"
type: "string"
description: "</xsl:text>
<!-- Handle special case for message category enums -->
<xsl:choose>
  <xsl:when test="contains($enum-name, 'message.category')">
    <xsl:value-of select="$enum-description"/>
  </xsl:when>
  <xsl:otherwise>
    <xsl:value-of select="$enum-description"/>
  </xsl:otherwise>
</xsl:choose>
<xsl:text>"

enum:</xsl:text>
<xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id) and (Version &lt;= $enum-version)]">
<xsl:sort select="Idx" data-type="number"/>
<xsl:text>
  - "</xsl:text><xsl:value-of select="LocalValue"/><xsl:text>"</xsl:text>
</xsl:for-each>

<xsl:text>

default: "</xsl:text><xsl:value-of select="DefaultEnumValue"/><xsl:text>"

x-gridworks:
  owner: "gridworks-energy"
  version: "</xsl:text><xsl:value-of select="$enum-version"/><xsl:text>"
  stable: true
  use_cases: ["ASL enum usage"]
  value_descriptions:</xsl:text>

<xsl:for-each select="$airtable//EnumSymbols/EnumSymbol[(Enum = $enum-id) and (Version &lt;= $enum-version)]">
<xsl:sort select="Idx" data-type="number"/>
<xsl:text>
    "</xsl:text><xsl:value-of select="LocalValue"/><xsl:text>": "</xsl:text>
<xsl:choose>
  <xsl:when test="normalize-space(Description) != ''">
    <xsl:value-of select="normalize-space(Description)"/>
  </xsl:when>
  <xsl:otherwise>
    <xsl:value-of select="LocalValue"/> <xsl:text> value</xsl:text>
  </xsl:otherwise>
</xsl:choose>
<xsl:text>"</xsl:text>
</xsl:for-each>

<!-- Add newline at EOF for git and pre-commit-->
<xsl:text>&#10;</xsl:text>

                        </xsl:element>
                     </FileSetFile>
                </xsl:for-each>
                </xsl:for-each>

            </FileSetFiles>
        </FileSet>
    </xsl:template>

</xsl:stylesheet>