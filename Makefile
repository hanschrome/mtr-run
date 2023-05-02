.PHONY: run

run:
	@docker-compose up -d || docker compose up -d

debug:
	@docker-compose up || docker compose up

cron:
	./cron.sh &> /dev/null & echo $$! > cron.pid
