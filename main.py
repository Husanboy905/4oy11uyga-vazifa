# 1-misol
# import asyncio
#
# from envs.labelimg.Lib.cgitb import reset
#
#
# async def paswords(pasvort):
#     a=""
#     i=0
#     while i<len(pasvort):
#         if not pasvort[i].isdigit():
#             a += pasvort[i]
#         i+=1
#         return a
# async def main():
#     pasvort=("P@ssw0rd123")
#     p=await paswords(pasvort)
#     print(p)
# asyncio.run(main())

# 2-misol
# async def exts(text):
#     a = ""
#     i = 0
#     while i < len(text) and i < 10:
#         a += text[i]
#         i += 1
#     return a
#
# async def main():
#     text = "Bu menins ismim Husanboy"
#     t = await exts(text)
#     print(t)
#
# asyncio.run(main())


# 3-misol
# async def names(name):
#     a=""
#     i=0
#     while i < len (name):
#         if not name[i].isdigit():
#             a += name[i]
#         i+=1
#         return a
# async def main():
#     n = "Al1ex4a"
#     p = await names(n)
#     print(p)
# asyncio.run(main())

# 4-misol
# async def kata_harif(text):
#     result = ""
#     i = 0
#     while i < len(text):
#         if not text[i].isspace():
#             result += text[i].lower()
#         i += 1
#     return result
#
# async def main():
#     text = "Bu Matn Katta Harfli Va Bo'sh Joyli"
#     t = await kata_harif(text)
#     print(t)
#
# asyncio.run(main())

# 5-misol
# async def unliy_harflar(text):
#     unliy = "aeiouAEIOU"
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i] in unliy:
#             result += text[i]
#         i += 1
#     return result
#
# async def main():
#     t = "Backend Python Django Standard"
#     u = await unliy_harflar(t)
#     print(u)
#
# asyncio.run(main())

# 6-misol
# async def ab_ketmaket(soz):
#     result = ""
#     i = 0
#     while i < len(soz):
#         if i < len(soz) - 1 and soz[i] == 'a' and soz[i + 1] == 'b':
#             result += "#"
#             i += 2
#         else:
#             result += soz[i]
#             i += 1
#     return result
#
# async def main():
#     soz = "alphabet abbreviation"
#     s = await ab_ketmaket(soz)
#     print(s)
#
# asyncio.run(main())


# 7-misol
# async def teskari_qil(text):
#     if text.isdigit():
#         return text[::-1]
#     return text
#
# async def main():
#     text = "123456789"
#     t = await teskari_qil(text)
#     print(t)
#
# asyncio.run(main())


# 8-misol
# async def orta(word):
#     uzunligi = len(word)
#     if uzunligi % 2 == 1:
#         orta = uzunligi // 2
#         return word[:orta] + word[orta + 1:]
#     return word
#
# async def main():
#     word = "husanboy"
#     o = await orta(word)
#     print(o)
#
# asyncio.run(main())

# 9-misol
# async def kichik_harifqil(name):
#     if name.endswith('a'):
#         return name.lower()
#     return name
#
# async def main():
#     name = "Husanboy"
#     k = await kichik_harifqil(name)
#     print(k)
#
# asyncio.run(main())


# 10-misol
# async def takralanuvchilt(text):
#     result = ""
#     seen = set()
#     i = 0
#     while i < len(text):
#         if text[i] not in seen:
#             result += text[i]
#             seen.add(text[i])
#         i += 1
#     return result
#
# async def main():
#     text = "programming"
#     t = await takralanuvchilt(text)
#     print(t)
#
# asyncio.run(main())

# 11-misol
# async def unloiy_har(word):
#     unliy = "aeiouAEIOU"
#     if all(a in unliy for a in word):
#         return word.upper()
#     return word
#
# async def main():
#     word = "aeiou"
#     u = await unloiy_har(word)
#     print(u)
#
# asyncio.run(main())


# 12-misol
import aiohttp
import asyncio
async def obahavo(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    async with aiohttp.ClientSession() as a:
        async with a.get(url) as javob:
            return await javob.json()

async def main():
    shahar = "Tashkent"
    api_key = "YOUR_API_KEY"
    w = await obahavo(shahar, api_key)
    print(w)

asyncio.run(main())
