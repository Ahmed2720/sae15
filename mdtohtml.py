import markdown

def convert():
    with open('file.md', 'r') as f:
        text = f.read()

    html = markdown.markdown(text)
    
    with open('file.html', 'w') as f:
        f.write(html)