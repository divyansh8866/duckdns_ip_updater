# DuckDNS IP Updater

This Python script is designed to update your DuckDNS domain with your current public IP address. DuckDNS is a free dynamic DNS service that allows you to map a domain to your changing IP address. This script ensures that your DuckDNS domain always points to your current public IP.

## Features

- Retrieves the current public IP address using the [ipify](https://www.ipify.org/) service.
- Checks whether the public IP has changed since the last update by storing the last recorded IP in a file.
- Updates DuckDNS only if the public IP has changed.
- Logs all activities, including successful updates and errors, to a log file (`duckdns_updater.log`).
- Configurable to run in a loop, updating DuckDNS every 10 minutes.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your system.
- Docker installed if you plan to run the script as a Docker container.

## Configuration

Set the following environment variables:

- `DUCKDNS_TOKEN`: Your DuckDNS token.
- `DUCKDNS_DOMAIN`: Your DuckDNS domain.

```bash
export DUCKDNS_TOKEN=your_actual_token
export DUCKDNS_DOMAIN=your_actual_domain
```

## Usage

### Running as a Standalone Script

1. Set the required environment variables.

```bash
export DUCKDNS_TOKEN=your_actual_token
export DUCKDNS_DOMAIN=your_actual_domain
```

2. Execute the script.

```bash
python script.py
```

### Running as a Docker Container

1. Build the Docker image.

```bash
docker build -t duckdns-updater .
```

2. Run the Docker container.

```bash
docker run -d -e DUCKDNS_TOKEN=your_actual_token -e DUCKDNS_DOMAIN=your_actual_domain duckdns-updater
```

### Docker Compose

Create a `docker-compose.yml` file:

```yaml
version: '3'

services:
  duckdns-updater:
    build: .
    restart: always
    environment:
      - DUCKDNS_TOKEN=your_actual_token
      - DUCKDNS_DOMAIN=your_actual_domain
```

Run the Docker container using Docker Compose.

```bash
docker-compose up -d
```

## Logs

View the logs for the script by checking the `duckdns_updater.log` file.

```bash
cat duckdns_updater.log
```

This log file contains information about the script's execution, including successful updates and any encountered errors.

Feel free to customize and integrate this script into your system to ensure your DuckDNS domain remains up-to-date with your current public IP address.
