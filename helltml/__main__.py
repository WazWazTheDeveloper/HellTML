import typer
import yaml
from helltml.html_parser import HTMLParser
from helltml.css_parser import CSSParser
import os

app = typer.Typer()
htmlParser = HTMLParser()
cssParser = CSSParser()

@app.command()
def build(filename: str = "hell.yml", outdir: str = "outdir"):
    with open(filename, 'r') as file:
        yml_file = yaml.safe_load(file)
    if ("pages" not in yml_file.keys()):
        print("error")
        return

    for pageKey in yml_file["pages"].keys():
        page = yml_file["pages"][pageKey]

        folder_path = f"./{outdir}/{pageKey}"
        if (not os.path.exists(folder_path)):
            os.makedirs(folder_path)

        if ("html" in page.keys()):
            html_file = open(f"{folder_path}/{pageKey}.html", 'w')
            html_file.write(htmlParser.createPage(page["html"]))
        if ("css" in page.keys()):
            css_file = open(f"{folder_path}/{pageKey}.css", 'w')
            css_file.write(cssParser.createCSSFile(page["css"]))
    return


if __name__ == "__main__":
    app()
