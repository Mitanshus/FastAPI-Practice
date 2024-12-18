"""UUID generator."""

import uuid


def generate_uuid() -> str:
    """Function that generated uuid."""
    # Generate a UUID and convert it to a string
    return str(uuid.uuid4())
