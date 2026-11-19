
import pytest

from src.core.process import Process
from src.algorithms.traditional.sjf import SJFScheduler


def create_processes(data):
    """Create fresh Process objects from test data."""
    return [
        Process(
            pid=pid,
            arrival_time=arrival,
            burst_time=burst
        )
        for pid, arrival, burst in data
    ]


def test_sjf_selects_shortest_available_process():
    """SJF should select the shortest burst among arrived processes."""

    processes = create_processes([
        (1, 0, 7),
        (2, 2, 4),
        (3, 3, 2),
        (4, 4, 1)
    ])

    scheduler = SJFScheduler()
    timeline = scheduler.schedule(processes)

    segments = timeline.get_segments()

    assert [
        (s.pid, s.start_time, s.end_time)
        for s in segments
    ] == [
        (1, 0, 7),
        (4, 7, 8),
        (3, 8, 10),
        (2, 10, 14)
    ]


def test_sjf_handles_idle_time():
    """SJF should correctly record CPU idle periods."""

    processes = create_processes([
        (1, 5, 3),
        (2, 10, 2)
    ])

    scheduler = SJFScheduler()
    timeline = scheduler.schedule(processes)

    segments = timeline.get_segments()

    assert [
        (s.pid, s.start_time, s.end_time)
        for s in segments
    ] == [
        (None, 0, 5),
        (1, 5, 8),
        (None, 8, 10),
        (2, 10, 12)
    ]


def test_sjf_tie_breaking():
    """Equal burst times should preserve ready queue insertion order."""

    processes = create_processes([
        (1, 0, 4),
        (2, 0, 2),
        (3, 0, 2)
    ])

    scheduler = SJFScheduler()
    timeline = scheduler.schedule(processes)

    segments = timeline.get_segments()

    assert [s.pid for s in segments] == [2, 3, 1]


def test_sjf_updates_process_attributes():
    """SJF should correctly update process runtime attributes."""

    processes = create_processes([
        (1, 0, 7),
        (2, 2, 4),
        (3, 3, 2),
        (4, 4, 1)
    ])

    scheduler = SJFScheduler()
    scheduler.schedule(processes)

    expected = {
        1: (0, 7),
        2: (10, 14),
        3: (8, 10),
        4: (7, 8)
    }

    for process in processes:
        start, completion = expected[process.pid]

        assert process.start_time == start
        assert process.completion_time == completion
        assert process.remaining_time == 0


def test_sjf_empty_workload():
    """An empty workload should return an empty timeline."""

    scheduler = SJFScheduler()
    timeline = scheduler.schedule([])

    assert len(timeline) == 0
    assert timeline.total_time == 0


def test_sjf_rejects_already_executed_processes():
    """SJF should reject previously executed processes."""

    processes = create_processes([
        (1, 0, 4)
    ])

    scheduler = SJFScheduler()
    scheduler.schedule(processes)

    with pytest.raises(ValueError):
        scheduler.schedule(processes)
