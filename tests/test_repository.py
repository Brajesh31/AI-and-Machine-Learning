from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]


def test_expected_notebooks_exist():
    notebooks = list(ROOT.glob("*.ipynb"))
    assert len(notebooks) == 4


def test_notebooks_are_valid_nbformat():
    for path in ROOT.glob("*.ipynb"):
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)


def test_dataset_manifest_documents_missing_data():
    manifest = ROOT / "data" / "README.md"
    assert manifest.is_file()
    content = manifest.read_text(encoding="utf-8")
    for filename in (
        "liver_cirrhosis.csv",
        "LoansData (1).csv",
        "diabetes.csv",
        "Cryptocurrency_FeaturedData.csv",
    ):
        assert filename in content


def test_documentation_index_exists():
    assert (ROOT / "docs" / "README.md").is_file()
