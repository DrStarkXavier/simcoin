from unittest import TestCase
from mock import patch
from node import abstract
from datetime import datetime
import config


class TestNode(TestCase):

    @patch('bash.check_output')
    @patch('bash.call_silent')
    @patch('dockercmd.exec_cmd')
    def test_get_timestamp(self, _, m_call_silent, m_check_output):
        m_call_silent.return_value = 0
        m_check_output.return_value = '2017-07-07 09:13:46.344211 UpdateTip: new best=hash height=111'

        received = abstract.get_timestamp('node-0', 'hash')

        self.assertEqual(received, datetime.strptime('2017-07-07 09:13:46.344211', config.log_time_format).timestamp())

    @patch('bash.check_output')
    @patch('bash.call_silent')
    @patch('dockercmd.exec_cmd')
    def test_get_timestamp_never_received(self, _, m_call_silent, m_check_output):
        m_call_silent.return_value = 1
        m_check_output.return_value = ''

        received = abstract.get_timestamp('node-0', 'hash')

        self.assertEqual(received, -1)

