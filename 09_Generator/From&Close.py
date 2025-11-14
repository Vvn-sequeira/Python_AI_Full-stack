
def chai():
    yield "Masala chai"
    yield "Cold Coffee"

def Tea():
    yield "Green Tea"
    yield "Sugar Teas"

def Menu():
    yield from chai()
    yield from Tea()

# for chai in Menu():
#     print(next(chai))

chai_menu = Menu()

for chai in chai_menu:
    print(chai)