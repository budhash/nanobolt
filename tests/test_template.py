import pytest
import logging
from .assertions import assertEqual, assertNotEqual, assertTrue, assertFalse
from .assertions import assertLess, assertLessEqual, assertGreater, assertGreaterEqual, assertAlmostEqual, assertNotAlmostEqual
from .assertions import assertIs, assertIsNot, assertIsInstance, assertIsNone, assertIsNotNone
from .assertions import assertIn
from .assertions import assertRaises

LOGGER = logging.getLogger(__name__)


class TestTemplate:

    @pytest.fixture(scope="class", autouse=True)
    def setup_teardown_class(self) -> None:
        LOGGER.info("Class: setup")
        yield
        LOGGER.info("Class: teardown")

    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown_function(self) -> None:
        pass
        yield
        pass

    def test_simple(self) -> None:
        """Test Template"""
        LOGGER.info("info message")
        assert 1 == 1

    def test_assertEqual(self):
        assertEqual(5, 5, "Numbers are not equal")

    def test_assertNotEqual(self):
        assertNotEqual(5, 3, "Numbers are equal")

    def test_assertTrue(self):
        assertTrue(True, "Expression is not true")

    def test_assertFalse(self):
        assertFalse(False, "Expression is not false")

    def test_assertLess(self):
        assertLess(2, 5, "2 is not less than 5")

    def test_assertLessEqual(self):
        assertLessEqual(2, 2, "2 is not less or equal to 2")

    def test_assertGreater(self):
        assertGreater(5, 2, "5 is not greater than 2")

    def test_assertGreaterEqual(self):
        assertGreaterEqual(5, 5, "5 is not greater or equal to 5")

    def test_assertAlmostEqual(self):
        assertAlmostEqual(1.3333, 1.3334, places=3, msg="Numbers are not almost equal")

    def test_assertNotAlmostEqual(self):
        assertNotAlmostEqual(1.3333, 1.3334, places=4, msg="Numbers are almost equal")

    def test_assertIn(self):
        assertIn(1, [1, 2, 3], "1 is not in list")

    def test_assertIs(self):
        a = [1, 2, 3]
        b = a
        assertIs(a, b, "a is not b")

    def test_assertIsNot(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        assertIsNot(a, b, "a is b")

    def test_assertIsInstance(self):
        assertIsInstance(1, int, "1 is not an instance of int")

    def test_assertIsNone(self):
        assertIsNone(None, "Expression is not None")

    def test_assertIsNotNone(self):
        assertIsNotNone(1, "Expression is None")

    def test_assertRaises(self):
        def func():
            raise ValueError
        assertRaises(ValueError, func)

    @pytest.mark.parametrize("input1, input2, expected", [(3, 2, 5), (2, 3, 5), (5, 5, 10)])
    def test_parameterized(self, input1, input2, expected):
        assert input1 + input2 == expected, f"Test Failed: {input1} + {input2} is not equal to {expected}"

    @pytest.fixture(params=["1", "2", "3"])
    def digits(self, request):
        return request.param

    @pytest.fixture(params=["+", "-"])
    def signs(self, request):
        return request.param

    def test_fixtures(self, digits):
        assert digits.isnumeric(), f"Test Failed: {digits} is not numeric"

    def test_multi_fixtures(self, signs, digits):
        LOGGER.info("value: " + signs + digits)

    @pytest.mark.skip('Reasoning for skipping this test')
    def test_skip(self):
        pytest.fail('this should be skipped')

    @pytest.mark.skipif('a' in ['a', 'b'], reason='Reasoning for skipping another test')
    def test_skip_if(self):
        pytest.fail('this should be skipped')

    @pytest.mark.skipif(not 42 == 24, reason='Reasoning for skipping test 42')
    def test_skip_unless(self):
        pytest.fail('this should be skipped')

    @pytest.mark.xfail
    def test_expected_failure(self):
        assert 1 == 0

    def teardown_method(self) -> None:
        """Run after every test method"""
        pass
