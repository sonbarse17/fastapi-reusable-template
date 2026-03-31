"""
Automated Testing Suite (tests/)
================================
This directory contains end-to-end and unit tests.
A common Phase-2 practice is to define `conftest.py` here which sets up a `TestClient`
and overrides the `get_db` dependency to point to a temporary test SQLite database, ensuring
tests run quickly and isolated from dev data!
"""
