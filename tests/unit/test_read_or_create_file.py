import unittest
from pathlib import Path
import os
from model.read_or_create_file import read_or_create_file


class TestReadOrCreateFile(unittest.TestCase):
    def test_file_exists(self):
        """Test that the function returns the contents of an existing file when the file exists"""
        file_path = "example.txt"
        placeholder_text = "Placeholder text"
        expected_contents = "Example file contents"

        with open(file_path, "w", encoding='utf-8') as file:
            file.write(expected_contents)

        actual_contents = read_or_create_file(file_path, placeholder_text)

        self.assertEqual(actual_contents, expected_contents)

    def test_file_not_exists(self):
        """Test that the function creates a new file and returns the placeholder text when the file does not exist"""
        file_path = "example.txt"
        placeholder_text = "Placeholder text"

        actual_contents = read_or_create_file(file_path, placeholder_text)

        self.assertEqual(actual_contents, placeholder_text)

    def test_file_path_with_pathlib(self):
        """Test that the function can accept a pathlib.Path object for the file path"""
        file_path = Path("example.txt")
        placeholder_text = "Placeholder text"

        actual_contents = read_or_create_file(file_path, placeholder_text)

        self.assertEqual(actual_contents, placeholder_text)

    def test_empty_file(self):
        """Test that the function creates a new file and returns the placeholder text when the file exists but is empty"""
        file_path = "example.txt"
        placeholder_text = "Placeholder text"

        with open(file_path, "w", encoding='utf-8') as file:
            file.write("")

        actual_contents = read_or_create_file(file_path, placeholder_text)

        self.assertEqual(actual_contents, placeholder_text)

    def test_placeholder_text_is_optional(self):
        """test that if the placeholder_text is not provided, it creates the file with an empty string"""
        file_path = "example.txt"

        actual_contents = read_or_create_file(file_path)

        self.assertEqual(actual_contents, "")

    def tearDown(self):
        if os.path.exists("example.txt"):
            os.remove("example.txt")


if __name__ == '__main__':
    unittest.main()
