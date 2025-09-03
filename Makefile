
build:
	docker compose build

up:
	docker compose up -d

restart:
	docker compose down
	docker compose up -d --build

down:
	docker compose down

clean:
	docker compose down --volumes --rmi all

log:
	docker compose logs -f