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

            <FileSetFile>
                    <xsl:element name="RelativePath"><xsl:text>../../../../src/gridworks/enums/__init__.py</xsl:text></xsl:element>

                <OverwriteMode>Always</OverwriteMode>
                <xsl:element name="FileContents">
<xsl:text>""" GwSchema Enums used in gridworks """</xsl:text>
<xsl:for-each select="$airtable//ProtocolEnums/ProtocolEnum[(normalize-space(ProtocolName) ='gridworks')]">
<xsl:sort select="EnumName" data-type="text"/>
<xsl:variable name="enum-id" select="Enum"/>
<xsl:for-each select="$airtable//GtEnums/GtEnum[GtEnumId=$enum-id]">
<xsl:text>
from gridworks.enums.</xsl:text>
<xsl:value-of select="translate(LocalName,'.','_')"/>
<xsl:text> import </xsl:text>
<xsl:call-template name="nt-case">
    <xsl:with-param name="type-name-text" select="LocalName" />
</xsl:call-template>

</xsl:for-each>
</xsl:for-each>
<xsl:text>


__all__ = [</xsl:text>
<xsl:for-each select="$airtable//ProtocolEnums/ProtocolEnum[(normalize-space(ProtocolName) ='gridworks')]">
<xsl:sort select="EnumName" data-type="text"/>
<xsl:variable name="enum-id" select="Enum"/>
<xsl:for-each select="$airtable//GtEnums/GtEnum[GtEnumId=$enum-id]">

<xsl:text>
    "</xsl:text>
    <xsl:call-template name="nt-case">
        <xsl:with-param name="type-name-text" select="LocalName" />
    </xsl:call-template>
    <xsl:text>",</xsl:text>
</xsl:for-each>
</xsl:for-each>
<xsl:text>
]

</xsl:text>



                </xsl:element>
            </FileSetFile>


        </FileSet>
    </xsl:template>


</xsl:stylesheet>
