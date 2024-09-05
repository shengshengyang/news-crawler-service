import unittest
from app.crawler import crawl_all_sources


class TestCrawler(unittest.TestCase):
    def test_crawl_news(self):
        news_items = crawl_all_sources()
        self.assertIsInstance(news_items, list)
        self.assertGreater(len(news_items), 0)


if __name__ == '__main__':
    unittest.main()
