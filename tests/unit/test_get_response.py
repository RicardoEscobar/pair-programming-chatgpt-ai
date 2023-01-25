"""2023-01-24 13:49:31
Contains unit tests for the get_response module.
"""
import unittest
from unittest import mock
from unittest.mock import patch
from controller.get_response import get_response


class GetResponseTest(unittest.TestCase):
    """Test case for get_response function unit tests."""

    def test_get_response_greeting(self):
        """Validate function get_response returns a greeting string."""

        prompt = 'Hi.'
        expected = 'Hi there! How can I help you?'
        mocked_response = mock.Mock()
        mocked_response.choices = [mock.Mock(text=expected)]
        with patch('openai.Completion.create', return_value=mocked_response) as mocked_create:
            actual = get_response(prompt)
            mocked_create.assert_called_with(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=2047
            )

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
