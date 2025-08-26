import allure

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Страница оформления заказа"""

    def __init__(self, page):
        super().__init__(page)
        self._address_delivery = self.page.locator("#address_delivery")
        self.delivery_first_name = self._address_delivery.locator(".address_firstname")
        self.delivery_address = self._address_delivery.locator(".address_address1")
        self.delivery_city = self._address_delivery.locator(".address_city")
        self.delivery_country = self._address_delivery.locator(".address_country_name")
        self.delivery_phone = self._address_delivery.locator(".address_phone")
        self.cart = self.page.locator("#cart_info")
        self.btn_place_order = self.page.get_by_role("link", name="Place Order")

    def check_items_in_cart(self, expect_items: list):
        """Проверка товаров в корзине"""
        with allure.step("Проверяем добавленный товар в корзине"):
            current_items = self.page.query_selector_all("tbody tr[id^='product-']")
            items_info = []

            # получение всех товаров из корзины
            for item in current_items:
                item_name = item.query_selector(".cart_description h4 a").inner_text()
                item_price = item.query_selector(".cart_price p").inner_text()
                item_qty = item.query_selector(".cart_quantity button.disabled").inner_text()
                item_total = item.query_selector(".cart_total_price").inner_text()

                items_info.append({
                    "name": item_name,
                    "price": item_price,
                    "quantity": item_qty,
                    "total": item_total,
                })

            for expect_item in expect_items:
                for elem in items_info:
                    if elem["name"] == expect_item:
                        pass

    def place_order(self):
        """Нажимает на кнопку 'Place_order'"""
        with allure.step("Нажимаем на кнопку 'Place_order'"):
            self.btn_place_order.click()
