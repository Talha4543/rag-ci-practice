# RAG CI practice

A tiny FastAPI app for practicing GitHub Actions CI/CD. It has one pure function
(`chunk_text`), a couple of endpoints, and tests — small enough to understand fully.

## Run it locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

pytest -v                        # run the tests
ruff check .                     # lint
uvicorn app.main:app --reload    # run the API at http://localhost:8000/docs
```

## What's already wired up

`.github/workflows/ci.yml` runs on every push to `main` and every pull request.
It lints with ruff and runs the tests. That's a complete, working CI pipeline.

## Your exercises

1. Push this to GitHub and watch the green check appear (steps in the chat).
2. Break a test on purpose, push, watch CI go red, then fix it.
3. Extend the workflow to build the Docker image.
4. Extend it again to push the image to GitHub Container Registry (ghcr.io).

See the chat walkthrough for the exact YAML to add in steps 3 and 4.
