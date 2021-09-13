import logging
import pprint
from django.conf import settings
from django.test import SimpleTestCase
from unittest.mock import Mock, patch

from stripes.templatetags import pretty_print, debug


class SetBreakpointTest(SimpleTestCase):
    @patch('builtins.breakpoint', Mock())
    def test_breakpoint_is_called_if_settings_debug_is_true(self):
        with self.settings(DEBUG=True):
            debug.set_breakpoint({'view': None})
            breakpoint.assert_called()

    @patch('builtins.breakpoint', Mock())
    def test_breakpoint_is_not_called_if_settings_debug_is_false(self):
        with self.settings(DEBUG=False):
            debug.set_breakpoint({'view': None})
            breakpoint.assert_not_called()

    @patch('logging.getLogger', Mock())
    def test_logs_warning_if_settings_debug_is_false(self):
        with self.settings(DEBUG=False):
            debug.set_breakpoint({'view': None})
            logging.getLogger.assert_called()


class PrettyPrintTest(SimpleTestCase):
    def test_filter_returns_expected_value(self):
        test_dict = {'test_key_1': 'test_value',
                     'test_key_2': ['a', 'b', 'c'],
                     'test_key_3': {'a': 1, 'b': 2, 'c': 3}}
        self.assertEqual(pprint.pformat(test_dict, indent=2, sort_dicts=False),
                         pretty_print.pretty_print(test_dict))
