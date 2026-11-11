from datetime import date

from avphdresearch.periods import aggregate_counts, period_label


def test_monthly():
    assert period_label(date(2024, 3, 12), 2) == "2024-03"


def test_weekly_year_boundary():
    assert period_label(date(2021, 1, 1), 1) == "2020-W53"


def test_aggregate():
    assert aggregate_counts([date(2024, 3, 1), date(2024, 3, 5)], 2) == {"2024-03": 2}
