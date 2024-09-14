import httpx

async def test_get_endpoint():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome back, nice to see you again!"}
