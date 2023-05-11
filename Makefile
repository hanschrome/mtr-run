.PHONY: run debug shell cron

run:
	@docker-compose up -d multi-trading-robot || docker compose up -d multi-trading-robot

debug:
	@docker-compose up multi-trading-robot || docker compose up multi-trading-robot

shell:
	@docker-compose run --rm python /bin/bash

cron:
	./cron.sh &> /dev/null & echo $$! > cron.pid
