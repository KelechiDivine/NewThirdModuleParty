class HelperCurrencyConversation:
    # def __init__(self, amount_in_aud, amount_in_gbp):
    #     self.AmountInAud = amount_in_aud
    #     self.AmountInGbp = amount_in_gbp
        
        def compute_usd_total(amount_in_aud=0, amount_in_gbp=0):
            total=0
            total += amount_in_aud * 0.78
            total += amount_in_gbp * 1.29
            return  total
        print(compute_usd_total(amount_in_gbp=10))