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
                    <xsl:element name="RelativePath"><xsl:text>../../../../../docs/asls/enums.rst</xsl:text></xsl:element>

                <OverwriteMode>Always</OverwriteMode>
                <xsl:element name="FileContents">
<xsl:text>
Enum Application Shared Language (ASL) Specifications
===============

</xsl:text>
<xsl:for-each select="$airtable//ProtocolEnums/ProtocolEnum[(normalize-space(ProtocolName) ='gridworks')]">
<xsl:sort select="VersionedTypeName" data-type="text"/>
<xsl:variable name="versioned-enum-id" select="VersionedEnum"/>
<xsl:for-each select="$airtable//VersionedEnums/VersionedEnum[(VersionedEnumId = $versioned-enum-id)  and (Status = 'Active' or Status = 'Pending')]">
<xsl:value-of select="VersionedEnumName" />
<xsl:text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: json/</xsl:text>
<xsl:value-of select="translate(EnumName,'.','-')"/>
<xsl:text>.json

</xsl:text>

</xsl:for-each>
</xsl:for-each>

                </xsl:element>
            </FileSetFile>


        </FileSet>
    </xsl:template>


</xsl:stylesheet>
