

para probarlo:  

    docker compose up -d

    docker cp "directorio de trabajo donde esta el main\main.py" python_client:/app/main.py

    docker exec -it python_client python3 /app/main.py


cuando terminen:

    docker compose down -v


