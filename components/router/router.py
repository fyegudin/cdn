import json
from flask import Flask, redirect


class Router:
    def __init__(self, caches):
        self.caches = caches
        self.status_file = "status.json"
        self.app = Flask(__name__)
        self.app.route('/content/<int:content_id>')(self.redirect_to_cache)

    def redirect_to_cache(self, content_id):
        with open(self.status_file, "r") as f:
            statuses = json.load(f)
        for cache_name, status in statuses.items():
            if status == "OK":
                cache = next((cache for cache in self.caches if cache.name == cache_name), None)
                if cache:
                    return redirect(cache.get_content_url(content_id), code=302)
        return "No available cache found"
