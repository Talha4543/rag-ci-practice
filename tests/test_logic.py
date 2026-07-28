import pytest

from app.logic import chunk_text


def test_basic_chunking():
    assert chunk_text("abcdefghij", chunk_size=5) == ["abcde", "fghij"]


def test_overlap():
    chunks = chunk_text("abcdefghij", chunk_size=5, overlap=2)
    assert chunks[0] == "abcde"
    assert chunks[1] == "defgh"


def test_empty_text():
    assert chunk_text("abcdefghij", chunk_size=5) == ["abcde", "fghij"]


def test_invalid_chunk_size():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=0)
