import json
from datetime import date

# TODO: Dodati type hinting na sve funkcije

OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers: list, products: list, customers: list) -> None:
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    # Omogućite unos kupca
    # Izračunajte sub_total, tax i total
    # Dodajte novu ponudu u listu offers
    
    
    print("\nUneseni kupci:")
    print(100*"-")
    new_offer = {}
    for customer in customers:
        print(customer['name'])
    print()
    while True:
        customer_name = input('Unesi ime kupca: ')
        is_customer = False

        for customer in customers:
            if customer["name"].lower() == customer_name.lower():
                is_customer = True
                new_offer["offer_number"] = len(offers) + 1
                new_offer["customer"] = customer["name"]
                today = date.today()
                today = today.strftime("%y-%m-%d")
                new_offer["date"] = today
                new_offer["items"] = []
        
        if is_customer == False:
            print("Kupac s tim imenom ne postoji.\n")
        else:
            break

    print("\nUneseni proizvodi:")
    print(100*"-")
    for element in products:
        print(f"ID proizvoda: {element["id"]}\t Naziv: {element["name"]}\t\t\t\t", end = "")
        if len(element["name"]) > 15:
            print(f"Cijena: {element["price"]:.2f}")
        elif len(element["name"]) > 7:
            print(f"\tCijena: {element["price"]:.2f}")
        else:
            print(f"\t\tCijena: {element["price"]:.2f}")
    print()


    product_flag = True
    current_item = {}
    sub_total = 0

    while product_flag:
        product_id = int(input('Unesi ID proizvoda: '))
        is_product = False
        
        if product_id <= len(products) and product_id >0:
            is_product = True
            current_item["product_id"] = product_id
            current_item["product_name"] = products[product_id-1]["name"]
            current_item["description"] = products[product_id-1]["description"]
            current_item["price"] = products[product_id-1]["price"]
                

        if is_product == False:
            print("Proizvod sa tim ID ne postoji.")
        else:
            while True:
            
                quantity = int(input('Unesi kolicinu odabranog proizvoda: '))
                if quantity > 0:
                    current_item["quantity"] = quantity
                    current_item["item_total"] = quantity * products[product_id-1]["price"]
                    new_offer["items"].append(current_item.copy())
                    sub_total += quantity * products[product_id-1]["price"]
                    break
                else:
                    print("Unesite količinu veću od nule.")

        while True:
            dodati_jos = input("\nŽelite li dodati još proizvoda na ponudu? (da/ne) ")
            if dodati_jos == "ne":

                product_flag = False
                break
            elif dodati_jos == "da":
                break
            else:
                print("Molim unesite da ili ne.")

    new_offer["sub_total"] = sub_total
    new_offer["tax"] = sub_total * 0.1
    new_offer["total"] = sub_total + new_offer["tax"]
    offers.append(new_offer)
    print("Ponuda unesena!")


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products: list) -> None:
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    while True:
        print()
        print("Želite li dodati novi ili promijeniti postojeći proizvod?:")
        print("1. Kreiraj novi proizvod")
        print("2. Ažuriraj proizvod")
        print("3. Odustani")
        choice = input("Odabrana opcija: ")
        print()

        if choice == "1":
            print()
            product_name = input("Unesi ime proizvnoda: ")
            product_desc = input("Unesi opis proizvnoda: ")
            product_price = float(input("Unesi cijenu proizvnoda: "))
            product_id = len(products) + 1
            products.append({
                "id": product_id,
                "name": product_name,
                "description": product_desc,
                "price": product_price
            })
            break

        elif choice == "2":
            print(100 * "-")
            for product in products:
                print(product)
            #print(products)
            print(100 * "-")
            while True:
                product_id = int(input("Unesi id proizvnoda kojega želite ažurirati: "))
                if product_id >= 1 and product_id <= len(products):
                    break
                else:
                    print(f"Proizvod sa tim ID ne postoji, unesite broj od 1 do {len(products)}")
            product_name = input("Unesi ažurirano ime proizvnoda: ")
            product_desc = input("Unesi ažurirani opis proizvnoda: ")
            product_price = float(input("Unesi ažuriranu cijenu proizvnoda: "))
            products[product_id - 1] = ({
                "id": product_id,
                "name": product_name,
                "description": product_desc,
                "price": product_price
            })
            break
        elif choice == "3":
            break
        else:
                print("Krivi izbor. Pokusajte ponovno.")

    


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers) -> None:
    """
    Allows the user to add a new customer or view all customers.
    """
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    while True:
        print()
        print("Izbornik: ")
        print("1. Dodaj novog kupca")
        print("2. Prikaži sve kupce")
        print("3. Odustani")

        choice = input("Odabrana opcija: ")
        print()

        if choice == "1":
            customer_name = (input("Unesi ime kupca: "))
            customer_email = (input("Unesi email kupca: "))
            customer_vatid = (input("Unesi VAT-ID kupca: "))
            customers.append({
                "name": customer_name,
                "email": customer_email,
                "vat_id": customer_vatid
            })
            break

        elif choice == "2":
            print(100*"-", end="")
            for customer in customers:
                print(f"\nIme kupca: {customer["name"]}\nEmail kupca: {customer["email"]}\nVAT-ID kupca: {customer["vat_id"]}\n")
            print(100*"-", end="")
            break
        elif choice == "3":
            break
        else:
                print("Krivi izbor. Pokusajte ponovno.")


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers) -> None:
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    
    while True:
        print()
        print("Izbornik:")
        print("1. Prikaži sve ponude")
        print("2. Prikaži sve ponude za određeni mjesec")
        print("3. Prikaži određenu ponudu")
        print("4. Odustani")
        
        choice = input("Odabrana opcija: ")
        print()

        if choice == "1":
            for offer in offers:
                print(100*"-")
                print_offer(offer)
            print(100*"-")
            break
        elif choice == "2":
            while True:
                month_input = input("Unesite željenu godinu i mjesec u formatu YYYY-MM: ")
                if int(month_input[:4]) >= 2000 and int(month_input[:4]) <= 2024 and int(month_input[5:]) >= 1 and int(month_input[5:]) <=12 and month_input[4] == "-":
                    for offer in offers:
                        if month_input == offer['date'][:7]:
                            print_offer(offer)
                            print(100*"-")
                    break
                else:
                    print("Krivi format datuma, molim unesite godinu i mjesec u formatu YYYY-MM")
            break
        elif choice == "3":
            offer_num = int(input("Odaberite broj ponude: "))
            print(100*"-")
            print_offer(offers[offer_num - 1])
            print(100*"-")
            break
        elif choice == "4":
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")
            



# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer: dict) -> None:
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("Offers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
