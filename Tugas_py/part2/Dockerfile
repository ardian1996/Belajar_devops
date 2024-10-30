# Gunakan image Python sebagai base
FROM python:3.9-slim

# Menetapkan direktori kerja
WORKDIR /app

# Menyalin file Python dan docker-compose.yml asli ke dalam container
COPY replace_yaml.py .
COPY docker-compose.yml .

# Menginstal library pyyaml yang diperlukan
RUN pip install pyyaml

# Menjalankan skrip Python untuk memodifikasi docker-compose.yml
CMD ["python", "replace_yaml.py"]
