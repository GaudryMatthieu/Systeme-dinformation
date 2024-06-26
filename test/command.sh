# How to build the image of prometheus
docker pull prom/prometheus:latest

# How to run the docker prometheus container
docker run -p 9090:9090 prom/prometheus

docker run -d -v "$pwd/test/prometheus.yml:/etc/prometheus/prometheus.yml" -p 9090:9090 prom/prometheus

# Docker image for alert with prometheus
docker pull prom/alertmanager:latest

# command to start the container
docker run --name alertmanager -d -p 127.0.0.1:9093:9093 quay.io/prometheus/alertmanager

docker run -d -v "$pwd/test/prometheus.yml:/etc/prometheus/prometheus.yml" -v C:\Users\matth\HEXAGONE\2e-annee\systeme-dinformation\cours\test\prometheus.yml -p 9090:9090 prom/prometheus

# command to build Grafana (OPtional)
docker pull grafana/grafana:latest

# Run Grafana (login: admin/admin)
docker run -d -p 3000:3000 --name=grafana grafana/grafana-enterprise