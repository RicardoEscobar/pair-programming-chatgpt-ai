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
        # Creates test file with python code
        with open("hello_world.py", "w", encoding='utf-8') as file:
            file.write('print("Hello world!")\n')
            self.hello_world_file_python = Path(file.name)

        # Creates test file with java code
        with open("hello_world.java", "w", encoding='utf-8') as file:
            file.write("""class Simple{
    public static void main(String args[]){
     System.out.println("Hello Java");
    }
}
""")
            self.hello_world_file_java = Path(file.name)

        return super().setUp()

    def tearDown(self) -> None:
        os.unlink(self.hello_world_file_python)
        os.unlink(self.hello_world_file_java)
        return super().tearDown()

    def test_generate_prompt_given_an_argument_str(self):
        """Validate function generate_prompt returns the same argument"""

        prompt = 'Hi.'
        expected = 'Hi.'
        actual = generate_prompt(prompt)
        self.assertEqual(actual, expected)

    def test_generate_prompt_given_an_optional_text_file_path(self):
        """Validate function generate_prompt returns considering a file path as input parameter."""

        prompt = 'Explain this code:\n'
        expected = """Explain this code:
```
print("Hello world!")
```"""
        actual = generate_prompt(prompt, self.hello_world_file_python)
        self.assertEqual(actual, expected)

    def test_generate_prompt_given_an_optional_programming_language(self):
        """Validate function generate_prompt returns considering an optional given programming language."""

        # Assert giving a 'Python' argument for programming_language expecting lowercase 'python'
        prompt = 'Explain this code:\n'
        programming_language = 'Python'
        expected = """Explain this code:
```python
print("Hello world!")
```"""

        actual = generate_prompt(
            prompt, self.hello_world_file_python, programming_language)
        self.assertEqual(actual, expected)

        # Assert giving JAVA as programming_language
        programming_language = 'JAVA'
        expected = """Explain this code:
```java
class Simple{
    public static void main(String args[]){
     System.out.println("Hello Java");
    }
}
```"""
        actual = generate_prompt(
            prompt, self.hello_world_file_java, programming_language)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
