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
                    <xsl:element name="RelativePath"><xsl:text>../../../../../../docs/sdk-types.rst</xsl:text></xsl:element>

                <OverwriteMode>Always</OverwriteMode>
                <xsl:element name="FileContents">
<xsl:text>
SDK for `gridworks &lt;https://pypi.org/project/gridworks/&gt;`_  Types
==================================================================

The Python classes enumerated below provide an interpretation of GridWorks
type instances (serialized JSON) as Python objects. Types are the building
blocks for GridWorks APIs. You can read more about how they work
`here &lt;api-sdk-abi.html&gt;`_, and examine their API specifications `here &lt;apis/types.html&gt;`_.
The Python classes below also come with methods for translating back and
forth between type instances and Python objects.


.. automodule:: gridworks.types

.. toctree::
   :maxdepth: 1
   :caption: TYPE SDKS

    </xsl:text>
<xsl:for-each select="$airtable//ProtocolTypes/ProtocolType[(normalize-space(ProtocolName) ='gridworks')]">
<xsl:sort select="TypeName" data-type="text"/>
<xsl:variable name="type-id" select="Type"/>
<xsl:for-each select="$airtable//Types/Type[(TypeId = $type-id)  and (Status = 'Active' or Status = 'Pending') and (ProtocolCategory = 'Json' or ProtocolCategory = 'GwAlgoSerial')]">
<xsl:call-template name="nt-case">
    <xsl:with-param name="type-name-text" select="TypeNameRoot" />
</xsl:call-template>
<xsl:text>  &lt;types/</xsl:text>
<xsl:value-of select="translate(TypeNameRoot,'.','-')"/>
<xsl:text>&gt;
    </xsl:text>

</xsl:for-each>
</xsl:for-each>

                </xsl:element>
            </FileSetFile>


        </FileSet>
    </xsl:template>


</xsl:stylesheet>
