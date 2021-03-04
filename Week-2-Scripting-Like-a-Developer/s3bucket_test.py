import unittest


class TestS3(unittest.TestCase):
    def test_bucket_name_value(self):
        bucket = 'cloudskillsbootcamp'

        self.assertEqual(bucket, 'cloudskillsbootcamp')

    def test_region_value(self):
        region = 'useast1'

        self.assertEqual(region, 'useast1')

    def test_bucket_name_is_string(self):
        bucket = 'cloudskillsbootcamp'

        self.assertTrue(type(bucket), str)

    def test_region_is_string(self):
        region = 'useast1'

        self.assertTrue(type(region), str)


if __name__ == '__main__':
    unittest.main()
