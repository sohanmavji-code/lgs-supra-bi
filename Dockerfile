FROM apache/superset:latest

# Superset home directory
ENV SUPERSET_HOME=/app/superset_home

# Switch to root
USER root
RUN mkdir -p /app/superset_home
RUN chown -R superset:superset /app/superset_home

# Copy your custom Superset config
COPY superset_config.py /app/pythonpath/superset_config.py

USER superset

# Start the server
ENTRYPOINT ["/usr/bin/run-server.sh"]
