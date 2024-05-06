pushd ..

if (-not (Test-Path .venv)) {
    # Create the virtual environment here.
    python -m venv .venv
}

.venv\Scripts\Activate.ps1

pip install -r app\requirements.txt

popd

# pause