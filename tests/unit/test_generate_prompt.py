"""2023-01-25 09:48:33
Contains unit tests for the get_response module.
"""
import os
from pathlib import Path
import unittest
from unittest import mock
from unittest.mock import patch
from controller.generate_prompt import generate_prompt


class GeneratePromptTest(unittest.TestCase):
    """Test case for generate_prompt function unit tests."""

    def setUp(self) -> None:
        self.hello_world_file = open("hello_world.py", "w", encoding='utf-8')
        self.hello_world_file.write('print("Hello world!")\n')
        return super().setUp()

    def tearDown(self) -> None:
        os.unlink(self.hello_world_file.name)
        return super().tearDown()

    def test_generate_prompt_given_an_argument_str(self):
        """Validate function generate_prompt returns the same argument"""

        prompt = 'Hi.'
        expected = 'Hi.'
        actual = generate_prompt(prompt)
        self.assertEqual(actual, expected)

    def test_generate_prompt_given_an_optional_text_file_path(self):
        """Validate function generate_prompt returns the same argument"""

        prompt = 'Explain this code:\n'
        text_file_path = Path(
            'C:/Users/Jorge/git/pair-programming-chatgpt-ai/hello_world.py')
        expected = """Explain this code:
```python
print("Hello world!")
```"""
        actual = generate_prompt(prompt, text_file_path)
        self.assertEqual(actual, expected)

        # Assert using str instead of Path object in the text_file_path
        text_file_path = 'C:/Users/Jorge/git/pair-programming-chatgpt-ai/hello_world.py'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
