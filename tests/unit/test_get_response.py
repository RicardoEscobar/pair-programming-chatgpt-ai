"""2023-01-24 13:49:31
Contains unit tests for the get_response module.
"""
import unittest
from unittest.mock import patch
from controller.get_response import get_response


class GetResponseTest(unittest.TestCase):
    """Test case for get_response function unit tests."""

    def test_get_response_greeting(self):
        """Validate function get_response returns a greeting string."""

        prompt = 'Hi.'
        expected = 'Hi there! How can I help you?'
        with patch('openai.Completion.create', return_value=expected) as mocked_create:
            get_response(prompt)
            mocked_create.assert_called_with(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=2047
            )

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
