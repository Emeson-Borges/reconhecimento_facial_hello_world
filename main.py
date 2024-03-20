import cv2

# Carregar o classificador pré-treinado para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar a captura de vídeo da webcam
cap = cv2.VideoCapture(0)

# Verificar se a captura de vídeo foi aberta corretamente
if not cap.isOpened():
    print("Erro ao abrir a captura de vídeo!")
    exit()

while True:
    # Ler o próximo frame do vídeo
    ret, frame = cap.read()
    
    # Verificar se o frame foi lido corretamente
    if not ret:
        print("Erro ao ler o frame!")
        break
    
    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostos no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Exibir o frame resultante
    cv2.imshow('Reconhecimento Facial com Python', frame)
    
    # Parar o loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura de vídeo e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()
