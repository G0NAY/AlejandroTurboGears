<%inherit file="local:templates.master"/>

<HTML>
    <HEAD>
    <TITLE>Weather</TITLE>
    </HEAD>
    <BODY BGCOLOR="FFFFFF">
        <CENTER><IMG SRC="https://goldentroutwilderness.files.wordpress.com/2012/01/various-weather.jpg" height="220" width="220" ALIGN="BOTTOM"> </CENTER>
        <HR>
        <H1>State of Mexico's Weather</H1>
        <p>Temperature: ${temperature} Celcius</p>
        <p>Pressure: ${pressure} Mb </p>
        <p>Humidity: ${humidity} %</p>
    </BODY>
</HTML>