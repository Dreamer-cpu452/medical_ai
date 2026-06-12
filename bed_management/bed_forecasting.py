class BedForecasting:

    def forecast(
        self,
        current_usage
    ):

        return int(
            current_usage * 1.15
        )