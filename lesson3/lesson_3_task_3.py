from address import Address
from mailing import Mailing

to_address = Address("443024", "Самара", "Мира", "9", "25")
from_address = Address("113554", "Москва", "Никольская", "26", "17")

Mailing = Mailing(to_address, from_address, "123", "TRK456789")
print(
    f"Отправление {Mailing.track} из {Mailing.from_address.index},"
    f"{Mailing.from_address.city}, {Mailing.from_address.street},"
    f"{Mailing.from_address.house} - "
    f"{Mailing.from_address.apartment} в {Mailing.to_address.index},"
    f"{Mailing.to_address.city}, {Mailing.to_address.street},"
    f"{Mailing.to_address.house} - {Mailing.to_address.apartment}."
    f"Стоимость {Mailing.cost} рублей."
)
