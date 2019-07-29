import os

# List = os.listdir()


def showdir(lista):
    if len(lista) == 0:
        return "Katalog jest pusty."
    else:
        # itemlist = []
        # itemlist = dict()
        itemlist = ''
        for item in lista:
            if os.path.isdir(item):
                # print(f"Directory: {item}")
                # return f"Directories: {item}"
                # itemlist.append(f"Directory: {item}")
                # itemlist.update({directory: item})
                itemlist += f"Directory: {item}\n"
            elif os.path.isfile(item):
                # print(f"File: {item}")
                # return f"Files: {item}"
                # itemlist.append(f"File: {item})
                # itemlist.update({file: item})
                itemlist += f"File: {item}\n"
        return itemlist
