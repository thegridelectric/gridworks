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
                        <xsl:element name="RelativePath"><xsl:text>../../../../rabbit/rabbitconfig/rabbit_definitions_dev.json</xsl:text></xsl:element>
                        <OverwriteMode>Always</OverwriteMode>
                        <xsl:element name="FileContents">
                        <xsl:text>{
    "vhosts":[
        {
            "name":"d1__1"
        },
        {
            "name":"dev_registry"
        }
    ],
    "permissions":[
        {
            "user":"smqPublic",
            "vhost":"d1__1",
            "configure":".*",
            "write":".*",
            "read":".*"
        },
        {
            "user":"smqPublic",
            "vhost":"dev_registry",
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
            "vhost":"d1__1",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":false,
            "arguments":{}
         },
        {
            "name":"</xsl:text><xsl:value-of select="Name"/><xsl:text>_tx",
            "vhost":"d1__1",
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
            "vhost":"d1__1",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":true,
            "arguments":{}
        },
        {
            "name":"gnfmic_tx",
            "vhost":"dev_registry",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":false,
            "arguments":{}
         },
        {
            "name":"gnf_tx",
            "vhost":"dev_registry",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":true,
            "arguments":{}
        },
        {
            "name":"gnrmic_tx",
            "vhost":"dev_registry",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":false,
            "arguments":{}
         },
        {
            "name":"gnr_tx",
            "vhost":"dev_registry",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":true,
            "arguments":{}
        },
        {
            "name":"worldmic_tx",
            "vhost":"dev_registry",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":false,
            "arguments":{}
        },
        {
            "name":"world_tx",
            "vhost":"dev_registry",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":true,
            "arguments":{}
        },
        {
            "name":"ear_tx",
            "vhost":"dev_registry",
            "type":"topic",
            "durable":true,
            "auto_delete":false,
            "internal":true,
            "arguments":{}
        }
    ],
    "queues": [
        {
        "name": "dummy_ear_q",
        "vhost": "d1__1",
        "durable": true,
        "auto_delete": false,
        "arguments": {}
       },
       {
        "name": "dummy_registry_ear_q",
        "vhost": "dev_registry",
        "durable": true,
        "auto_delete": false,
        "arguments": {}
       }
    ],
    "bindings":[
    {
        "source":"amq.topic",
        "vhost":"d1__1",
        "destination":"ear_tx",
        "destination_type":"exchange",
        "routing_key":"#",
        "arguments":{}
    },
    {
        "source":"ear_tx",
        "vhost":"d1__1",
        "destination":"dummy_ear_q",
        "destination_type":"queue",
        "routing_key":"#",
        "arguments":{}
    },
    {
        "source":"ear_tx",
        "vhost":"dev_registry",
        "destination":"dummy_registry_ear_q",
        "destination_type":"queue",
        "routing_key":"#",
        "arguments":{}
    }</xsl:text>
    <xsl:for-each select="$airtable//RabbitPairings/RabbitPairing">
        <xsl:sort select="From" data-type="text"/>
        <xsl:sort select="To" data-type="text"/>
        <xsl:text>,
    {
        "source":"</xsl:text><xsl:value-of select="From"/><xsl:text>mic_tx",
        "vhost":"d1__1",
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
        "vhost":"d1__1",
        "destination":"ear_tx",
        "destination_type":"exchange",
        "routing_key":"#",
        "arguments":{}
    }</xsl:text>
    </xsl:for-each>
    <xsl:text>,

    {
        "source":"gnfmic_tx",
        "vhost":"dev_registry",
        "destination":"gnr_tx",
        "destination_type":"exchange",
        "routing_key":"*.*.gnf.*.gnr.*",
        "arguments":{}
    },
    {
        "source":"gnrmic_tx",
        "vhost":"dev_registry",
        "destination":"world_tx",
        "destination_type":"exchange",
        "routing_key":"*.*.gnr.*.world.*",
        "arguments":{}
    },
    {
        "source":"gnfmic_tx",
        "vhost":"dev_registry",
        "destination":"ear_tx",
        "destination_type":"exchange",
        "routing_key":"#",
        "arguments":{}
    },
    {
        "source":"gnrmic_tx",
        "vhost":"dev_registry",
        "destination":"ear_tx",
        "destination_type":"exchange",
        "routing_key":"#",
        "arguments":{}
    }
    ]
}
</xsl:text>
                    </xsl:element>
                    </FileSetFile>
        </FileSet>
    </xsl:template>
</xsl:stylesheet>
