import goslate

def Trans(text, last):
    gs = goslate.Goslate()
    translate = gs.translate(text, last)

    return translate
