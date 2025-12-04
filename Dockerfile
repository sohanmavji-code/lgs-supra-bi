FROM apache/superset:3.1.0

USER root

# Upgrade pip
RUN pip install --upgrade pip

# Superset home directory
ENV SUPERSET_HOME=/app/superset_home
RUN mkdir -p /app/superset_home && chown -R superset:superset /app/superset_home

# Copy Superset config
COPY superset_config.py /app/pythonpath/superset_config.py

USER superset

# Initialize Superset on container start
CMD superset db upgrade && \
    superset fab create-admin \
      --username ${ADMIN_USERNAME:-admin} \
      --password ${ADMIN_PASSWORD:-admin} \
      --firstname Admin \
      --lastname User \
      --email admin@lgs.com && \
    superset init && \
    /usr/bin/run-server.sh
