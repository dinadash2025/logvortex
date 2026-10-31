import re
from pydantic import BaseModel

LOG_PATTERN = re.compile(r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d+) (?P<size>\S+)')

class LogRecord(BaseModel):
    ip: str
    timestamp: str
    method: str
    path: str
    status: int
    size: int

def parse_log_line(line: str) -> LogRecord | None:
    match = LOG_PATTERN.match(line)
    if not match: return None
    data = match.groupdict()
    return LogRecord(
        ip=data["ip"],
        timestamp=data["timestamp"],
        method=data["method"],
        path=data["path"],
        status=int(data["status"]),
        size=int(data["size"]) if data["size"].isdigit() else 0
    )
