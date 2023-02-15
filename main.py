from Megoldas import Megoldas


def main() -> None:
    # 1. feladat
    m: Megoldas = Megoldas('furdoadat.txt')

    # 2. feladat
    print('2. feladat')
    print(f'Az első vendég {m.kiiras_oraban(m.elso_oltozo_kilepes)}-kor lépett ki az öltözőből.')
    print(f'Az utolsó vendég {m.kiiras_oraban(m.utolso_oltozo_kilepes)}-kor lépett ki az öltözőből.')

    # 3. feladat
    print('\n3. feladat')
    print(f'A fürdőben {m.vendegek()} vendég járt csak egy részlegen.')

    # 4. feladat
    print('\n4. feladat')
    print(f'{m.kello_azonosito}. vendég {"%.0f" % m.legtovabb_oraban}:{"%.0f" % m.legtovabb_percben}:{"%.0f" % m.legtovabb_mpben}')

    # 5. feladat
    print('\n5. feladat')
    print(f'6-9 óra között {m.vendegek_erkezes[0]} vendég')
    print(f'9-16 óra között {m.vendegek_erkezes[1]} vendég')
    print(f'16-20 óra között {m.vendegek_erkezes[2]} vendég')


if __name__ == "__main__":
    main()
