Bookylst is a web app used to store a user's book information. The main webpage features a list of books entered by the user and information regarding them. Each book has it's own separate page which shows further details like 3 sentences and highlights of the book. It also features a "Read Later" webpage which can be used to list any book the user may want to read in the future. The web app uses Google Books API and it's database to retrieve information. This is a project built for personal use.

[insert screenshot of website here]

Booklyst is hosted on [PythonAnywhere](https://www.pythonanywhere.com) and is live on https://dcsp3.pythonanywhere.com. Please note that it is not mobile compatible.

# Features

## My Books
This is the homepage of the website and displays all the books added by the user in a list. It shows the cover page, title, author, rating, date finished and genre for each book. It also has a remove button for each book which deletes it from the database.

## Read Later 
This webpage displays all the books added to "Read Later" by the user. It displays the cover page, title, author and summary of the book. It also has a remove button for each book which deletes it from the database. 

## Individual Book Pages
Each book in "My Books" has a separate page (identified by the book id) which shows all information about the book from the homepage and the 3 sentences and highlights given by the user. It also has an edit button to make any changes to the information.


# How It Works
## Adding a book to "My Books"
To add a book to the list of read books, the user has to click on the "Add Book" button at the bottom of the home webpage. This leads to a new page with a form. The user has to input the title, rating, date finished, 3 sentences (or 3 major learnings) and highlights from the book. On clicking submit, the title of the book is used as the search term for the Google Books API to retrieve the cover, title and author of the book. This is then saved in the database and displayed on the "My Books" webpage.

## Adding a book to "Read Later"
To add a book to the list of unread books, the user has to click on the "Add Book" button at the bottom of the read later webpage. This leads to a new page with a form that only has a 'title' field. On clicking submit, the title of the book is used as a search term for the Google Books API to retrieve the cover, title, author and the summary of the book. This is then saved in the database and displayed on the "Read Later" webpage.
 

# Installation
Since django files are automatically generated and individual to each web app, a possible method to replicate this project is to create an app using the [documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial01/) and copy-pasting the python, html and css files.

# Technologies Used
1. [Django](https://www.djangoproject.com/): Web framework
2. [Google Books API](https://developers.google.com/books/):  Retrieving book information


# Attributions
- Logo icon designed by [Smashicons](https://www.flaticon.com/authors/smashicons) from www.flaticon.com
- Logo text by [calligraphyfonts.net](https://www.fontspace.com/good-memories-font-f71165) from www.fontspace.com
