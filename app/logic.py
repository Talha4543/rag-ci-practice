"""Small, pure functions that are easy to unit-test in CI."""


def chunk_text(text: str, chunk_size: int, overlap: int = 0) -> list[str]:
    """Split text into chunks of `chunk_size` characters, optionally overlapping.

    This is a toy version of the chunking you already do in your RAG pipeline,
    kept simple so the tests are easy to read.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be >= 0 and < chunk_size")

    chunks: list[str] = []
    step = chunk_size - overlap
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += step
    return chunks
