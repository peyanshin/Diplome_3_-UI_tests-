from selenium.webdriver.common.by import By

class OrdersListPageLocators:
    #Окно Ленты заказов
    ORD_LIST_TEXT = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5' and text()='Лента заказов']") #заголовок Лента заказов в окне Лента заказов
    ORD_NUM_TEXT = (By.XPATH, "//p[contains(@class, 'OrderFeed_number') and contains(@class, 'text') and contains(@class, 'text_type_digits-large')]") #текст счётчика всех заказов
    ORD_DAY_NUM_TEXT = (By.XPATH, "//div/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']") #текст счётчика заказов за день
    ORD_NUM_WORK_TEXT = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li.text.text_type_digits-default.mb-2") #Номер заказа в списке "В работе"
    