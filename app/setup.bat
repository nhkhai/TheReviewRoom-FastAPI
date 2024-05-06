@ECHO OFF

PUSHD ..

IF NOT EXIST .venv (
    @REM Create the virtual environment here.
    python -m venv .venv
)

CALL .venv\Scripts\activate

pip install -r app\requirements.txt

POPD

@REM PAUSE