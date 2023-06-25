<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl" xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xsl:output method="xml" indent="yes" />
    <xsl:param name="root" />
    <xsl:param name="codee-root" />
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
                        <xsl:element name="RelativePath"><xsl:text>../../../../rabbit/rabbitconfig/rabbit_definitions_hybrid.json</xsl:text></xsl:element>
                        <OverwriteMode>Always</OverwriteMode>
                        <xsl:element name="FileContents">
                        <xsl:text>{
    "vhosts":[
        {
            "name":"hw1__1"
        }
    ],
    "permissions":[
        {
            "user":"smqPublic",
            "vhost":"hw1__1",
            "configure":".*",
            "write":".*",
            "read":".*"
        }
    ],
    "exchanges":[</xsl:text>
    <xsl:for-each select="$airtable//RabbitExchangeRoles/RabbitExchangeRole">
        <xsl:sort select="Name" data-type="text"/>
    <xsl:text>
        {
            "name":"</xsl:text><xsl:value-of select="Name"/>
            <xsl:text>mic_tx",
            "vhost":"hw1__1",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":false,
            "arguments":{}
         },
        {
            "name":"</xsl:text><xsl:value-of select="Name"/><xsl:text>_tx",
            "vhost":"hw1__1",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":true,
            "arguments":{}
        },</xsl:text>
    </xsl:for-each>
         <xsl:text>
        {
            "name":"ear_tx",
            "vhost":"hw1__1",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":true,
            "arguments":{}
        }
    ],
    "bindings":[
    {
        "source":"amq.topic",
        "vhost":"hw1__1",
        "destination":"ear_tx",
        "destination_type":"exchange",
        "routing_key":"#",
        "arguments":{}
    }</xsl:text>
    <xsl:for-each select="$airtable//RabbitPairings/RabbitPairing">
        <xsl:sort select="From" data-type="text"/>
        <xsl:sort select="To" data-type="text"/>
        <xsl:text>,
    {
        "source":"</xsl:text><xsl:value-of select="From"/><xsl:text>mic_tx",
        "vhost":"hw1__1",
        "destination":"</xsl:text><xsl:value-of select="To"/><xsl:text>_tx",
        "destination_type":"exchange",
        "routing_key":"*.*.</xsl:text><xsl:value-of select="From"/>
        <xsl:text>.*.</xsl:text>
        <xsl:value-of select="To"/><xsl:text>.*",
        "arguments":{}
    }</xsl:text>
    </xsl:for-each>
    <xsl:for-each select="$airtable//RabbitExchangeRoles/RabbitExchangeRole">
    <xsl:sort select="Name" data-type="text"/>
          <xsl:text>,
    {
        "source":"</xsl:text><xsl:value-of select="Name"/><xsl:text>mic_tx",
        "vhost":"hw1__1",
        "destination":"ear_tx",
        "destination_type":"exchange",
        "routing_key":"#",
        "arguments":{}
    }</xsl:text>
    </xsl:for-each>
    <xsl:text>
    ]
}
</xsl:text>
                    </xsl:element>
                    </FileSetFile>
        </FileSet>
    </xsl:template>
</xsl:stylesheet>
