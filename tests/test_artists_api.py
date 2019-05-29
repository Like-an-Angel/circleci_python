import unmock
import unittest
from app import fetchSpotifyArtist



class TestArtistsApi(unittest.TestCase):
    def test_fetchSpotifyArtist(self):

        self.response = fetchSpotifyArtist()
        assert isinstance(self.response.json(), dict)
        assert isinstance(self.response.json(), dict)
        self.assertEqual(self.response.status_code, 200)
