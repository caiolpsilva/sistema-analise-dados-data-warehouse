# run.py
from src.api.api import app
from src.databases.objectdb import init_objectdb
from src.databases.datawarehouse import DataWarehouse
import os

def init_databases():
    """Initialize all database connections and schemas."""
    print("Inicializando bancos de dados...")
    
    # Initialize SQLite databases
    init_objectdb()
    
    # Initialize Data Warehouse
    dw = DataWarehouse()
    
    print("Bancos de dados inicializados com sucesso!")

def main():
    """Main application entry point."""
    try:
        # Create necessary directories if they don't exist
        os.makedirs('src/databases', exist_ok=True)
        
        # Initialize databases
        init_databases()
        
        # Start Flask application
        print("Iniciando servidor na porta 8000...")
        app.run(host='0.0.0.0', port=8000, debug=True)
        
    except Exception as e:
        print(f"Erro ao iniciar a aplicação: {e}")
        raise

if __name__ == "__main__":
    main()
