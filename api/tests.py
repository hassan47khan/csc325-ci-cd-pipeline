from rest_framework.test import APITestCase


class HealthEndpointTests(APITestCase):
    def test_health_returns_ok(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


class HelloEndpointTests(APITestCase):
    def test_hello_default_name(self):
        response = self.client.get("/api/hello/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, World!"})

    def test_hello_custom_name(self):
        response = self.client.get("/api/hello/", {"name": "CSC325"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, CSC325!"})
