# Section 3: The Web Scraping process


## 05. The Webscraping process

1. obtain web URL and download the web page
  + use the python requests library
  + obtain the source code

2. parse the downloaded data into a parser to get data in a readable & structured format
  + HTML parser
  + BeautifulSoup library to extract the data that we need

3. save data
  + build a Pandas dataframe
  + store as CSV, JSON, or SQL database



## 06. What to know first

1. Request library

2. HTML


## 07. Requests library

+ Requests: a python library
+ download the source code
  + page text or contents
  + from the target web page
+ first determining the URL of the web page to be scraped
+ using a request method call `get`
+ the `get` method performing a `GET` request


## 08. requests.get() method

+ using a web browser (chrome or explorer)

+ visit a we page

+ web browser makes a `GET` request to tge web server

+ web server: the web page data/files stored

+ returns the files after a `GET` request

+ browser renders the web page files for humans to be able to read

+ files in different forms: HTML, CSS, & JavaScript


## 09. Introduction to HTML

+ HTML: a markup language rather than a programming language

+ the standard markup language for structuring and formatting web page

+ like MS Word format by using MS Word to structure the content on the page and format it, e.g., font size, color, etc.

+ using HTML formatting & structuring made possible by using tags
  + tags: angled brackets `< >`

+ HTML not a programming language


## 10. HTML tags

+ `<p>`: paragraph
+ `<table>`: table
+ `<tr>`: table rows
+ `<th>`: table headers
+ `<td>`: table columns
+ `<tbody>`: table body
+ `<col>`: column properties
+ `<div>`: division/section within a document
+ `<!DOCTYPE>`: HTML document
+ `<html>`: HTML document
+ `<head>`: metadata for the document
+ `<title>` title for the document
+ `<a>`: hyperlink
+ `<img>`: image
+ `<h1>`: HTML heading
+ `<br>`: line break



## 11. Inspection

+ Demo: list of "Game of Thrones" episodes

+ using right click + `inspect` to view HTML source file


## 12. Introduction to Beautiful Soup





