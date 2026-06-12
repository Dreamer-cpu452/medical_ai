import joblib


class ModelLoader:

    @staticmethod
    def load_model(model_path):

        try:

            model = joblib.load(
                model_path
            )

            return model

        except Exception as e:

            print(
                "Model Loading Error:",
                e
            )

            return None