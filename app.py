import os
from flask import Flask
app = Flask(__name__)

files = {}
filesByHash = {}

@app.route('/')
def index():
    generateVideos()
    return basicTemplate(generateUl())


@app.route('/videos/<n>', methods=['GET'])
def getVideo(n):
    frame = f'''
                <video controls>
                    <source src="/static/{filesByHash[int(n)]}" type="video/mp4">
                </video>
                <br>
                <a href="/static/{filesByHash[int(n)]}" download>Download {filesByHash[int(n)]}</a>
    '''
    return basicTemplate(frame)


def basicTemplate(var):
    html = f'''
        <!doctype html>
        <html>
            <head>
                <title>Video</title>
            </head>
            <body>
            {var}
            </body>
        </html>
    '''
    return html

def generateUl():
    links = ''
    for key in files:
        if key.endswith('mp4'):
            links += f'<li><a href="/videos/{files[key]}">{key}</a></li>\n'
        else:
            links += f'<li><a href="/static/{key}" download>Download</a> {key}</li>\n'
    return f'<ul>{links}</ul>'


def generateVideos():
    # Use a two way dict of names to ints for URLs.
    global files
    global filesByHash
    i = 0
    for file in os.listdir('static'):
        files[file] = i
        filesByHash[i] = file
        i += 1

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
