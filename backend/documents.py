# Document handling simulation

documents = []

def upload_document(title, file_path, user):
    document = {
        "id": len(documents) + 1,
        "title": title,
        "file_path": file_path,
        "uploaded_by": user["username"]
    }
    documents.append(document)

    print(f"Document '{title}' uploaded by {user['username']}")
    return document


def list_documents():
    for doc in documents:
        print(doc)
