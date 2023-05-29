FROM nginx:1.23

COPY nginx.conf /etc/nginx/nginx.conf

COPY certs/* /etc/ssl/

EXPOSE 8000


