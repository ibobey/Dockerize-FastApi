from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"directory": "root"}


@app.get('/api')
async def api():
    return {"directory": "api", "version": "1.0.0", "description": "Test Api"}
