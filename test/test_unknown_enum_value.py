# coding: utf-8

"""
Manual test for unknown enum value handling.

The SDK's enum template (templates/model_enum.mustache) defines `_missing_` so
that values not declared in the SDK fall back to `UNKNOWN_DEFAULT_OPEN_API`
instead of raising `ValueError`. This protects callers from API responses that
introduce new enum values before the SDK is regenerated.
"""

import json
import unittest

from revengai.models.ai_decompilation_rating import AiDecompilationRating


class TestUnknownEnumValue(unittest.TestCase):
    def test_known_value_resolves_normally(self):
        self.assertIs(AiDecompilationRating("POSITIVE"), AiDecompilationRating.POSITIVE)

    def test_unknown_value_falls_back_to_unknown_default(self):
        self.assertIs(
            AiDecompilationRating("SOMETHING_NEW_FROM_THE_API"),
            AiDecompilationRating.UNKNOWN_DEFAULT_OPEN_API,
        )

    def test_unknown_value_from_json_falls_back_to_unknown_default(self):
        self.assertIs(
            AiDecompilationRating.from_json(json.dumps("SOMETHING_NEW_FROM_THE_API")),
            AiDecompilationRating.UNKNOWN_DEFAULT_OPEN_API,
        )


if __name__ == "__main__":
    unittest.main()
