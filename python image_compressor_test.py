import unittest

# Import the functions you want to test from your main code
from main import img_from_file_path, img_from_http_request, main

class TestImageCompressor(unittest.TestCase):
    def test_img_from_file_path(self):
        # Provide a sample image file path
        file_path = "C:\Users\AYAN PRADHAN\Desktop\mypic.jfif"

        # Call the function and check if it returns a valid image object
        result = img_from_file_path(file_path)
        self.assertIsNotNone(result)

    def test_img_from_http_request(self):
        # Provide a sample image URL
        url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png"

        # Call the function and check if it returns a valid image object
        result = img_from_http_request(url)
        self.assertIsNotNone(result)

    
    # You can add more test cases for other functions

if __name__ == '__main__':
    unittest.main()
