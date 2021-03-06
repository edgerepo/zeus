from collections import defaultdict
from marshmallow import Schema, fields, pre_dump


class CoverageStatsSchema(Schema):
    lines_covered = fields.Integer()
    lines_uncovered = fields.Integer()
    diff_lines_covered = fields.Integer()
    diff_lines_uncovered = fields.Integer()


class TestStatsStatsSchema(Schema):
    count = fields.Integer()
    failures = fields.Integer()
    duration = fields.Number()
    failures_unique = fields.Integer(allow_none=True)
    count_unique = fields.Integer(allow_none=True)


class StyleViolationsStatsSchema(Schema):
    count = fields.Integer()


class BundleStatsSchema(Schema):
    total_asset_size = fields.Integer()


# should be "dumped" with a list of ItemStat instances


class StatsSchema(Schema):
    coverage = fields.Nested(CoverageStatsSchema(), dump_only=True)
    tests = fields.Nested(TestStatsStatsSchema(), dump_only=True)
    style_violations = fields.Nested(StyleViolationsStatsSchema(), dump_only=True)
    bundle = fields.Nested(BundleStatsSchema(), dump_only=True)

    @pre_dump
    def process_stats(self, data):
        result = defaultdict(lambda: defaultdict(int))
        for stat in data:
            bits = stat.name.split(".", 1)
            if len(bits) != 2:
                continue

            result[bits[0]][bits[1]] = stat.value
        return result
