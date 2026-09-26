from django.http import HttpResponse
import asyncio
from app.models import Company
import httpx
from asgiref.sync import sync_to_async


async def async_home(request):
    async def task1():
        print("task1 started")
        await asyncio.sleep(3)
        print("task 1 finished")

    async def task2():
        print("task 2 started")
        await asyncio.sleep(1)
        print("task2 finished")

    res1, res2 = await asyncio.gather(task1(), task2())

    return HttpResponse("this is a asunc view")


async def github_user(request):

    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/users/octocat")

    data = response.json()

    return HttpResponse(data["login"])


async def async_company(request):
    comp = await Company.objects.aget(id=1)
    return HttpResponse(comp.name)


async def check_company(request):
    if await Company.objects.filter(name="Google").aexists():
        return HttpResponse("company exists")
    return HttpResponse("copany not exists")


@sync_to_async
def get_company():
    comp = Company.objects.get(id=1)
    return comp.name


async def company1(request):
    comp = await get_company()
    return HttpResponse(f"{comp}")
