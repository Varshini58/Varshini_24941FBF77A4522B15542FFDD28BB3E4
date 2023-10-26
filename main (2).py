class Bankaccount:
  def __init__(self):
    self.balance=0
    print("Bankaccount Details")
  def deposit (self):
    amount=float(input("Enter the amount:"))
    self.balance+=amount
    print("amount is deposited in your amount",amount)
  def Withdraw (self):
    amount=float(input("Enter the amount:"))
    if self.balance>=amount:
      self.balance-=amount
      print("your Withdraw:", amount)
    else:
      print("you don't have enough money ")
  def display (self):
      print("Available Balance:",self.balance)
s=Bankaccount()
s.deposit()
s.Withdraw()
s.display()


















  

      
      
    
    
    
    
