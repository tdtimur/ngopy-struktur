from app.jalan import Gang, Raya, Tol
from app.kendaraan import Mobil, Motor


def lalu_lintas(peristiwa=0):
    gang1 = Gang(lebar=1, buntu=False)
    gang2 = Gang(lebar=4, buntu=True)
    gang2.tutup()
    raya = Raya(lebar=12, macet=False)
    tol = Tol(lebar=15, macet=True)

    motor = Motor()
    mobil = Mobil()

    if peristiwa == 0:
        return motor.masuk(gang1)

    elif peristiwa == 1:
        return motor.masuk(gang2)

    elif peristiwa == 2:
        return mobil.masuk(raya)

    elif peristiwa == 3:
        return mobil.masuk(tol)

    else:
        return False


if __name__ == '__main__':
    print(lalu_lintas(peristiwa=0))
    print(lalu_lintas(peristiwa=1))
