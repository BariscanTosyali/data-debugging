# pylint: disable=missing-docstring

import sys

def full_name(first_name, last_name):
    """returns the full name without extra spaces"""
    # capitalize() metoduyla isimleri düzenliyoruz
    # .strip() ile eğer isimlerden biri boşsa oluşacak kenar boşluklarını temizliyoruz
    name = f"{first_name.capitalize()} {last_name.capitalize()}".strip()

    return name

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Hiç argüman girilmezse: "Hello !"
        print(f'Hello {full_name("", "")}!')
    elif len(sys.argv) == 2:
        # Sadece ilk isim girilirse: "Hello John!"
        print(f'Hello {full_name(sys.argv[1], "")}!')
    else:
        # İki isim de girilirse: "Hello John Lennon!"
        print(f"Hello {full_name(sys.argv[1], sys.argv[2])}!")
