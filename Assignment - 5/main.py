from device import Device
from smartphone import Smartphone
from laptop import Laptop
from tablet import Tablet
from cart import Cart

if __name__ == '__main__':

    shopping_cart = Cart()

    device = Device('Apple Watch', 534,20, '5' )
    print(device)
    print(device.is_available(20))
    print(device.is_available(25))
    shopping_cart.add_device(device=device, amount=20)
    print()

    smartphone = Smartphone('IPhone', 1000, 100, '10', 6, 8)
    print(smartphone.is_available(20))
    smartphone.apply_discount(20)
    smartphone.reduce_stock(10)
    shopping_cart.add_device(device=smartphone, amount=50)
    print(smartphone.make_call())
    print(smartphone.install_app())
    smartphone.display_info()
    print(smartphone)

    laptop = Laptop('Mac', 2000, 10, 20, 8, 'M3')
    print(laptop.is_available(200))
    laptop.apply_discount(30)
    # if shopping_cart.add_device(laptop, 11) is not True:
    #     print(shopping_cart.add_device(laptop, 11))
    print(laptop)

    tablet = Tablet('IPad', 1500, 1, 10, 4000, 0.8)
    print(tablet)

    # try:
    #     shopping_cart.add_device(tablet, 10)
    # except ValueError as e:
    #     print(e)
    shopping_cart.add_device(laptop, 11)
    shopping_cart.add_device(tablet, 2)
    shopping_cart.print_items()
    print()

    shopping_cart.remove_device(smartphone, 6)
    shopping_cart.print_items()
    print()

    shopping_cart.add_device(laptop, 5)
    shopping_cart.add_device(tablet, 1)
    shopping_cart.print_items()
    shopping_cart.get_total_price()
    print()

    shopping_cart.remove_device(laptop, 3)
    shopping_cart.print_items()
    print()

    print(shopping_cart.checkout())

    print(device)
    print(smartphone)
    print(laptop)
    print(tablet)


