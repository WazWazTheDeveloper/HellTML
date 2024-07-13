import json

_specialAttrs = ["children", "children_text"]
_elementWithNoClosing = ["meta"]


class HTMLParser:
    def __init__(self):
        self.page = ""
        self.tabCount = 0

    def createPage(self, pageData: json):
        if ("html" not in pageData.keys()):
            return
        self.page += f"<!DOCTYPE html>"
        self.page += f"<html>"
        self.tabCount += 1

        if ("head" in pageData["html"].keys()):
            self.page += f"<head>"
            self.tabCount += 1
            for key in pageData["html"]["head"].keys():
                self.addElement(key, pageData["html"]["head"][key])
            self.tabCount -= 1
            self.page += f"</head>"

        if ("body" in pageData["html"].keys()):
            self.page += f"<body>"
            self.tabCount += 1
            for key in pageData["html"]["body"].keys():
                self.addElement(key, pageData["html"]["body"][key])
            self.tabCount -= 1
            self.page += f"</body>"

        self.page += f"</html>"
        return self.page

    def addElement(self, elementKey: str, elementAttr: json):
        cutIndex = elementKey.find('&')
        if (cutIndex != -1):
            elementKey = elementKey[:cutIndex]
        self.page += f"<{elementKey}"
        self.addAttrs(elementAttr)
        self.page += ">"

        if (elementAttr is not None):
            for key in elementAttr:
                if (key == "children_text"):
                    self.page += elementAttr[key]
                if (key == "children"):
                    for elementKey_1 in elementAttr[key]:
                        self.addElement(
                            elementKey_1, elementAttr["children"][elementKey_1])

        if (elementKey not in _elementWithNoClosing):
            self.page += f"</{elementKey}>"
        return

    def addAttrs(self, elementAttr: json):
        if (elementAttr is None):
            return
        for key in elementAttr.keys():
            if (key in _specialAttrs):
                continue
            self.page += f' {key}="{elementAttr[key]}"'

        return

    def getTabs(self):
        return "\t" * self.tabCount
