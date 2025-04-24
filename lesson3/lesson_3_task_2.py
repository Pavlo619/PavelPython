from Smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 12", "+79924749130"))
catalog.append(Smartphone("Apple", "iPhone 14", "+79189457471"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79181427172"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 11", "+79121113473"))
catalog.append(Smartphone("Google", "Pixel 8", "+79289347474"))
catalog.append(Smartphone("Sony", "Xperia 10", "+79226513231"))

for phone in catalog:
    print(phone)