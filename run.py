import simplify

if __name__ == "__main__":
    service = simplify.auth.load_drive()
    drive = simplify.drive.Drive(drive_id ='0AFB5gF1TxS1vUk9PVA', service =service)
    print(drive.docs())
