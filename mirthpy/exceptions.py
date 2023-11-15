class UnauthorizedError(Exception):
    def __init__(self, message="Unauthorized access"):
        self.message = message
        super().__init__(self.message)