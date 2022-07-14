import sys
sys.path_append('../repo-name')#imports python file from parent dirctory 
from main_py_file_name import path_append

class BasicTests(unittest.TestCase):

    #executed prior to each test
    def setUp(self):
        self.app = app.test_client()
    
    def test_main_page(self):
        response = self.app.get('/', follow redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.app.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_register_page(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual()
        unittest.main(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()