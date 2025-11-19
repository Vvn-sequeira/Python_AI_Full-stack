
def chaiServed(flavor):

    try:
        if flavor == "unknown":
            raise ValueError("we don't serve this Flovor!! ")
        print(f"Preparing {flavor} .....")
    except ValueError as e:
        print(e)
    finally: 
        print("Next customer please ....")

chaiServed("Mango")
chaiServed("unknown")

