@ECHO OFF
PUSHD ..
@REM uvicorn app.main:app --reload
@REM uvicorn app.main:app --host 0.0.0.0 --port 80
@REM uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
@REM uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
uvicorn app.main:app --host 0.0.0.0 --port 9000 --reload
POPD
@REM PAUSE