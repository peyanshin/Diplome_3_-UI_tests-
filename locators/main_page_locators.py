from selenium.webdriver.common.by import By

class MainPageLocators:
    #Локаторы главной страницы
    CON_BUTTON = (By.XPATH, "//*[text()='Конструктор']") #кнопка Конструктор
    ORD_LIST_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and text()='Лента Заказов']") #кнопка Лента заказов
    MAI_LOG_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and text()='Конструктор']") #кнопка лого Stellar burger
    PER_ACC_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']") #кнопка Личный кабинет
    BRE_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[text()='Булки']]") #кнопка Булки в Конструкторе
    BRE_TEXT = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and text()='Булки']") #текст Булки в Конструкторе
    BRE_DAD_ITEM = (By.XPATH, "//a[@draggable='true' and contains(@class, 'BurgerIngredient_ingredient') and contains(@href, '/ingredient/') and .//p[contains(text(), 'Флюоресцентная булка')]]") #булка для перетаскивания в заказ
    BRE_COUNTER = (By.XPATH, "//ul[@class='BurgerIngredients_ingredients__list__2A-mT']/a[1]//p[@class='counter_counter__num__3nue1']") #счётчик флюоресцентной булки    
    SAU_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[text()='Соусы']]") #кнопка Соус в Конструкторе
    SAU_TEXT = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and text()='Соусы']") #текст Соусы в Конструкторе
    SAU_DAD_ITEM = (By.XPATH, "//a[@draggable='true' and contains(@class, 'BurgerIngredient_ingredient') and contains(@href, '/ingredient/') and .//p[contains(text(), 'Соус с шипами Антарианского плоскоходца')]]") #соус для перетаскивания в заказ
    FIL_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[text()='Начинки']]") #кнопка Начинки в Конструкторе
    FIL_TEXT = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and text()='Начинки']") #текст Соусы в Конструкторе
    FIL_DAD_ITEM = (By.XPATH, "//a[@draggable='true' and contains(@class, 'BurgerIngredient_ingredient') and contains(@href, '/ingredient/') and .//p[contains(text(), 'Биокотлета из марсианской Магнолии')]]") #начинка для перетаскивания в заказ
    BASKET_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__')]") #корзина заказа
    MAKE_ORD_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") #кнопка оформить заказ
    SIG_ACC_BUTTON = (By.XPATH, "//*[text()='Войти в аккаунт']") #кнопка Войти в аккаунт
