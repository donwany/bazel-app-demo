from absl.testing import absltest

def add(a: int, b: int) -> int:
  return a + b


# Create a test case class that inherits from absltest.TestCase
class TestMathOperations(absltest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(add(5, -3), 2)


if __name__ == "__main":
    absltest.main()