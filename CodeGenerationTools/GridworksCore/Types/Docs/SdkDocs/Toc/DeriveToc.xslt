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
SDK for Gridworks Types
=======================

Types are the building blocks for GridWorks APIs: they articulate
*what* is getting sent without specifying the *where* (i.e.,
a Restful API endpoint, or a queue in a rabbit broker) or *how* (i.e.,
specifying that a Restful POST requires *this* type, or returns *that* type).

As you are learning, you can assume that all Gridworks types are serialized JSON.
Json is the lingua franca of APIs. It is not a programming language,
it is more like a multi-dimensional graph structure.

The API specs for these GridWorks types is `here &lt;apis/types.html&gt;`_. The Python Type
SDKs provide a Pythonic method of creating valid instances of these types, and for
interpretting payloads as  natural Python objects.

You will notice massive overlap in the API specs and the SDK documentation for types.
Why is that?

Imagine the actors in GridWorks as cells in an organism. They have ways of communicating,
and this is captured in their cell membranes. An actor's APIs specify how it communicates
at and beyond its cell membranes. An SDK, in contrast,  is like an internal organelle
capable of generating valid messages to be sent out of the membrane.

The Purpose of This SDK
^^^^^^^^^^^^^^^^^^^^^^^^
This SDK, paired with its `API &lt;apis/types.html&gt;`_, is part of a Gridworks tutorial
application designed to teach the basic mechanics of communication in GridWorks.
Go `here &lt;api-sdk-abi.html&gt;`_ for instructions.

.. automodule:: gridworks.types

.. toctree::
   :maxdepth: 1
   :caption: TYPE SDKS

    </xsl:text>
<xsl:for-each select="$airtable//ProtocolTypes/ProtocolType[(normalize-space(ProtocolName) ='gridworks')]">
<xsl:sort select="TypeName" data-type="text"/>
<xsl:variable name="schema-id" select="Type"/>
<xsl:for-each select="$airtable//Schemas/Schema[(SchemaId = $schema-id)  and (Status = 'Active' or Status = 'Pending') and (ProtocolCategory = 'Json' or ProtocolCategory = 'GwAlgoSerial')]">
<xsl:variable name="local-alias" select="AliasRoot" />
<xsl:call-template name="nt-case">
    <xsl:with-param name="mp-schema-text" select="AliasRoot" />
</xsl:call-template>
<xsl:text>  &lt;types/</xsl:text>
<xsl:value-of select="translate(AliasRoot,'.','-')"/>
<xsl:text>&gt;
    </xsl:text>

</xsl:for-each>
</xsl:for-each>

                </xsl:element>
            </FileSetFile>


        </FileSet>
    </xsl:template>


</xsl:stylesheet>
