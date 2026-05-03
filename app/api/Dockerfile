# this is a multi-stage build Dockerfile
# this is stage 1; only installs dependencies, and is a temporary stage

FROM python:3.11-slim AS builder		
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# this is stage 2; starts from a clean slate with just the packages and code, no cache
# or any unncessary build tools

FROM python:3.11-slim				
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
