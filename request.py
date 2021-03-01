import aiohttp
import asyncio

async def requests(inputs, itc):
    base_url = r"http://inputtools.google.com" + \
        r'/request?text=' + inputs + '&itc=' + itc + '&num=1&cp=0&cs=1&ie=utf-8&oe=utf-8&app=test'
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url) as response:

            html = await response.text()
            return html

            
      
async def main(sentences, itc):
    all_req = []
    for sentence in sentences:
        if len(sentence)==0:
            continue
        all_req.append(asyncio.ensure_future(requests(sentence, itc)))
    responses = await asyncio.gather(*all_req)
    return responses

def get_transliterated(sentence, itc):

    loop = asyncio.get_event_loop()
    all_response = loop.run_until_complete(main(sentence, itc))
    return all_response

