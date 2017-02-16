# -*- coding: UTF-8 -*-
import unittest
import tcparser

class TestParserMethods(unittest.TestCase):

        def test_getArticleInfoNoCompany(self):
                self.assertEqual(tcparser.getArticleInfo('https://techcrunch.com/2017/02/15/elon-musk-posts-then-deletes-tweets-calling-trumps-immigration-ban-not-right/'), ['Elon Musk posts, then deletes, tweets calling Trump’s immigration ban “not right”', 'https://techcrunch.com/2017/02/15/elon-musk-posts-then-deletes-tweets-calling-trumps-immigration-ban-not-right/', 'n/a', 'n/a'])

        def test_getArticleInfoWithCompany(self):
                self.assertEqual(tcparser.getArticleInfo('https://techcrunch.com/2017/02/15/google-teams-up-with-kaggle-to-host-100000-video-classification-challenge/'), ['Google teams up with Kaggle to host $100,000 video classification challenge', 'https://techcrunch.com/2017/02/15/google-teams-up-with-kaggle-to-host-100000-video-classification-challenge/', 'Google', 'http://www.google.com/'])

        def test_getArticleUrls(self):
                self.assertTrue(len(tcparser.getArticleUrls("https://techcrunch.com", ['//h2[@class="post-title"]/node()/@href', '//li[@class="plain-item"]/node()/@href'])) > 0)

if __name__ == '__main__':
        unittest.main()