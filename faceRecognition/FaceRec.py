# import the face_recognition library 
# pip install face_recognition

import face_recognition
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama3.jpg")
modi_image = face_recognition.load_image_file("modi.jpg")
naga_image = face_recognition.load_image_file("naga.jpg")


biden_encoding = face_recognition.face_encodings(biden_image)[0]
obama_encoding = face_recognition.face_encodings(obama_image)[0]
modi_encoding = face_recognition.face_encodings(modi_image)[0]
naga_encoding = face_recognition.face_encodings(naga_image)[0]

# new_image = face_recognition.load_image_file("newimg.jpg")
# new_encoding = face_recognition.face_encodings(new_image)[0]

new_image = face_recognition.load_image_file("modi2.jpg")
new_encoding = face_recognition.face_encodings(new_image)[0]

results1 = face_recognition.compare_faces([new_encoding], biden_encoding)
results2 = face_recognition.compare_faces([new_encoding], obama_encoding)
results3 = face_recognition.compare_faces([new_encoding], modi_encoding)
results4 = face_recognition.compare_faces([new_encoding], naga_encoding)
if results4[0] == True:
    print("new image is NG")
if results3[0] == True:
    print("new image is Modi")
if results2[0] == True:
    print("new image is Obama")
if results1[0] == True:
    print("new image is Biden")



