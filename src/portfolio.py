class Portfolio:
    """
    Simple Portfolio object – na razie tylko nazwa,
    później dodamy pozycje, RWA, PnL itd.
    """

    def __init__(self, name: str):
        self.name = name
        self.positions = []  # tu będą pozycje finansowe

    def __repr__(self):
        return f"<Portfolio {self.name} | positions={len(self.positions)}>"
