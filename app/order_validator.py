class OrderValidator:
    def validate(self, order_data):
        # 檢查必要欄位是否存在且不為空
        required_fields = ['id', 'name', 'address', 'price', 'currency']
        for field in required_fields:
            if field not in order_data or not order_data[field]:
                return False

        # 驗證 id 的格式
        if not isinstance(order_data['id'], str) or not order_data['id'].strip():
            return False

        # 驗證 name 的格式
        if not isinstance(order_data['name'], str) or not order_data['name'].strip():
            return False

        # 驗證 address 的格式
        address_required_fields = ['city', 'district', 'street']
        for field in address_required_fields:
            if field not in order_data['address'] or not isinstance(order_data['address'][field], str) or not \
                    order_data['address'][field].strip():
                return False

        # 驗證 price 的格式
        if not isinstance(order_data['price'], str):
            return False
        try:
            float(order_data['price'])
        except ValueError:
            return False

        # 驗證 currency 的格式
        if not isinstance(order_data['currency'], str) or not order_data['currency'].strip():
            return False

        return True
