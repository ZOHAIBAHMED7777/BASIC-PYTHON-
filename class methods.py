class bank:
    bank_name="pakistan_bank"
    rate_of_interest=14.9
    @staticmethod
    def simple_interest(prin,n):
        si=(prin*n*bank.rate_of_interest)/100
        print(si)
        
prin=float(input("enter the value of simple intrest"))
n=int(input("enter the year of the interest"))
bank.simple_interest(prin,n)