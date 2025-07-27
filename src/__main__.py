class Position:
    """Pojedyncza pozycja w portfelu"""
    def __init__(self, name: str, price: float, quantity:int, risk_weight: float):
        self.name = name
        self.price = price
        self.risk_weight = risk_weight
        self.quantity = quantity
        
    def value(self):
        return self.price * self.quantity



    def rwa(self):
        
        return self.value() * self.risk_weight


class Portfolio:
    """Portfel – zbiera pozycje i liczy łączny RWA"""
    def __init__(self, name: str, capital: float):
        self.name = name
        self.positions = []
        self.capital = capital

    def add_position(self, position: Position):
        self.positions.append(position)

    def total_rwa(self):
        return sum(p.rwa() for p in self.positions)
    
    def cet1_ratio(self):
        rwa = self.total_rwa()
        return self.capital / rwa if rwa >0 else 0 

    def stress_test(self, shock: float):
        ssum = 0
        for p in self.positions:
            new_price_p = p.price * (1 + shock)
            new_value_p = new_price_p * p.quantity * p.risk_weight
            ssum += new_value_p
        return ssum


    def __repr__(self):
        return f"<Portfolio {self.name} | positions={len(self.positions)}>"

def main():
    print("Stress Testing Engine – pierwsza wersja")

    # Tworzymy portfel i dodajemy kilka pozycji
    pf = Portfolio("Demo",capital = 100000)

    pf.add_position(Position("APPLE", 200, 13, 0.8))
    pf.add_position(Position("TESLA", 300, 43, 0.8))
    pf.add_position(Position("EY", 300, 28, 0.8))
    print(pf)
    print("Total RWA:", pf.total_rwa())
    print("CET1 ratio:", round(pf.cet1_ratio(),2))
    print("new_walue of portfolio", pf.stress_test(0.4))

    
if __name__ == "__main__":
    main()
