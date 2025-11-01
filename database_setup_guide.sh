# 1. Install dependencies
pip install sqlalchemy psycopg2-binary

# 2. Make sure PostgreSQL is running
docker compose up -d postgres

# 3. Create the tables
python create_tables.py

# 4. Test the table
python test_student_table.py

# 5. Test CRUD operations
python student_repository.py
