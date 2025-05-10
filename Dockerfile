# Imagen base con NGINX ligero
FROM nginx:alpine

# Crear una carpeta (opcional, solo si quieres organizar)
# RUN mkdir /usr/share/nginx/html/images

# Copiar todas las imágenes JPG al directorio público de NGINX
COPY *.jpg /usr/share/nginx/html/

# Exponer el puerto por defecto de NGINX
EXPOSE 80
