#FROM php:8.1


#RUN apt-get update -y && apt-get install -y openssl zip unzip git libonig-dev nodejs npm  
#RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
#RUN docker-php-ext-install pdo mbstring
#WORKDIR /app
#COPY . /app
#RUN composer install
#RUN npm install
#RUN npm run build

#CMD php artisan serve --host=0.0.0.0 --port=8181
#EXPOSE 8181

# Menggunakan base image PHP 8.1
FROM php:8.1

# Install dependencies
RUN apt-get update -y && apt-get install -y \
    openssl \
    zip \
    unzip \
    git \
    libonig-dev \
    nodejs \
    npm && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Composer secara global
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install PHP extensions yang dibutuhkan
RUN docker-php-ext-install pdo pdo_mysql mbstring

# Set working directory
WORKDIR /app

# Copy seluruh project ke dalam container
COPY . /app

# Install dependencies composer
RUN composer install --no-interaction --prefer-dist --optimize-autoloader

# Install dependencies npm
RUN npm install && npm run build

# Expose port aplikasi Laravel
EXPOSE 8282

# Jalankan aplikasi Laravel menggunakan artisan
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8282"]

