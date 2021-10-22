import os
from flask import Flask
app = Flask(__name__)

videos = {}
videosByHash = {}

@app.route('/')
def index():
    generateVideos()
    return basicTemplate(generateUl())


@app.route('/videos/<n>', methods=['GET'])
def getVideo(n):
    print(n)
    frame = f'''
                <video width="1080" controls>
                    <source src="/static/{videosByHash[int(n)]}" type="video/mp4">
                </video>
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
    for key in videos:
        links += f'<li><a href="/videos/{videos[key]}">{key}</a></li>\n'
    return '<ul>\n' + links + '</ul>\n'


def generateVideos():
    global videos
    global videosByHash
    i = 0
    for file in os.listdir('static'):
        if file.endswith('.mp4'):
            videos[file] = i
            videosByHash[i] = file
            i += 1

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
