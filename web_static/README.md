# 0x01. AirBnB clone - Web static

## Description
What you should learn from this project:

* What is HTML
* How to create an HTML page
* What is a markup language
* What is the DOM
* What is an element / tag
* What is an attribute
* How does the browser load a webpage
* What is CSS
* How to add style to an element
* What is a class
* What is a selector
* How to compute CSS Specificity Value
* What are Box properties in CSS

---

### [0. Inline styling](./0-index.html)
Write an HTML page that displays a header and a footer.

Layout:

* Body:
no margin
no padding
* Header:
color #FF0000 (red)
height: 70px
width: 100%
* Footer:
color #00FF00 (green)
height: 60px
width: 100%
text `Holberton School` center vertically and horizontally
always at the bottom at the page
Requirements:

* You must use the `header` and `footer` tags
* You are not allowed to import any files
* You are not allowed to use the `style` tag in the `head` tag
* Use inline styling for all your tags
![0 example output](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/0-index.png)


### [1. Head styling](./1-index.html)
Write an HTML page that displays a header and a footer by using the `style` tag in the `head` tag (same as `0-index.html`)

Requirements:

* You must use the `header` and `footer` tags
* You are not allowed to import any files
* No inline styling
* You must use the `style` tag in the `head` tag
* The layout must be exactly the same as `0-index.html`


### [2. CSS files](./2-index.html)
Write an HTML page that displays a header and a footer by using CSS files (same as `1-index.html`)

Requirements:

* You must use the `header` and `footer` tags
* No inline styling
* You must have 3 CSS files:
	* `styles/2-common.css`: for global style (i.e. the `body` style)
	* `styles/2-header.css`: for header style
	* `styles/2-footer.css`: for footer style
The layout must be exactly the same as `1-index.html`


### [3. Zoning done!](./3-index.html)
Write an HTML page that displays a header and footer by using CSS files (same as `2-index.html`)

Layout:

* Common:
	* no margin
	* no padding
	* font color: #484848
	* font size" 14px
	* font family: `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;`
	* [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png) in the browser tab
* Header:
	* color: white
	* height: 70px
	* width: 100%
	* border bottom 1px #CCCCCC
	* [logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png) align on left and center vertically (20px space at the left)
* Footer:
	* color white
	* height: 60px
	* width: 100%
	* border top 1px #CCCCCC
	* text `Holberton School` center vertically and horizontally
	* always at the bottom at the page
Requirements:

* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 3 CSS files:
	* `styles/3-common.css`: for the global style (i.e `body` style)
	* `styles/3-header.css`: for the header style
	* `styles/3-footer.css`: for the footer style
![3 example output](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/3-index.png)


### [4. Search!](./4-index.html)
Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on `3-index.html`)

* Container:
	* between `header` and `footer` tags, add a `div`:
		* classname: `container`
		* max width 1000px
		* margin top and bottom 30px - it should be 30px under the bottom of the `header` (screenshot)
		* center horizontally
* Filter section:
	* tag `section`
	* classname `filters`
	* inside the `.container`
	* color white
	* height: 70px
	* width: 100% of the container
	* border 1px #DDDDDD with radius 4px
* Button search:
	* tag `button`
	* text `Search`
	* font size: 18px
	* inside the section filters
	* background color #FF5A5F
	* text color #FFFFFF
	* height: 48px
	* width: 20% of the section filters
	* no borders
	* border radius: 4px
	* center vertically and at 30px of the right border
	* change opacity to 90% when the mouse is on the button
Requirements:

* You must use: `header`, `footer`, `section`, `button` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 4 CSS files:
	* `styles/4-common.css`: for the global style (`body` and `.container` styles)
	* `styles/3-header.css`: for the header style
	* `styles/3-footer.css`: for the footer style
	* `styles/4-filters.css`: for the filters style
* `4-index.html` __won’t be W3C valid__, don’t worry, it’s temporary
![4 example output](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/4-index.png)


### [5. More filters](./5-index.html)
Write an HTML page that displays a header, footer and a filters box.

Layout: (based on `4-index.html`)

* Locations and Amenities filters:
	* tag: `div`
	* classname: `locations` for location tag and `amenities` for the other
	* inside the section filters (same level as the `button` Search)
	* height: 100% of the section filters
	* width: 25% of the section filters
	* border right #DDDDDD 1px only for the first left filter
	* contains a title:
		* tag: `h3`
		* font weight: 600
		* text `States` or `Amenities`
	* contains a subtitle:
		* tag: `h4`
		* font weight: 400
		* font size: 14px
		* text with fake contents
Requirements:

* You must use: `header`, `footer`, `section`, `button`, `h3`, `h4` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 4 CSS files:
	* `styles/4-common.css`: for the global style (`body` and `.container` styles)
	* `styles/3-header.css`: for the header style
	* `styles/3-footer.css`: for the footer style
	* `styles/5-filters.css`: for the filters style
![5 example output](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/5-index.png)


### [6. It's (h)over](./6-index.html)
* Write an HTML page that displays a header, footer and a filters box with dropdown.


### [7. Display results](./7-index.html)
* Write an HTML page that displays a header, footer, a filters box with dropdown and results.


### [8. More details](./8-index.html)
* Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.


### [9. Full details](./100-index.html)
* Write an HTML page that displays a header, footer, a filters box with dropdown and results.


### [10. Flex](./101-index.html)
* Improve the Places section by using Flexible boxes for all Place articles


### [11. Responsive design](./102-index.html)
* Improve the page by adding responsive design to display correctly in mobile or small screens.


### [12. Accessibility](./103-index.html)
* Improve the page by adding Accessibility support

---

## Author
* **Tim Assavarat** - [tassavarat](https://github.com/tassavarat)
