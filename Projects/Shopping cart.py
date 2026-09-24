Items  = {"Apple" : 10,
          "Banana" : 15,
          "Watermelon" : 18,
          "Grape" : 12,
          "Orange" : 10,}

Cart = input(f"Choose items to add to your cart from:\n {Items.keys()}\n").split()
Cart = [item.capitalize() for item in Cart if item.capitalize() in Items.keys()]

price = sum(Items.get(items) for items in Cart)

print(f"That will cost you: R{price}")