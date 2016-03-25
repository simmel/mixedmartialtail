# vim: set fileencoding=utf-8 sw=4 et tw=79
import pytest
import time

@pytest.mark.benchmark(
    min_rounds=5,
)

def test_json_100p_syslog(benchmark):
    benchmark(time.sleep, 0.02)
