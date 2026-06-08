#class method w/o parameter
class Mobile:
    @classmethod
    def show_model(cls):
        print("RealMe X")
realme = Mobile()
Mobile.show_model()