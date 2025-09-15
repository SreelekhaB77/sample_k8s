FROM postgres:14-alpine

# Set environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=app_db

# Copy init SQL to automatically run at container startup
COPY init.sql /docker-entrypoint-initdb.d/
