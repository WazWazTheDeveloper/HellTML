# HellTML
Ever wondered how to transform your frontend development into a never-ending nightmare?

Introducing my brainchild: "HellTML"! It's a frontend framework that gleefully crams all your HTML and CSS into a YAML file, where indentation errors and misplaced colons reign supreme. Forget about the joys of live reloading or intuitive debugging— with "HellTML", you'll be diving headfirst into a labyrinth of indents gone wild and inexplicable syntax errors. Embrace the chaos and discover a whole new level of frontend development frustration!

<!-- Have you ever thought how could you achive the worst development experience writing frontend?

Well, I did and I gladly want to present you my abomination: `HellTML` a frontend framework that moves all your html and css into a YAML file! -->

## How to use
first you will need to install HellTML:

`> pip install helltml`

and the only command you will need is:

`> python -m helltml --filename=your_yaml_file.yml`

## YAML file format:

### HTML

Each key under the html key represents either an attribute or an element within an HTML document.

for example:

```YAML
pages:
    example_1:
        html:
            head:
                children:
                    title:
                        children_text: "example"
            body:
                children:
                    div:
                        class: "example_class"
```
Explanation:

* Keys such as `head`, `body`, `div`, and `title` correspond to specific HTML tags.

* The `children` key signifies the nested elements or content within each HTML tag.

* The `children_text` key is used to specify plain text content within an element.

* Attributes like `class` denote standard attributes that can be applied to html tags.

and after building we should get the following html file:
```html
<html>
    <head>
        <title>example</title>
    </head>
    <body>
        <div class="example_class"></div>
    </body>
</html>
```

### CSS

Each key under the css key represents a class and its attributes


for example:
```YAML
pages:
    your_page_1:
        html:
        ...
        css:
            "*":
              margin: 0

            body:
                display: flex

            "@media (max-width: 900px)" :
                children: 
                  section span:
                    width: "calc(10vw - 2px)"
                    height: "calc(10vw - 2px)"
```
Explanation:
* Keys such as `"*"`, `"@media (max-width: 900px)"`, `section span`, and `body` represent class selectors in a CSS file.

* The `children`  key indicates nested classes or elements within the respective CSS selectors.

* any other attributes like `margin`, and `display` correspond to standard  css properties.

## Example
open the `examples/login page` folder

run the following command:

`> python -m helltml --filename="login_page.yml"`

now you should see a new directory `outdir/login_page` with a files inside named `login_page.css` and `login_page.html`