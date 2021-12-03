from kosar import Kosar


class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    def __init__(self,lista: list)->None:
        self.lista = lista
        kosar = []
        for sor in lista:
            if sor[0] == "F":
                kos = kosar(sor[0])
                kosar.append(kos)
            if sor[0] == "toll":
                kos = kosar(sor[0])
                kosar.append(kos)
            if sor[0] == "HB ceruza":
                kos = kosar(sor[0])
                kosar.append(kos)
            if sor[0] == "Colostok":
                kos = kosar(sor[0])
                kosar.append(kos)
            if sor[0] == "kefe":
                kos = kosar(sor[0])
                kosar.append(kos)
            if sor[0] == "szatyor":
                kos = kosar(sor[0])
                kosar.append(kos)
            if sor[0] == "doboz":
                kos = kosar(sor[0])
                kosar.append(kos)
            if sor[0] == "ceruzaelem":
                kos = kosar(sor[0])
                kosar.append(kos)
            if sor[0] == "csavarkulcs":
                kos = kosar(sor[0])
                kosar.append(kos)
            if sor[0] == "filctoll":
                kos = kosar(sor[0])
                kosar.append(kos)
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """
        pass

    def feladat_1(self, filepath: str) -> None:
        lista = []
        try:
            f = open("kosar.txt","r",encoding="UTF-8")
            for sor in f:
                sor = sor.strip().split()
                lista.append(sor)
            f.close()
        except FileNotFoundError:
            print("Hiba!")
        return None
        pass

    def feladat_2(self,lista:list) -> None:
        """
        Kiírja, hányan fizettek a pénztárnál.
        """
        print("2. feladat:")
        sum = 0
        for sor in lista:
            sum = sum + sor.pay
        print(f"{sum}-en fizettek a pénztárnál")
        pass

    def feladat_3(self,lista:list) -> None:
        i = 0
        for sor in lista:
            if sor == "F":
                sor_sz = i + sor[0]
            """Bekéri egy vásárlás sorszámát és kiírja:
            - hány darab árucikk volt a kosárban,
            - mely árucikkekből és milyen mennyiségben vásároltak,
            - a vásárlás összegét.
        """
        print("3. feladat:")
        sorszam = input("Kérem adja meg a vásárlás sorszámát: ")

        pass

    def feladat_4(self) -> None:
        """
        Bekéri egy árucikk nevét és kiírja:
            - melyik vásárlásnál vettek először a termékből
            - melyik vásárlásnál vettek utoljára a termékből
            - összesen hány alkalommal vásároltak a termékből
        """
        pass

    def feladat_5(self, filepath: str) -> None:
        """
        Elmenti a megadott fájlba a vásárlásonként fizetendő összeget.
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
pass