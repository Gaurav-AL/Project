<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<!-- <xsl:output method="html" encoding="UTF-8"/> -->
<xsl:template match="/">
<html>
<body>
<head>
<title>Food Menu</title>
</head>
<h3>Food Menu</h3>
<table border="3">
    <tr >
    <th>S.NO</th>
    <th>Food Name</th>
    <th>Day</th>
    <th>Price</th>
    </tr>
    <xsl:for-each select="menu/food">
    <tr>
    <td><xsl:value-of select="sno"/></td>
    <td><xsl:value-of select="foodname"/></td>
    <td><xsl:value-of select="day"/></td>
    <td><xsl:value-of select="price"/></td>  
    </tr>
    </xsl:for-each>

</table>
    
</body>
</html>
</xsl:template>
</xsl:stylesheet>