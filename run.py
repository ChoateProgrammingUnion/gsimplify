import pprint

import simplify

if __name__ == "__main__":
    creds = simplify.auth.load_creds()
    drive = simplify.drive.Drive("0AFB5gF1TxS1vUk9PVA", creds)
    for each_doc in drive.docs(public=True):
        document = simplify.docs.Docs(each_doc, creds)
        pprint.pprint(document)

