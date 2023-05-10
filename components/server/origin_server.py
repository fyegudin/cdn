from flask import Flask


class Server:
    def __init__(self, name, content_path):
        self.name = name
        self.content_path = content_path
        self.app = Flask(__name__)
        self.app.route('/content/<int:content_id>')(self.get_content)

    def get_content(self, content_id):
        with open(self.content_path + str(content_id) + ".mp4", "rb") as f:
            content = f.read()
        return content
