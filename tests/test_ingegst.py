import unittest
import os
import pandas as pd
from src.ingest import load_csv

class TestIngest(unittest.TestCase):

    def setUp(self):
        # Setup: create a small dummy CSV file
        self.test_file = "tests/test_data.csv"
        data = {
            "title": ["Movie A", "Movie B"],
            "type": ["Movie", "TV Show"]
        }
        pd.DataFrame(data).to_csv(self.test_file, index=False)

    def tearDown(self):
        # Cleanup after test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_csv_success(self):
        df = load_csv(self.test_file)
        self.assertEqual(df.shape, (2, 2))  # 2 rows, 2 columns

    def test_load_csv_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            load_csv("tests/nonexistent_file.csv")

if __name__ == '__main__':
    unittest.main()