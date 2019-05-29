import unmock
import unittest
from app import fetchSpotifyArtist, fetchSpotifyTracks, fetchSpotifyPlaylists



class TestArtistsApi(unittest.TestCase):
    def test_fetchSpotifyArtist(self):

        self.response = fetchSpotifyArtist()
        assert isinstance(self.response.json(), dict)
        assert isinstance(self.response.json(), dict)
        self.assertEqual(self.response.status_code, 200)

class TestPlaylistsApi(unittest.TestCase):
    def test_fetchSpotifyPlaylist(self):

        self.response = fetchSpotifyPlaylists()
        assert isinstance(self.response.json(), dict)
        assert isinstance(self.response.json(), dict)
        self.assertEqual(self.response.status_code, 200)

class TestTracksApi(unittest.TestCase):
    def test_fetchSpotifyTracks(self):

        self.response = fetchSpotifyTracks4()
        assert isinstance(self.response.json(), dict)
        assert isinstance(self.response.json(), dict)
        self.assertEqual(self.response.status_code, 200)
