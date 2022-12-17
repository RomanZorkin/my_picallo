-include .env
export

run:
	@docker-compose up -d
	@python main.py