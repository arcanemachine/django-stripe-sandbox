import os
from django.test import SimpleTestCase
from unittest.mock import Mock, patch

from . import helpers as h

hh = h  # deleteme


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


MOCK_DOTENV = {'TEST_KEY': 'TEST_VALUE_DOTENV'}
MOCK_OS_ENVIRON = {'TEST_KEY': 'TEST_VALUE_OS_ENVIRON'}


class SettingGetTest(SimpleTestCase):
    @patch('dotenv.dotenv_values', Mock(return_value=MOCK_DOTENV))
    def test_setting_get_returns_dotenv_value_if_value_present(self):
        self.assertEqual(h.setting_get('TEST_KEY'), 'TEST_VALUE_DOTENV')

    @patch.dict(os.environ, MOCK_OS_ENVIRON, clear=True)
    def test_setting_get_returns_os_environ_value_if_value_present(self):
        self.assertEqual(h.setting_get('TEST_KEY'), 'TEST_VALUE_OS_ENVIRON')

    # this test uses DEBUG because non-existent keys cannot be mocked
    @patch('django_stripe_sandbox.local_config.DEBUG',
           'TEST_VALUE_LOCAL_CONFIG')
    def test_setting_get_returns_local_config_value_if_value_present(self):
        self.assertEqual(h.setting_get('DEBUG'), 'TEST_VALUE_LOCAL_CONFIG')

    def test_setting_get_returns_default_value_if_no_values_present(self):
        default_value = 'TEST_VALUE_DEFAULT'
        self.assertEqual(h.setting_get('TEST_KEY', default_value),
                         default_value)

    def test_setting_get_shows_warning_if_default_cannot_be_cast(self):
        pass

    def test_setting_get_shows_warning_with_default_value_secret_key(self):
        pass

    def test_setting_get_shows_warning_with_default_value_debug(self):
        pass

    def test_setting_get_shows_warning_with_default_value_other(self):
        pass

    def test_setting_get_shows_no_warning_if_show_warning_is_false(self):
        pass

    def test_setting_get_adds_dotenv_value_to_multi_locations_list(self):
        pass

    def test_setting_get_adds_os_environ_value_to_multi_locations_list(self):
        pass

    def test_setting_get_adds_local_config_value_to_multi_locations_list(self):
        pass

    # TODO: why does TEST_KEY show as being duplicated in local_config?
