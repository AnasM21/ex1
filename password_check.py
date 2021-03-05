def main():
    tenta = 1

    while tenta < 4:
        pwd = input("saisir votre mot de passe :  ")
        if pwd == "abc123":
            print("Bienvenue, authnetification reussie !")
            break

        elif pwd != "abc123":
            print("mot de passe erroné ")
        tenta = tenta + 1
    else:
        print("vous avez depassé le nbr de tentatives possibles")


if __name__ == '__main__':
    main()