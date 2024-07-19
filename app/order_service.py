import re


class OrderService:
    def transform(self, order_data):
        # 檢查 name
        if not re.match(r'^[a-zA-Z\s]+$', order_data['name']):
            raise ValueError("Name must contain only English letters and spaces")
        if not order_data['name'].istitle():
            raise ValueError("Name does not start with an uppercase letter")

        price = float(order_data['price'])

        # 檢查並轉換 currency
        if order_data['currency'] not in ['TWD', 'USD']:
            raise ValueError("Currency is not TWD or USD")
        if order_data['currency'] == 'USD':
            price *= 31
            order_data['price'] = str(price)
            order_data['currency'] = 'TWD'

        # 檢查 price
        if price > 2000:
            raise ValueError("Price exceeds 2000")

        return order_data
