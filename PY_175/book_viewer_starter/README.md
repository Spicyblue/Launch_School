# Book Viewer Web Application

This Flask-based application allows users to browse and search through the chapters of The Adventures of Sherlock Holmes by Sir Arthur Conan Doyle. The app provides an interactive interface for displaying the table of contents, viewing chapters, and searching for specific text within chapters.

## Features

**Table of Contents**: Displays a list of chapters for easy navigation.  

**Chapter Viewer**: View individual chapters formatted with paragraphs.  

**Search Functionality**: Allows users to search for text across all chapters and view results by paragraph.  

**Dynamic Links**: Each search result links to the specific chapter and highlights the relevant paragraph.  

**Error Handling**:
Redirects users to the homepage for invalid routes.

### Installation

1. Clone this repository:

    ```console
    git clone https://github.com/Spicyblue/Launch_School/tree/fedb3c2883b9760a9fb64f087ad31f1b5e53474b/PY_175/book_viewer_starter
    cd book-viewer
    ```

2. Install Dependencies:  
    Necessary dependencies includes Poetry, Flasks and Python(Version 3.9 and above) The application was developed using python3.12

    To install Poerty, first install pipx and then poetry by using the following command on your commandline interface

    ```console
    pip install pipx
    pipx install poetry
    ```

    To install flask, use the following command on your commandline interface:

    ```console
    poetry add flask
    ```

3. Set up the file structure:

    app.py: Main flask application
    book_viewer/data/toc.txt: Contains the table of contents (one chapter per line).
    book_viewer/data/chpX.txt: Contains the content of chapters (e.g., chp1.txt, chp2.txt).
    book_viewer/templates/: Contains all necessary HTML templates.
    book_viewer/static/: Contains all static files.

4. Run the application

    To run the application, ensure you are in the directory for book_viewer containing app.py
    Next, run the following code on your commandline interface.

    ```console
    poetry run python app.py
    ````

    Open your application in your broswer by entering the address below:
    http://localhost:5003

### Future Enhancements

- Add paragraph highlighting for search results.
- Improve UI/UX with modern styling.
- Add pagination for long chapters.

### License

This project is open-source and licensed under the MIT License. Feel free to use and adapt it for your own projects. See License.md for more infomation about the license
