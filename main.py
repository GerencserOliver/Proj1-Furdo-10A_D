from Megoldas import Megoldas


def main() -> None:
    # 1. feladat
    m: Megoldas = Megoldas('furdoadat.txt')

    # 2. feladat
    print('2. feladat')
    print(f'Az első vendég {m.kiiras_oraban(m.elso_oltozo_kilepes)}-kor lépett ki az öltözőből.')
    print(f'Az utolsó vendég {m.kiiras_oraban(m.utolso_oltozo_kilepes)}-kor lépett ki az öltözőből.')


if __name__ == "__main__":
    main()
