import pprint
from typing import Optional

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import Resource, build
from pydantic import BaseModel

from simplify.typedefs import DocType, FolderType


class Docs:
    def __init__(self, doc: DocType, creds):
        self.document = doc
        self.service = build('docs', 'v1', credentials=creds)
        self.get(doc.id)
        self.parse()

    def __str__(self):
        return self.document.content

    def __repr__(self):
        return pprint.pformat(self.document.dict())

    def get(self, id=str) -> dict:
        """
        Grabs the document from Google Docs
        """
        self.document.content = self.service.documents().get(documentId=id).execute()
        return self.document.content

    def parse(self):
        """
        Parses document into a dict-like parse tree.
        """
        try:
            for section in self.document.content.get("body").get("content"):
                if "paragraph" in section:
                    paragraph = section.get("paragraph")
                    style = paragraph.get("paragraphStyle").get("namedStyleType")
                    content = "".join([elm.get("textRun").get("content") for elm in paragraph.get("elements")])
                    if style == "TITLE":
                        self.document.title = paragraph.get("elements")[0].get("textRun").get("content")
                    elif style == "HEADING_1":
                        pass
                    elif style == "NORMAL_TEXT":
                        pass

        except AttributeError:
            pass
