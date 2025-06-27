FROM python:3.11-slim

WORKDIR /app

COPY . .

# Étape 1 : Installer les dépendances système
RUN pip install --no-cache-dir -r requirements.txt

# Étape 2 : Lancer les tests
CMD ["python", "-m", "unittest", "discover"]
