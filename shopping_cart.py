class ShoppingCart:
    # write your code here
    def __init__(self, total=0, employee_discount=None, items=[], prices=[]):
      self.total = total
      self.employee_discount = employee_discount
      self.items = items
      self.prices = prices
    
    def add_item(self, name, price, quantity=1):
       self.items.append(name)
       for i in range(1,quantity+1):
          self.prices.append(price)
       self.total = sum(self.prices)
       return self.total

    def mean_item_price(self):
       return sum(self.prices)/len(self.prices)

    def median_item_price(self):
       self.prices.sort()
       length = len(self.prices)
       if length%2 == 0:
          median = sum(self.prices[(length/2)-1:(length/2)+1])/2
       else:
          median = self.prices[int((length/2)-.5)]
       return median


    def apply_discount(self):
       if self.employee_discount == None:
          return "Sorry, there is no employee discount to apply to your cart :("
       else:
          return self.total * (1-(self.employee_discount/100))

    def void_last_item(self):
       if self.prices == []:
           return "There are no items in your cart!"
       else:
          self.prices.pop()
          self.total = sum(self.prices)
          return self.total
