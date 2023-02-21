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
    print('A legtöbb időt eltöltő vendég:')
    print(f'{m.adat_ido_kiiras}')

    # 5. feladat
    print('\n5. feladat')
    print(f'6-9 óra között {m.vendegek_erkezes[0]} vendég')
    print(f'9-16 óra között {m.vendegek_erkezes[1]} vendég')
    print(f'16-20 óra között {m.vendegek_erkezes[2]} vendég')

    # 7. feladat
    print('\n7. feladat')
    print(f'Uszoda: {len(m.bent_voltak[0])}')
    print(f'Szauna: {len(m.bent_voltak[1])}')
    print(f'Gyógyvizes medencék: {len(m.bent_voltak[2])}')
    print(f'Strand: {len(m.bent_voltak[3])}')


if __name__ == "__main__":
    main()
