import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from run_local import build

class TestAnalytics(unittest.TestCase):
    def test_completed_revenue(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertAlmostEqual(build(Path(tmp) / "test.db"), 410.50)

if __name__ == "__main__": unittest.main()
