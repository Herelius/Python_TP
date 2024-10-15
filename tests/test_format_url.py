import os
import sys
import unittest

# Ajouter src au chemin de recherche des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import format_url


class TestFormatUrl(unittest.TestCase):
    def test_uri_exists(self) -> None:
        self.assertEqual(format_url("https", "google.com", ""), "https://google.com/", msg="url 'https://google.com/' exists!")
    
    def test_uri_unknown(self) -> None:
        self.assertEqual(format_url("https", "toto.com", "fr"), None, msg="url 'https://toto.com/fr' does not exists!")


if __name__ == "__main__":
    unittest.main(verbosity=2)

