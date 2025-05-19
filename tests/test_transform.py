import unittest
import pandas as pd
from src.transform import transform_data

class TestTransform(unittest.TestCase):

    def test_transform_data(self):
        data = {
            "country": ["United States, Canada", None],
            "duration": ["90 min", "1 Season"]
        }
        df = pd.DataFrame(data)
        transformed_df = transform_data(df)

        # Test main_country extraction
        self.assertEqual(transformed_df.loc[0, "main_country"], "United States")
        self.assertEqual(transformed_df.loc[1, "main_country"], "Unknown")

        # Test duration_num extraction
        self.assertEqual(transformed_df.loc[0, "duration_num"], 90.0)
        self.assertEqual(transformed_df.loc[1, "duration_num"], 1.0)

        # Test duration_type extraction
        self.assertEqual(transformed_df.loc[0, "duration_type"], "min")
        self.assertEqual(transformed_df.loc[1, "duration_type"], "Season")

if __name__ == '__main__':
    unittest.main()