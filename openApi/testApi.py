from locust import HttpUser, between, task

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index_page(self):
        self.client.get("/")

    @task(3)
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})
