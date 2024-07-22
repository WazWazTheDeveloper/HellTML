import json

class CSSParser:
    def __init__(self):
        self.css = ""

    def createCSSFile(self, CSSData):
        self.css = ""

        for key in CSSData.keys():
            self.createObject(key,CSSData[key])
        return self.css

    def createObject(self, cssObjectQuerry: str, classData: json):
        self.css += f"{cssObjectQuerry}"
        self.css += "{"
        for key in classData.keys():
            if(key == "children"):
                for key2 in classData["children"].keys():
                    self.createObject(key2,classData["children"][key2])
                continue
            self.css += f"{key}:{classData[key]};"
        self.css += "}"
        return
