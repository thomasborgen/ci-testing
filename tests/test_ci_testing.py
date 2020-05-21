# -*- coding: utf-8 -*-

"""Test code for circleci."""

from ci_testing.do_stuff import return_arg


class TestDoStuff(object):
    """Test dostuff module."""

    def test_do_stuff_return_arg(self):
        """Test that we can initialize the run callable object."""
        test_value = 'bob'
        assert return_arg(test_value) == test_value
