def booksEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "title":  item["title"],
        "author":   item["author"],
        "number_pages":  item["number_pages"],
        "publisher":  item["publisher"]
    }

def listOfBookEntity(db_item_list) -> list:
    list_book_entity = []
    for item in db_item_list:
        list_book_entity.append(booksEntity(item))
    return list_book_entity