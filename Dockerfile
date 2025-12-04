FROM apache/superset:latest

# Set Superset home
ENV SUPERSET_HOME=/app/superset_home

# Switch to root to install pip upgrades
USER root
RUN pip install --upgrade pip

# Create directory for superset
RUN mkdir -p /app/superset_home
RUN chown -R superset:superset /app/superset_home

# Switch to superset user
USER superset

# Start Superset server
ENTRYPOINT ["/usr/bin/run-server.sh"]
