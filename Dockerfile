FROM apache/superset:latest

USER root
RUN pip install --upgrade pip

# create superset directory
RUN mkdir -p /app/superset_home
ENV SUPERSET_HOME=/app/superset_home

USER superset

# start superset using the default script
ENTRYPOINT ["/usr/bin/run-server.sh"]
