import face_recognition

def face_encodings_func(path):
    # Solishtirishni xohlagan yuzlar mavjud rasmlarni yuklash
    person_nin_rasmi = face_recognition.load_image_file(path)
    # Har bir rasm uchun yuzlarning kodlashini olish
    person1_yuz_kodlari = face_recognition.face_encodings(person_nin_rasmi)[0]

    return person1_yuz_kodlari

def find_true_index(lst):
    for i, value in enumerate(lst):
        if value == True:
            return i
    return -1

def is_true_face(array,path):

    # Solishtirishni xohlagan yuzlar mavjud rasmlarni yuklash
    person1_nin_rasmi = face_recognition.load_image_file(path)

    # Har bir rasm uchun yuzlarning kodlashini olish
    person1_yuz_kodlari = face_recognition.face_encodings(person1_nin_rasmi)[0]

    # Yuzlarning kodlarini solishtirish
    natijalar: list = face_recognition.compare_faces(array, person1_yuz_kodlari)
    return find_true_index(natijalar)

