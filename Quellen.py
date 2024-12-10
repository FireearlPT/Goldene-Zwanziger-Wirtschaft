with open("Quellen.txt","rb") as f:
    Sources = f.read().decode("utf-8").replace("\r","").split("\n")
Sources_Dict = {}
Short_Sources = []
for source in Sources:
    Sources_Dict.update({source.replace("http://","").replace("https://",""):source})
    Short_Sources.append(source.replace("http://","").replace("https://",""))
Short_Sources.sort()
Sources = []
for source in Short_Sources:
    Sources.append(Sources_Dict[source])
#print(Sources)
output = ""
for source in Sources:
    output += """        <a href=""" + source + """>
            """ + source + """; 11.12.2024
        </a>
        <br>"""
print(output)
input()