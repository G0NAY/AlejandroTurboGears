<%inherit file="local:templates.master"/>


<HTML>
    <HEAD>
    <TITLE>DatosWeather</TITLE>
    </HEAD>
    <BODY BGCOLOR="FFFFFF">
        <CENTER>

            <ul>
                % for key, value in json.items():
                    <p>${key},${value}</p>
                         %if key == "sys":
                                %for key1, value1 in json[key].items():
                                <h3>${key1},${value1}</h3>
                                %endfor
                         %endif

                %endfor

            </ul>


            <h1>${json['name']}</h1>
            <p></p>

        <H1>State of Mexico's Weather</H1>
        </CENTER>
    </BODY>
</HTML>