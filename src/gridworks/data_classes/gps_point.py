""" GpsPoint Definition """

from typing import Dict


class GpsPoint:
    by_id: Dict[str, "GpsPoint"] = {}

    def __new__(cls, gps_point_id: str, *args, **kwargs):  # type: ignore
        try:
            return cls.by_id[gps_point_id]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[gps_point_id] = instance
            return instance

    def __init__(
        self,
        gps_point_id: str,
        lat: float,
        lon: float,
    ):
        self.gps_point_id = gps_point_id
        self.lat = lat
        self.lon = lon

    def __repr__(self) -> str:
        rs = f"GpsPoint lat: {self.lat}, lon: {self.lon} \r gps_point_id: {self.gps_point_id}"
        return rs
