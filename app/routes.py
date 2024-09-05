from flask import Blueprint, jsonify
from .crawler import crawl_all_sources

main = Blueprint('main', __name__)


@main.route('/api/v1/news/crawl', methods=['GET'])
def crawl_news_route():
    data = crawl_all_sources()
    return jsonify(data)
