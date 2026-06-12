class ResourceForecasting:

    def forecast(
        self,
        current_usage
    ):

        return int(
            current_usage * 1.20
        )