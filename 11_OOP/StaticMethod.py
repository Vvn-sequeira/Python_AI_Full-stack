
class ChaiUtils:

    @staticmethod
    def clean_(text):
        return [ itme.strip() for itme in text.split(",")]


raw = "  water ,    hello , dfdkj            , hi "
print(raw)
print(ChaiUtils.clean_(raw))