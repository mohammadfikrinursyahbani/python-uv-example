# Init uv
```
uv init example
```
# Structure
```
example
├── hello.py
├── pyproject.toml
├── README.md
└── uv.lock
```
# Add single libraries
```
uv add polars
```
# Installing using requirements.txt
```
uv pip install -r requirements.txt
```
# Run specific file
```
uv run --directory test test_file.py
```