# Detecção de Rostos em Tempo Real usando OpenCV

Este é um código Python que utiliza a biblioteca OpenCV para realizar a detecção de rostos em tempo real usando a webcam do computador. Ele detecta rostos em um vídeo capturado pela webcam e desenha retângulos ao redor dos rostos detectados.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. Você também precisará instalar a biblioteca OpenCV. Você pode instalá-lo via pip usando o seguinte comando:


## Como Usar

1. Clone este repositório para o seu sistema.

2. Navegue até o diretório do projeto no terminal.

3. Execute o script Python usando o seguinte comando:



4. Uma janela será aberta mostrando a saída da webcam. Os rostos detectados serão destacados com retângulos azuis.

5. Pressione a tecla 'q' para sair do programa.

## Explicação do Código

O código Python (`face_detection.py`) consiste em:

- Carregar um classificador pré-treinado para detecção de rostos.
- Inicializar a captura de vídeo da webcam.
- Ler os frames da câmera, convertê-los para escala de cinza e detectar rostos em cada frame.
- Desenhar retângulos ao redor dos rostos detectados.
- Exibir o frame resultante com os rostos detectados em uma janela.
- Continuar este processo até que a tecla 'q' seja pressionada.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorar este código, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
