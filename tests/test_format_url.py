import os
import sys
import unittest

# Ajouter src au chemin de recherche des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import format_url


class TestFormatUrl(unittest.TestCase):
    def test_uri_with_slash(self) -> None:
        self.assertEqual(format_url("https", "google.com", "/fr"), "https://google.com/fr")
        
    def test_uri_without_slash(self) -> None:
        self.assertEqual(format_url("https", "google.com", "fr"), "https://google.com/fr")
        
    def test_error_protocol(self) -> None:
        with self.assertRaises(ValueError):
            format_url("ftp", "google.com", "fr")
        
    def test_error_hostname(self) -> None:
        with self.assertRaises(ValueError):
            format_url("ftp", "google", "fr")


if __name__ == "__main__":
    unittest.main(verbosity=2)

