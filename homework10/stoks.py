"""
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта центробанка РФ)
Код компании (справа от названия компании на странице компании)
P/E компании (информация находится справа от графика на странице компании)
Годовой рост/падение компании в процентах (основная таблица)
Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от графика на странице компании)
Сохранить итоговую информацию в 4 JSON файла:

Топ 10 компаний с самими дорогими акциями в рублях.
Топ 10 компаний с самым низким показателем P/E.
Топ 10 компаний, которые показали самый высокий рост за последний год
Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
Пример формата:
[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]
For scrapping you cans use beautifulsoup4
For requesting aiohttp
"""

import asyncio
import json
import re
from heapq import heappushpop

import aiohttp
import requests
from bs4 import BeautifulSoup


async def get_sp500():

    async with aiohttp.ClientSession() as session:

        for page in range(1, 11):
            async with session.get(
                "https://markets.businessinsider.com/index/components/s&p_500",
                params=[("p", page)],
            ) as response:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")

                for company in get_stocks_on_page(soup):
                    asyncio.create_task(get_company_info(session, company))
                    await asyncio.sleep(0.01)

    create_json_files()


def get_stocks_on_page(soup):
    return soup.find_all("a", href=re.compile(r"-stock$"), attrs={"title": True})


def get_current_usd():
    html = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text
    soup = BeautifulSoup(html, "html.parser")
    return float(
        soup.find("valute", attrs={"id": "R01235"}).value.text.replace(",", ".")
    )


async def get_company_info(session, company):
    company_name = company["title"]
    company_url = f"https://markets.businessinsider.com/{company['href']}"
    company_ticker = re.split(r"/", company["href"])[-1].split("-")[0].upper()
    company_growth = list(list(company.parent.next_siblings)[-4].children)[
        -2
    ].text.strip("%")

    async with session.get(company_url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")

        current_cost = (
            float(
                soup.find(
                    "div", attrs={"class": "progress__label snapshot__price-label"}
                ).text.replace(",", "")
            )
            * get_current_usd()
        )
        pe_ratio = get_info_from_page(soup, "P/E Ratio")
        high_year = get_info_from_page(soup, "52 Week High")
        low_year = get_info_from_page(soup, "52 Week Low")

        if all((high_year, low_year)):
            potential_profit = round((high_year - low_year) * get_current_usd(), 2)
        else:
            potential_profit = None

        company_info = {
            "code": company_ticker,
            "name": company_name,
            "price": round(current_cost, 2),
            "P/E": pe_ratio,
            "growth": company_growth,
            "potential profit": potential_profit,
        }

    choose_top10(company_info)


def get_info_from_page(soup, parameter):
    try:
        return float(
            list(
                soup.find(
                    "div", attrs={"class": "snapshot__header"}, string=parameter
                ).parent.stripped_strings
            )[0].replace(",", "")
        )
    except AttributeError:
        pass


highest_cost = [() for _ in range(10)]
lowest_pe_ratio = [() for _ in range(10)]
highest_growth = [() for _ in range(10)]
highest_potential_profit = [() for _ in range(10)]


def choose_top10(company: dict) -> None:
    if company["price"]:
        heappushpop(highest_cost, (company["price"], company))
    if company["P/E"]:
        heappushpop(lowest_pe_ratio, (-company["P/E"], company))
    if company["growth"]:
        heappushpop(highest_growth, (company["growth"], company))
    if company["potential profit"]:
        heappushpop(
            highest_potential_profit,
            (company["potential profit"], company),
        )


def to_json(file_name, data, key, reverse=True):
    data = (i[1] for i in data)
    with open(file_name, "w") as f:
        json.dump(sorted(data, key=lambda x: x[key], reverse=reverse), f, indent="")


def create_json_files():
    to_json("highest_cost.json", highest_cost, "price")
    to_json("lowest_pe_ratio.json", lowest_pe_ratio, "P/E", reverse=False)
    to_json("highest_growth.json", highest_growth, "growth")
    to_json(
        "highest_potential_profit.json", highest_potential_profit, "potential profit"
    )


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(get_sp500())
