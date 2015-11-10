import nose
import awesome

def test_add():
    nose.tools.assert_equal(awesome.smile(), ":)")

def test_whatever():
    assert True

def test_sameness():
    nose.tools.assert_equal(awesome.smile(), awesome.smile2())
