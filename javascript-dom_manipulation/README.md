# JavaScript - DOM Manipulation

## Description

This project is a series of exercises focused on manipulating the DOM (Document Object Model) using JavaScript. It covers selecting HTML elements, listening to user events, dynamically updating content and styles, and fetching data from external APIs using the Fetch API and Promises.

## Learning Objectives

By the end of this project, you should be able to explain, without Google:

* How to select HTML elements in JavaScript
* How to manipulate the "class" list of an HTML element
* How to listen/bind to events on an HTML tag
* How to manipulate the DOM by using JavaScript
* How to make a `GET` request with Fetch API
* How to use a Promise
* How to update the content of an HTML tag by using JavaScript

## Requirements

* All files are interpreted/compiled on Ubuntu 20.04 LTS using the latest version of a browser (Chrome/Firefox)
* All files should end with a new line
* A `README.md` file at the root of the project folder is mandatory
* Your code should use the `.js` extension
* Files are tested using JavaScript standard style guidelines

## How to Test

Each task comes with a corresponding `X-main.html` file used for testing. Because some tasks use the Fetch API to request external resources, the files should be served through a local HTTP server rather than opened directly (`file://`), to avoid CORS restrictions.

```bash
python3 -m http.server 8000
```

Then open the relevant file in your browser, for example:

```
http://localhost:8000/0-main.html
```

## Tasks

| Task | File | Description |
| ---- | ---- | ----------- |
| 0 | `0-script.js` | Updates the text color of the `header` element to red using `querySelector` |
| 1 | `1-script.js` | Updates the text color of the `header` element to red when the user clicks on the element with id `red_header` |
| 2 | `2-script.js` | Adds the class `red` to the `header` element when the user clicks on the element with id `red_header` |
| 3 | `3-script.js` | Toggles the `header` element's class between `red` and `green` when the user clicks on the element with id `toggle_header` |
| 4 | `4-script.js` | Adds a new `<li>Item</li>` to the `ul` element with class `my_list` when the user clicks on the element with id `add_item` |
| 5 | `5-script.js` | Updates the text of the `header` element to `New Header!!!` when the user clicks on the element with id `update_header` |
| 6 | `6-script.js` | Fetches a Star Wars character's name from the SWAPI API and displays it in the element with id `character` |
| 7 | `7-script.js` | Fetches all Star Wars movie titles from the SWAPI API and lists them in the `ul` element with id `list_movies` |
| 8 | `8-script.js` | Fetches a translated "hello" greeting and displays it in the element with id `hello`, working even when loaded from the `<head>` tag |

## Repository

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-dom_manipulation`

## Author

Dhay Aldhwayan
