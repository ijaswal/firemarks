# tests/scraper_test.py

import unittest

from backend.scraper.kindle_scraper import scrape_kindle_highlights


class TestKindleScraper(unittest.TestCase):
    def test_scrape_kindle_highlights(self):
        highlights = scrape_kindle_highlights()
        self.assertIsInstance(highlights, list)
        self.assertTrue(len(highlights) > 0)

if __name__ == '__main__':
    unittest.main()
