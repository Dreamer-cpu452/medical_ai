import matplotlib.pyplot as plt


class Charts:

    def create_chart(self):

        x = [
            "Jan",
            "Feb",
            "Mar",
            "Apr"
        ]

        y = [
            100,
            120,
            180,
            200
        ]

        plt.plot(
            x,
            y
        )

        plt.title(
            "Patient Growth"
        )

        plt.show()