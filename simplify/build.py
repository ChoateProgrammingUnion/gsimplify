import simplify.auth
import simplify.drive
import simplify.templates


class Builder:
    def __init__(self, drive_str: str, template_dir: str):
        self.creds = simplify.auth.load_creds()
        self.drive = simplify.drive.Drive(drive_str, self.creds)
        self.templator = simplify.templates.Templates(template_dir)

    def build(self):
        for each_doc in drive.docs(public=True):
            render(each_doc)

    def render(self, doc, template = "example.html"):
        document = simplify.docs.Docs(doc, self.creds)
        return document.render(templator.get("example.html"))
