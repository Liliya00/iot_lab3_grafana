import random
from datetime import datetime


def generate_sensor_record():
    object_type = random.choice(["parking", "traffic_light", "edge_node"])

    base_record = {
        "timestamp": datetime.utcnow(),
        "object_type": object_type,
        "object_id": f"{object_type}_{random.randint(1, 5)}",
        "latitude": 50.45 + random.uniform(-0.01, 0.01),
        "longitude": 30.52 + random.uniform(-0.01, 0.01),
    }

    if object_type == "parking":
        total_places = random.choice([30, 40, 50, 80, 100])
        empty_count = random.randint(0, total_places)
        occupied_count = total_places - empty_count
        occupancy_percent = round((occupied_count / total_places) * 100, 2)

        base_record.update({
            "measurement": "parking_metrics",
            "empty_count": empty_count,
            "occupied_count": occupied_count,
            "total_places": total_places,
            "occupancy_percent": occupancy_percent,
            "vehicle_count": None,
            "latency_ms": None,
            "packet_loss": None,
            "bandwidth_mbps": None,
            "power_consumption": None,
            "cpu_load": None,
            "edge_temperature": None,
        })

    elif object_type == "traffic_light":
        base_record.update({
            "measurement": "traffic_metrics",
            "current_signal": random.choice(["red", "yellow", "green"]),
            "vehicle_count": random.randint(0, 80),
            "pedestrian_button": random.choice([0, 1]),
            "empty_count": None,
            "occupied_count": None,
            "total_places": None,
            "occupancy_percent": None,
            "latency_ms": None,
            "packet_loss": None,
            "bandwidth_mbps": None,
            "power_consumption": None,
            "cpu_load": None,
            "edge_temperature": None,
        })

    else:
        base_record.update({
            "measurement": "network_energy_metrics",
            "latency_ms": round(random.uniform(10, 300), 2),
            "packet_loss": round(random.uniform(0, 8), 2),
            "bandwidth_mbps": round(random.uniform(5, 100), 2),
            "power_consumption": round(random.uniform(20, 120), 2),
            "cpu_load": round(random.uniform(5, 95), 2),
            "edge_temperature": round(random.uniform(35, 85), 2),
            "empty_count": None,
            "occupied_count": None,
            "total_places": None,
            "occupancy_percent": None,
            "vehicle_count": None,
        })

    return base_record