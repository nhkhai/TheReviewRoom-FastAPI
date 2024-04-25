@ECHO OFF

PUSHD ..

python -m venv .venv

CALL .venv\Scripts\activate

pip install -r requirements.txt

POPD

@REM PAUSE