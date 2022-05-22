from fastapi import FastAPI
import sys
sys.path.insert(
    0, '/Users/praveenkumarb/Documents/pk-workspace/BeautyFull/lib/')
import service
app = FastAPI()
service = service.Service()


@app.get("/health-check")
async def healthCheck():
    return {"status": "Running"}

@app.post('/create-cart')
async def createCart():
    return service.createCart()
