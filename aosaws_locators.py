from faker import Faker

fake = Faker(locale='en_CA')

# ------------------ locators section-------------------------------
app = 'Advantage Online Shopping'
aos_url = 'https://advantageonlineshopping.com/#/'
aos_home_page_title = ' Advantage Shopping'
aos_add_user = 'https://advantageonlineshopping.com/#/register'
aos_add_user_title = ' Advantage Shopping'

# -------------------- data section ---------------------------------
firstname = fake.first_name()
lastname = fake.last_name()
full_name = f'{firstname} {lastname}'
phone = fake.phone_number()
username = f'{firstname}{lastname}'.lower()[:10]
password = fake.password()
confirm_password = f'{password}'
email = fake.email()
country = fake.current_country()
city = fake.city()
address = fake.street_address()
province = fake.province_abbr()
postcode = fake.postcode()

# -------------------- Text ---------------------------------
speakers = f'Speakers'.upper()
tablets = f'Tablets'.upper()
laptops = f'Laptops'.upper()
mice = f'Mice'.upper()
headphones = f'Headphones'.upper()

# -------------------- Nav Link ---------------------------------
special_offers = f'Special Offers'.upper()
popular_items = f'Popular Items'.upper()
contact_us = f'Contact Us'.upper()

# -------------------- Messages ---------------------------------
messages = fake.text()

# -------------------- Buttons ---------------------------------
continue_shopping = f' CONTINUE SHOPPING '

# -------------------- Add Cart ---------------------------------
shop_tablets = 'https://advantageonlineshopping.com/#/category/Tablets/3'
shop_hp_tablet = 'https://advantageonlineshopping.com/#/product/16'
shop_cart = 'https://advantageonlineshopping.com/#/shoppingCart'
order_payment = 'https://advantageonlineshopping.com/#/orderPayment'
tablet_name = ' HP ELITEPAD 1000 G2 TABLET '
add_cart = 'ADD TO CART'

# -------------------- My Orders and Accounts ---------------------------------
my_orders = 'https://advantageonlineshopping.com/#/MyOrders'
my_account= 'https://advantageonlineshopping.com/#/myAccount'
#no_orders = ' - No orders - '


print(firstname, lastname, phone, username, password, email)
