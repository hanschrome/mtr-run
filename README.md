# Multi-Trading-Robot

This project deploys a multi-trading robot using Docker Compose.

## Prerequisites

- [Docker](https://www.docker.com/) (v20.10 or later recommended)
- [Docker Compose](https://docs.docker.com/compose/) (v1.29 or later recommended)
- [GNU Make](https://www.gnu.org/software/make/) (optional, for using Makefile)

## Setup

1. Clone the repository
2. Modify the `.env` to add BINANCE_PUBLIC_KEY and BINANCE_PRIVATE_KEY.
3. Modify the configuration in `data/1.json` to your liking. Check also the `data/index.json`.

## Usage

```bash
make run # Start the containers
make cron # Start the containers in debug mode, check .pid file created to know the pid you should kill.
```

In case you need to debug 

```bash
make debug # Start the containers in debug mode
```
