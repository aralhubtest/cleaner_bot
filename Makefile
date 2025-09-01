
build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

clean:
	docker compose down --volumes --rmi all

log:
	docker compose logs -f