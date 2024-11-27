from flask import Flask, render_template, g, redirect, request

app = Flask(__name__)

# 404 Error handling and redirecting
@app.errorhandler(404)
def page_not_found(_error):
   return redirect('/')

# Seach query to show possible results and matches in paragrpahs.
def chapters_matching(query, contents):
    if not query:
        return []

    results = []
    for index, name in enumerate(contents, start=1):
        with open(f"book_viewer/data/chp{index}.txt", "r") as file:
            chapter_content = file.read()
        
        matches = {}
        for para_index, paragraph in enumerate(chapter_content.split("\n\n")):
            if query.lower() in paragraph.lower():
                matches[para_index] = paragraph
            
        # Add chapter only if there are matches
        if matches:
            results.append({'number': index, 'name': name, 'paragraphs': matches})

    return results

# hightlight matches
def highlight(text, term):
    return text.replace(term, f'<strong>{term}</strong>')

# Define the filter
def in_paragraphs(text):
    paragraphs = text.split("\n\n")
    formatted_paragraphs = [
        f'<p>{paragraph}</p>'
        for paragraph in paragraphs
        if paragraph
    ]
    return ''.join(formatted_paragraphs)

# Register all the filters with the app
app.jinja_env.filters['in_paragraphs'] = in_paragraphs
app.jinja_env.filters['highlight'] = highlight


# load and read the table of content first
@app.before_request
def load_contents():
    with open("book_viewer/data/toc.txt", "r") as file:
        g.contents = file.readlines()

# Homepage route for the table of contents
@app.route("/")
def index():
    return render_template('home.html', contents=g.contents)

# Route for Chapters
@app.route("/chapters/<page_num>")
def chapter(page_num):

    # ensure the page number is within the available page range
    if page_num.isdigit() and (1 <= int(page_num) <= len(g.contents)):

        # Get the chapter name and title
        chapter_name = g.contents[int(page_num) - 1]
        title = f"Chapter {page_num}: {chapter_name}"

        # Read Chapter 1 content
        with open(f"book_viewer/data/chp{page_num}.txt") as file:
            chapter_content = file.read()
        
        return render_template('chapter.html',
                            chapter_title=title,
                            title=title,
                            chapter=chapter_content,
                            contents=g.contents)
    else:
        return redirect('/')

# Route to search data in the application
@app.route("/search")
def search():
    query = request.args.get('query', '')
    results = chapters_matching(query, g.contents) if query else []
    return render_template('search.html',
                            query=query, 
                           results=results, 
                           contents=g.contents)

if __name__ == "__main__":
    app.run(debug=True, port=5003)
