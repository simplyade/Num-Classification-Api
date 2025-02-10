import httpx

async def get_fun_fact(number: int) -> str:
    url = f"http://numbersapi.com/{number}/math"
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)
        if response.status_code == 200:
            fact = response.text
            # Ensure Armstrong number facts are formatted correctly
            if "narcissistic" in fact.lower():
                armstrong_eq = " + ".join(f"{digit}^{len(str(number))}" for digit in str(number))
                return f"{number} is an Armstrong number because {armstrong_eq} = {number}"
            return fact
        # Default Numbers API fact
        return f"No fun fact available for {number}."
