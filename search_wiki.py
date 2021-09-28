import wikipedia
def search(language,text):
    if language=="Uz":
        wikipedia.set_lang("uz")
        try:
            response=wikipedia.summary(text)
            response=f"Quyidagi ma'lumot topildi:\n{response}"
        except:
            response="Afsuski ma'lumot topilmadi😐"
    elif language=="Eng":
        wikipedia.set_lang("en")
        try:
            response=wikipedia.summary(text)
            response=f"This information has been found:\n{response}"
        except:
            response="Nothing has been found😐"
            
    else:
        wikipedia.set_lang("ru")
        try:
            response=wikipedia.summary(text)
        except:
            response="Ничего не найдено😐"
    return response
        