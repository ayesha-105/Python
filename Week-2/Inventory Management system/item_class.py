from datetime import date

class Item:
    def __init__(self,item_id, item_name,item_category, quantity, supplier,price_per_unit,date_added, expiry_date):
        self.item_id= item_id
        self.item_id= item_id
        self.item_name= item_name
        self.item_category= item_category
        self.quantity= quantity
        self.supplier= supplier
        self.price_per_unit= price_per_unit
        self.date_added= date.today().isoformat
        self.expiry_date= expiry_date

    def to_dict(self):
        return{
            "item_id": self.item_id,
            "item_name": self.item_name,
            "item_category": self.item_category,
            "quantity": self.quantity,
            "supplier": self.supplier,
            "price_per_unit": self.price_per_unit,
            "date_added": self.date_added,
            "expiry_date": self.expiry_date
        }