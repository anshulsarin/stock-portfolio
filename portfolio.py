"""
Commit this file to your repository and push it to GitHub using GitHub Desktop, with a suitable commit message.
"""

class Portfolio():
    portfolio = []

    def __init__ (self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def buy (self):
        portfolio.append((self.name, self.shares, self.price))

    def cost (self):
        total_price = sum(self.shares*self.price for (_, self.shares, self.price) in portfolio)
        return total_price
