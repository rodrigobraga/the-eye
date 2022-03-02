from locust import HttpUser, between, task


class Event(HttpUser):
    wait_time = between(1, 5)

    @task
    def post(self):
        payload = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "cta click",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/",
                "element": "chat bubble",
            },
            "timestamp": "2021-01-01 09:15:27.243860Z",
        }

        # Generate token using the command; get_tokens_for_user
        token = "Bearer <token>"

        self.client.post(
            url="/events/",
            json=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": token,
            },
        )
