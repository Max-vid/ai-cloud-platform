def process_metrics(data):
    return {
        "status": "received",
        "server_id": data.server_id,
        "cpu": data.cpu,
        "ram": data.ram,
        "disk": data.disk,
        "network": data.network,
        "timestamp": data.timestamp,
    }
