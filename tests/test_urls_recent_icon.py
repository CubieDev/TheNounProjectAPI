import unittest

import context 


from TheNounProjectAPI.api import API

class IconCustomURLs(unittest.TestCase):

    def setUp(self):
        key = "mock api key to satisfy type check in api._get_oauth()"
        secret = "mock secret key to satisfy type check in api._get_oauth()"
        self.api = API(key, secret, testing=True)

    def _test_get_recent_icons(self, limit=None, offset=None, page=None):
        """
        Helper function to call api's get_recent_icons in such a way that we only get the URL
        and don't actually make the request.
        """
        return self.api.get_recent_icons(limit=limit, offset=offset, page=page).url

    def test_get_recent_icons(self):
        """
        Test URL for get_recent_icons
        """
        expected = "http://api.thenounproject.com/icons/recent_uploads"
        result = self._test_get_recent_icons()
        self.assertEqual(expected, result)

    def test_get_recent_icons_limit_offset(self):
        """
        Test URL for get_recent_icons, with limit 12 and offset 3
        """
        expected = "http://api.thenounproject.com/icons/recent_uploads?limit=12&offset=3"
        limit = 12
        offset = 3
        result = self._test_get_recent_icons(limit=limit, offset=offset)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()