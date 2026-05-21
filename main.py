import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from generator import generate_sensor_record


INFLUX_URL = "http://localhost:8086"
TOKEN = "mytoken"
ORG = "iot_org"
BUCKET = "sensor_data"


def write_record(write_api, record):
    point = (
        Point(record["measurement"])
        .tag("object_type", record["object_type"])
        .tag("object_id", record["object_id"])
        .time(record["timestamp"], WritePrecision.NS)
    )

    for key, value in record.items():
        if key in ["measurement", "timestamp", "object_type", "object_id"]:
            continue

        if value is not None:
            if isinstance(value, str):
                point = point.field(key, value)
            else:
                point = point.field(key, float(value))

    write_api.write(bucket=BUCKET, org=ORG, record=point)


def main():
    client = InfluxDBClient(
        url=INFLUX_URL,
        token=TOKEN,
        org=ORG
    )

    write_api = client.write_api(write_options=SYNCHRONOUS)

    print("Sending IoT sensor data to InfluxDB...")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            record = generate_sensor_record()
            write_record(write_api, record)

            print(
                f"Sent: {record['measurement']} | "
                f"{record['object_id']} | "
                f"{record['timestamp']}"
            )

            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopped data generation.")
        client.close()


if __name__ == "__main__":
    main()