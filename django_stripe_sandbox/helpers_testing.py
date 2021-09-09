class SetUpTestCaseMixin:
    def get_response(self, test_url=None):
        if test_url:
            return self.client.get(test_url)
        else:
            return self.client.get(self.test_url)
