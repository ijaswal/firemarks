from flask import Flask, jsonify
from scraper.kindle_scraper import scrape_kindle_highlights

app = Flask(__name__)

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'ok'}), 200

@app.route('/api/highlights')
def get_kindle_highlights():
    highlights = scrape_kindle_highlights()
    return jsonify(highlights)

if __name__ == '__main__':
    app.run(debug=True)
