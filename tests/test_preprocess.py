import unittest
import pandas as pd
from src.preprocess import preprocess_data

class TestPreprocess(unittest.TestCase):

    def test_preprocess_data(self):
        # Sample input DataFrame
        data = {
            "title": [" Movie A ", None],
            "type": ["Movie", "TV Show"],
            "date_added": ["January 1, 2020", None],
            "country": ["United States", "India"]
        }
        df = pd.DataFrame(data)

        processed_df = preprocess_data(df)

        # Row with None title should be dropped
        self.assertEqual(processed_df.shape[0], 1)
        # Title should be stripped
        self.assertEqual(processed_df.iloc[0]['title'], "Movie A")
        # Column names should be lowercase with underscores
        self.assertIn("date_added", processed_df.columns)

if __name__ == '__main__':
    unittest.main()