from pathlib import Path


def test_core_source_has_no_network_imports() -> None:
    source_root = Path("src/workskill_safe")
    source = "\n".join(path.read_text(encoding="utf-8") for path in source_root.glob("*.py"))
    forbidden = (
        "import " + "requests",
        "import " + "httpx",
        "import " + "aiohttp",
        "import " + "socket",
        "from " + "urllib",
    )
    for item in forbidden:
        assert item not in source
