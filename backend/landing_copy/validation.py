"""Validate the fixed v1 landing text contract before storing a revision."""

from django.core.exceptions import ValidationError

# A leaf is its maximum plain-text length. Optional groups are handled below.
COPY_SCHEMA = {
    "seo": {"title": 120, "description": 300},
    "shared_text": {
        "navigation_labels": {
            "solutions": 40,
            "how_it_works": 40,
            "use_cases": 40,
            "pricing": 40,
            "faq": 40,
            "contact": 40,
        },
        "action_labels": {"book_demo": 60, "watch_demo": 60},
        "footer_tagline": 120,
    },
    "hero": {
        "eyebrow": 120,
        "heading_lead": 120,
        "heading_accent": 80,
        "description": 400,
        "side_note": 120,
        "highlights": {
            "opportunities": {"label": 120},
            "time": {"label": 120},
            "always_on": {"label": 120},
        },
    },
    "trust": {
        "eyebrow": 120,
        "testimonial": {"quote": 400, "attribution": 120},
    },
    "problem": {
        "eyebrow": 80,
        "heading": 160,
        "description": 400,
        "items": {
            "late_replies": {"label": 120},
            "lost_conversations": {"label": 120},
            "manual_followup": {"label": 120},
            "disconnected_tools": {"label": 120},
            "unanswered_prospects": {"label": 120},
        },
    },
    "solution": {
        "eyebrow": 80,
        "heading": 160,
        "description": 500,
        "items": {
            "attract": {"heading": 80, "description": 240},
            "converse": {"heading": 80, "description": 240},
            "follow_up": {"heading": 80, "description": 240},
            "book": {"heading": 80, "description": 240},
            "sell": {"heading": 80, "description": 240},
        },
    },
    "results": {
        "eyebrow": 80,
        "heading": 160,
        "description": 400,
        "items": {
            "bookings": {"value": 30, "label": 120, "description": 200},
            "time_saved": {"value": 30, "label": 120, "description": 200},
            "conversions": {"value": 30, "label": 120, "description": 200},
        },
    },
    "audiences": {
        "eyebrow": 80,
        "heading": 160,
        "description": 400,
        "items": {
            "retail": {"heading": 100, "description": 240},
            "wellness": {"heading": 100, "description": 240},
            "education": {"heading": 100, "description": 240},
            "b2b": {"heading": 100, "description": 240},
            "hospitality": {"heading": 100, "description": 240},
        },
    },
    "closing_cta": {
        "left_note": 160,
        "heading": 180,
        "description": 300,
        "right_note": 160,
    },
}
OPTIONAL_GROUPS = {"trust", "results"}


def _check(value: object, schema: dict | int, path: str) -> None:
    if isinstance(schema, int):
        if not isinstance(value, str) or not value.strip() or len(value) > schema:
            raise ValidationError(f"{path} must be nonempty text of at most {schema} characters.")
        if "<" in value or ">" in value or "://" in value or "javascript:" in value.lower():
            raise ValidationError(f"{path} must be plain text without markup or URLs.")
        return

    if path.endswith((".highlights", ".items")):
        if not isinstance(value, list):
            raise ValidationError(f"{path} must be a list.")
        item_ids = [item.get("id") if isinstance(item, dict) else None for item in value]
        if (
            len(item_ids) != len(schema)
            or any(not isinstance(item_id, str) for item_id in item_ids)
            or set(item_ids) != set(schema)
        ):
            raise ValidationError(f"{path} must contain exactly the known item IDs.")
        for item in value:
            item_schema = {"id": 80, **schema[item["id"]]}
            _check(item, item_schema, f"{path}.{item['id']}")
        return

    if not isinstance(value, dict) or set(value) != set(schema):
        raise ValidationError(f"{path} must contain exactly the supported fields.")
    for key, child_schema in schema.items():
        _check(value[key], child_schema, f"{path}.{key}")


def validate_copy(value: object) -> None:
    """Accept only complete v1 copy with optional unverified-claim groups."""

    if not isinstance(value, dict):
        raise ValidationError("copy must be an object.")
    required = set(COPY_SCHEMA) - OPTIONAL_GROUPS
    if not required <= set(value) or not set(value) <= set(COPY_SCHEMA):
        raise ValidationError("copy must contain the supported required groups.")
    for key in value:
        _check(value[key], COPY_SCHEMA[key], f"copy.{key}")
