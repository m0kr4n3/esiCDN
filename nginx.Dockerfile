FROM nginx:1.23

COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir /usr/share/nginx/content

COPY content /usr/share/nginx/content/

COPY certs/* /etc/ssl/

EXPOSE 8000


