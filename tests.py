import unittest
from main import app
import json
class Tests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    def testGetTasks(self):
        response = self.app.get('/gettasks',follow_redirects=True)
        d = (response.data).decode('utf-8')
        data = json.loads(d)
        print("Data: ",  data)
        self.assertEqual(response.status_code,200)
    def testPutTask(self):
        d = {"Name":"foo"}
        d = json.dumps(d)
        response = self.app.post(
            '/puttask',
            data = d
        )
        # comment
        self.assertEqual(response.status_code,204)
    def testBoth(self):
        d = {"Name":"bar"}
        d = json.dumps(d)
        response = self.app.post(
            '/puttask',
            data = d
        )
        res2 = self.app.get(
            "/gettasks"
        )
        # comment2
        data = json.loads(res2.data.decode('utf-8'))
        flag = False
        for item in data:
            if item["Name"] == "bar":
                flag = True
        self.assertEqual(flag,True)
        self.assertEqual(response.status_code,204)
        self.assertEqual(res2.status_code,201)

if __name__ == "__main__":
    unittest.main()