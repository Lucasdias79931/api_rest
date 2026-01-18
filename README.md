# API REST WITHOUT FRAMEWORK OR ORM

# Database Migrations

This project uses plain SQL migrations, without ORM or migration framework.
All migrations are executed sequentially using a shell script.

Running Migrations

1. Export environment variables

Load variables from .env into the current shell session:
    ```sh
        export $(grep -v '^#' .env | xargs)
    ```

2. Give execution permission to the script

This only needs to be done once:    
    ```sh
        chmod +x scripts/migrate.sh

    ```

3. Run migrations

From the project root:
    ```sh
        ./scripts/migrate.sh
    ```