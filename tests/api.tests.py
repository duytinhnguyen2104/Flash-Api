# from pyunitreport import HTMLTestRunner
import unittest
from server.server import app
import json
from HtmlTestRunner import HTMLTestRunner


class ClientTest(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.empty= {}
        self.data = {
            "image_data": "ZnJvbSBhcHAgaW1wb3J0IG15YXBwDQppbXBvcnQgdW5pdHRlc3QNCg0KIyBweXRob24gLW0gdW5pdHRlc3QgdGVzdF9hcHANCg0KDQpjbGFzcyBUZXN0TXlBcHAodW5pdHRlc3QuVGVzdENhc2UpOg0KICAgIGRlZiBzZXRVcChzZWxmKToNCiAgICAgICAgc2VsZi5hcHAgPSBteWFwcC50ZXN0X2NsaWVudCgpDQoNCiAgICBkZWYgdGVzdF9tYWluKHNlbGYpOg0KICAgICAgICBydiA9IHNlbGYuYXBwLmdldCgnLycpDQogICAgICAgIGFzc2VydCBydi5zdGF0dXMgPT0gJzIwMCBPSycNCiAgICAgICAgYXNzZXJ0IGInTWFpbicgaW4gcnYuZGF0YQ0KICAgICAgICAjYXNzZXJ0IEZhbHNlDQoNCiAgICBkZWYgdGVzdF9hZGQoc2VsZik6DQogICAgICAgIHJ2ID0gc2VsZi5hcHAuZ2V0KCcvYWRkLzIvMycpDQogICAgICAgIHNlbGYuYXNzZXJ0RXF1YWwocnYuc3RhdHVzLCAnMjAwIE9LJykNCiAgICAgICAgc2VsZi5hc3NlcnRFcXVhbChydi5kYXRhLCAnNScpDQoNCiAgICAgICAgcnYgPSBzZWxmLmFwcC5nZXQoJy9hZGQvMC8xMCcpDQogICAgICAgIHNlbGYuYXNzZXJ0RXF1YWwocnYuc3RhdHVzLCAnMjAwIE9LJykNCiAgICAgICAgc2VsZi5hc3NlcnRFcXVhbChydi5kYXRhLCAnMTAnKQ0KDQogICAgZGVmIHRlc3RfNDA0KHNlbGYpOg0KICAgICAgICBydiA9IHNlbGYuYXBwLmdldCgnL290aGVyJykNCiAgICAgICAgc2VsZi5hc3NlcnRFcXVhbChydi5zdGF0dXMsICc0MDQgTk9UIEZPVU5EJyk=",
            "username": "thongnm",
            "index": 1
        }
        self.traing = {
            "image_data": "ZnJvbSBhcHAgaW1wb3J0IG15YXBwDQppbXBvcnQgdW5pdHRlc3QNCg0KIyBweXRob24gLW0gdW5pdHRlc3QgdGVzdF9hcHANCg0KDQpjbGFzcyBUZXN0TXlBcHAodW5pdHRlc3QuVGVzdENhc2UpOg0KICAgIGRlZiBzZXRVcChzZWxmKToNCiAgICAgICAgc2VsZi5hcHAgPSBteWFwcC50ZXN0X2NsaWVudCgpDQoNCiAgICBkZWYgdGVzdF9tYWluKHNlbGYpOg0KICAgICAgICBydiA9IHNlbGYuYXBwLmdldCgnLycpDQogICAgICAgIGFzc2VydCBydi5zdGF0dXMgPT0gJzIwMCBPSycNCiAgICAgICAgYXNzZXJ0IGInTWFpbicgaW4gcnYuZGF0YQ0KICAgICAgICAjYXNzZXJ0IEZhbHNlDQoNCiAgICBkZWYgdGVzdF9hZGQoc2VsZik6DQogICAgICAgIHJ2ID0gc2VsZi5hcHAuZ2V0KCcvYWRkLzIvMycpDQogICAgICAgIHNlbGYuYXNzZXJ0RXF1YWwocnYuc3RhdHVzLCAnMjAwIE9LJykNCiAgICAgICAgc2VsZi5hc3NlcnRFcXVhbChydi5kYXRhLCAnNScpDQoNCiAgICAgICAgcnYgPSBzZWxmLmFwcC5nZXQoJy9hZGQvMC8xMCcpDQogICAgICAgIHNlbGYuYXNzZXJ0RXF1YWwocnYuc3RhdHVzLCAnMjAwIE9LJykNCiAgICAgICAgc2VsZi5hc3NlcnRFcXVhbChydi5kYXRhLCAnMTAnKQ0KDQogICAgZGVmIHRlc3RfNDA0KHNlbGYpOg0KICAgICAgICBydiA9IHNlbGYuYXBwLmdldCgnL290aGVyJykNCiAgICAgICAgc2VsZi5hc3NlcnRFcXVhbChydi5zdGF0dXMsICc0MDQgTk9UIEZPVU5EJyk=",
            "username": "thongnm",
            "index": 10
        }

    def test_adduserimage(self):
        """
            Decriptions: without request body
        """        
        res = self.client.post('/addUserImage', data = json.dumps(self.data), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content_type, 'application/json')

    def test_adduserimage_500(self):
        """
            Decriptions: without request body
        """        
        res = self.client.post('/addUserImage', content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.content_type, 'application/json')

    def test_adduserimage_400(self):
        """
            Descriptions: empty request
        """
        res = self.client.post('/addUserImage', data = json.dumps(self.empty), content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.content_type, 'application/json')

    def test_training(self):
        """
            Descriptions: empty request
        """
        res = self.client.post('/addUserImage', data = json.dumps(self.traing), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content_type, 'application/json')

    @unittest.SkipTest
    def test_login(self):
        """

        """
        res = self.client.post('/face_recognition_func')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content_type, 'application/json')

if __name__ == '__main__':
    unittest.main()
    # unittest.main(testRunner=HTMLTestRunner(output='coverage'))