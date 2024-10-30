import yaml

def replace_values_in_yaml(input_file, output_file, replacements):
    # Membaca file YAML asli
    with open(input_file, 'r') as file:
        data = yaml.safe_load(file)
    
    # Melakukan penggantian nilai sesuai dengan dictionary replacements
    for service, params in replacements.items():
        if service in data.get('services', {}):
            for key, new_value in params.items():
                # Mengganti environment variables atau sub-key lainnya
                if 'environment' in data['services'][service]:
                    for i, env_var in enumerate(data['services'][service]['environment']):
                        if env_var.startswith(f"{key}="):
                            data['services'][service]['environment'][i] = f"{key}={new_value}"
                else:
                    # Jika parameter bukan environment, langsung mengganti
                    data['services'][service][key] = new_value
    
    # Menyimpan hasil modifikasi ke file YAML baru
    with open(output_file, 'w') as file:
        yaml.dump(data, file)

# Definisikan nilai-nilai yang akan diubah
replacements = {
    "app": {
        "DB_HOST": "db",
        "DB_PORT": "3306",
        "DB_USER": "new_user",
        "DB_PASS": "new_password",
    },
    "db": {
        "image": "mysql:8.0",
        "volumes": "mysql_data:/var/lib/mysql",
        "MYSQL_ROOT_PASSWORD": "new_root_password",
        "MYSQL_USER": "new_user",
        "MYSQL_PASSWORD": "new_password",
        "MYSQL_DATABASE": "new_database"
    }
}

# Memanggil fungsi untuk melakukan replace
replace_values_in_yaml('docker-compose.yml', 'docker-compose-modified.yml', replacements)
