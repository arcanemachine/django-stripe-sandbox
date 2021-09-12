import dotenv
from django.test import SimpleTestCase
from unittest import mock

from . import helpers as h

hh = h  # deleteme

MOCK_DOTENV = {'TEST_KEY': 'TEST_VALUE'}


class ColorizeTest(SimpleTestCase):
    test_message = 'Test Message'

    def test_colorize_with_no_param_color_returns_yellow_message(self):
        self.assertEqual(
            h.colorize(self.test_message),
            f"{h.COLOR_CODE_YELLOW}{self.test_message}{h.COLOR_CODE_WHITE}")

    def test_colorize_with_param_color_green_returns_green_message(self):
        self.assertEqual(
            h.colorize(self.test_message, 'green'),
            f"{h.COLOR_CODE_GREEN}{self.test_message}{h.COLOR_CODE_WHITE}")

    def test_colorize_with_param_color_red_returns_red_message(self):
        self.assertEqual(
            h.colorize(self.test_message, 'red'),
            f"{h.COLOR_CODE_RED}{self.test_message}{h.COLOR_CODE_WHITE}")

    def test_colorize_with_param_color_yellow_returns_yellow_message(self):
        self.assertEqual(
            h.colorize(self.test_message, 'yellow'),
            f"{h.COLOR_CODE_YELLOW}{self.test_message}{h.COLOR_CODE_WHITE}")

    def test_colorize_with_invalid_param_color_returns_white_message(self):
        self.assertEqual(
            h.colorize(self.test_message, 'invalid color'),
            f"{h.COLOR_CODE_WHITE}{self.test_message}{h.COLOR_CODE_WHITE}")


class SettingGetTest(SimpleTestCase):
    @mock.patch('dotenv.dotenv_values', mock.Mock(return_value="HELLO"))
    def test_setting_get_returns_dotenv_file_if_value_present(self):
        self.assertEqual(h.setting_get('TEST_KEY'), 'TEST_VALUE')
