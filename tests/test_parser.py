from logvortex.parser import parse_log_line

def test_parse_valid_log():
    line = '127.0.0.1 - - [01/Nov/2026:10:00:00 +0000] "GET /api/health HTTP/1.1" 200 1234'
    rec = parse_log_line(line)
    assert rec is not None
    assert rec.status == 200
    assert rec.method == "GET"
    assert rec.path == "/api/health"
