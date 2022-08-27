import cv2
import os
import face_recognition


#Codificar los rostros extraidos
imageFacesPath ="C:/Users/DESPACHO TORRES/Desktop/RECONOCIMIENTO FACIAL/images/faces"

class Info:
    def __init__(self, name, apellido, alias, fecha_de_nacimiento, origen, objetivo, variable):
        self.name = name
        self.apellido = apellido
        self.alias = alias
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.origen = origen
        self.objetivo = objetivo
        self.variable= variable['VALOR1']

Monica = Info('MÓNICA DE LOURDES', 'GUERRERO TORRES',"La bebe", "25/12/2002", "ESPAÑA", "VENGANZA", {'VALOR1':0})
Mama = Info('MÓNICA DE LOURDES', 'TORRES HIDALGO', "Come pollo","20/01/1972", "ECUADOR", "VIVIR", {'VALOR1':0})
Papa = Info('ANTONIO', 'GUERRERO AMBITE', "Pendejo", "12/01/1958", "ESPAÑOL", "VIVIR", {'VALOR1':0})
CapitanAmerica = Info('STEVE', 'ROGERS', "El trasero de america", "Muy viejo", "EEUU", "SALVAR AL MUNDO", {'VALOR1':0})
Data = Info('DATA', '---', "ANDROIDE", "---", "OMICRON THETA", "SER EL MEJOR PERSONAJE DE STAR TRECK", {'VALOR1':0})
Calvito = Info('Jean-Luc', 'Picard', "Capitan", "---", "TIERRA", "NAVEGAR EL ENTERPRISE", {'VALOR1':0})
Tesla = Info('Nikola', 'Tesla', "---", "10/07/1856", "CROACIA", "SU GRAN OBJETIVO ERA DISTRIBUIR LA ENERGÍA ELÉCTRICA A TODO EL MUNDO Y A MUY BAJO COSTE", {'VALOR1':0})
Tia = Info('Carmen', 'Guerrero', "Tiaaaa", "6/10/1947", "ESPAÑA", "---", {'VALOR1':0})




facesEncodings=[]
facesNames = []

for file_name in os.listdir(imageFacesPath):
	image = cv2.imread(imageFacesPath+"/"+ file_name)
	image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

	f_coding = face_recognition.face_encodings(image, known_face_locations=[(0,150,150,0)])[0]
	facesEncodings.append(f_coding)
	facesNames.append(file_name.split('.')[0])



	#cv2.imshow("Image", image)
	#cv2.waitKey(0)
#cv2.destroyAllWindows()


#####################################
#Leyendo video

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)



#DETECCION FACIAL
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
	ret, frame = cap.read()
	if ret == False:
		break
	frame = cv2.flip(frame,1)
	orig = frame.copy()
	faces = faceClassif.detectMultiScale(frame,1.1,5)
	
	for(x,y,w,h) in faces:
		face = orig[y:y+h, x: x+w]
		face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
		actual_face_encoding = face_recognition.face_encodings(face, known_face_locations =[(0,w, h, 0)])[0]
		result= face_recognition.compare_faces(facesEncodings, actual_face_encoding)
		
		if True in result:
			index= result.index(True)
			name = facesNames[index]
			color = (125,220,0)
			
			c = str(facesNames[index])
			if c == "Monica" and Monica.variable == 0:
				print("\n+++++++++++++++++++++++++")
				print ("\nINFORMACIÓN sobre <<Monica>>: ")
				print("NOMBRE:", Monica.name)
				print("APELLIDO:", Monica.apellido)
				print("ALIAS:", Monica.alias)
				print("FECHA DE NACIMIENTO: ", Monica.fecha_de_nacimiento)
				print("PAIS DE ORIGEN: ", Monica.origen)
				print("OBJETIVO: ", Monica.objetivo)
				print("\n+++++++++++++++++++++++++")
				Monica.variable += 1
			elif c == 'Mama' and Mama.variable == 0:
				print("\n+++++++++++++++++++++++++")
				print ("\nINFORMACIÓN sobre <<Mamá>>: ")
				print("NOMBRE: ", Mama.name)
				print("APELLIDO:", Mama.apellido)
				print("ALIAS:", Mama.alias)
				print("FECHA DE NACIMIENTO: ", Mama.fecha_de_nacimiento)
				print("PAIS DE ORIGEN: ", Mama.origen)
				print("\n+++++++++++++++++++++++++\n")
				Mama.variable += 1
			elif c == 'Papa' and Papa.variable == 0:
				print("\n+++++++++++++++++++++++++")
				print ("\nINFORMACIÓN sobre <<Papá>>: ")
				print("NOMBRE: ", Papa.name)
				print("APELLIDO:", Papa.apellido)
				print("ALIAS:", Papa.alias)
				print("FECHA DE NACIMIENTO: ", Papa.fecha_de_nacimiento)
				print("PAIS DE ORIGEN: ", Papa.origen)
				print("\n+++++++++++++++++++++++++\n")
				Papa.variable += 1
			elif c == 'CapitanAmerica' and CapitanAmerica.variable == 0:
				print("\n+++++++++++++++++++++++++")
				print ("\nINFORMACIÓN sobre <<CapitanAmerica>>: ")
				print("NOMBRE: ", CapitanAmerica.name)
				print("APELLIDO:", CapitanAmerica.apellido)
				print("ALIAS:", CapitanAmerica.alias)
				print("FECHA DE NACIMIENTO: ", CapitanAmerica.fecha_de_nacimiento)
				print("PAIS DE ORIGEN: ", CapitanAmerica.origen)
				print("OBJETIVO: ", CapitanAmerica.objetivo)
				print("\n+++++++++++++++++++++++++\n")
				CapitanAmerica.variable += 1
			elif c == 'Tesla' and Tesla.variable == 0:
				print("\n+++++++++++++++++++++++++")
				print ("\nINFORMACIÓN sobre <<Tesla>>: ")
				print("NOMBRE: ", Tesla.name)
				print("APELLIDO:", Tesla.apellido)
				print("ALIAS:", Tesla.alias)
				print("FECHA DE NACIMIENTO: ", Tesla.fecha_de_nacimiento)
				print("PAIS DE ORIGEN: ", Tesla.origen)
				print("OBJETIVO: ", Tesla.objetivo)
				print("\n+++++++++++++++++++++++++\n")
				Tesla.variable += 1
			elif c == 'Tia' and Tia.variable == 0:
				print("\n+++++++++++++++++++++++++")
				print ("\nINFORMACIÓN sobre <<Tia>>: ")
				print("NOMBRE: ", Tia.name)
				print("APELLIDO:", Tia.apellido)
				print("ALIAS:", Tia.alias)
				print("FECHA DE NACIMIENTO: ", Tia.fecha_de_nacimiento)
				print("PAIS DE ORIGEN: ", Tia.origen)
				print("\n+++++++++++++++++++++++++\n")
				Tia.variable += 1
		else:
			name ="Desconocido"
			color = (50,50,255)	

		cv2.rectangle(frame, (x,y+h), (x+w,y+h+30), color, -1)
		cv2.rectangle(frame, (x,y), (x+w,y+h), color, 2)
		cv2.putText(frame,name,(x,y+h+25),2,1,(255,255,255),2,cv2.LINE_AA)

 

	cv2.imshow("Frame", frame)
	k= cv2.waitKey(1) & 0xFF
	if k == ord('s'):
		break

cap.release()
cv2.destroyAllWindows()
