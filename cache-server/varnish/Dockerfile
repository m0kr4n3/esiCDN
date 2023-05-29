FROM varnish:7.3.0

COPY default.vcl /etc/varnish/

USER root

RUN apt update && apt install -y python3 python3-pip

RUN pip3 install flask

RUN mkdir /app

COPY app /app/

EXPOSE 8080

# COPY script.sh /etc/varnish/

# RUN chmod +x /etc/varnish/script.sh

RUN  sh -c 'python3 /app/app.py > /python_app_logs.txt &'

RUN sh -c "varnishncsa -F '%{Varnish:handling}x %U%q %{Varnish:hitmiss}x' > /logs.txt  &"