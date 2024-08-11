from flask import Flask, request, render_template, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from themes import *
from style import *
app = Flask(__name__)

def get_youtube_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    else:
        return None

def fetch_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en'])
        formatter = TextFormatter()
        text_formatted = formatter.format_transcript(transcript.fetch())
        return text_formatted
    except Exception as e:
        return str(e)

def get_blog(doc_content, template='editoral', author='Anonymous', style = 'default', youtube_url=""):
    response_str = generate_content(doc_content, template, author, style = style, youtube_url=youtube_url)
    css = get_css(template, style)
    css_to_file(response_str, css)
    response_str = add_css_link(response_str)
    return response_str

def css_to_file(response_str, css):
    with open("./static/css/generated.css", "w")as file:
        file.write(css)

def add_css_link(html_content):
    css_link = f'<link rel="stylesheet" href="../static/css/generated.css" />'
    head_tag = '</head>'
    return html_content.replace(head_tag, f'{css_link}\n{head_tag}')

@app.route('/test.html')
def test_page():
    return render_template('test.html')

@app.route('/', methods=['GET'])
def index():
    print("Rendering index page")
    return render_template('start.html')


@app.route('/generate-blog', methods=['POST'])
def generate_blog():
    print("Entering generate_blog function")
    try:
        url = request.form['video_url']
        print(f"Received video URL: {url}")
        video_id = get_youtube_video_id(url)
        print(f"Extracted video ID: {video_id}")
        template = request.form['selected_template']
        print(f"Selected template: {template}")
        style = request.form['selected_palette']
        print(f"Selected style palette: {style}")
        if not video_id:
            print("Error: Invalid YouTube URL")
            return jsonify({'error': 'Invalid YouTube URL'}), 400

        print("Fetching transcript...")
        transcript = fetch_transcript(video_id)
        print(f"Fetched transcript (first 100 chars): {transcript[:100]}...")
        if not transcript:
            print("Error: Could not fetch transcript")
            return jsonify({'error': 'Could not fetch transcript'}), 400

        print("Generating blog content...")
        html_content = get_blog(transcript, template, style=style, youtube_url=url)
        print("Blog content generated successfully")
        print(f"Generated HTML content (first 100 chars): {html_content[:100]}...")
        return jsonify({'html_content': html_content})
    except Exception as e:
        print(f"Error occurred in generate_blog: {str(e)}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
