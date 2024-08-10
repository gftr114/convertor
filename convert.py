class ConverterLogic():
    def __init__(self):
        self.rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "UAH": 41.1,
            "GBR": 0.75
        }

    def convert(self, amount, from_cur, to_cur):
        if from_cur == to_cur:
            return amount
        
        return amount * self.rates[to_cur] / self.rates[from_cur]