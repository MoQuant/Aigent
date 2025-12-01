import google.generativeai as genai

genai.configure(api_key=open('key.txt','r').read())

model = genai.GenerativeModel("gemini-2.0-flash-001")

from aiohttp import web
import json


class API:

    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port

    def ignition(self):
        app = web.Application()
        app.router.add_get('/accounting', self.accounting)
        app.router.add_get('/finance', self.finance)
        app.router.add_get('/business', self.business)
        web.run_app(app, host=self.host, port=self.port)

    async def accounting(self, request):
        params = dict(request.query)
        prompt = params['prompt']
        base_prompt = f"""
            You are an accounting expert. You know every single detail about the
            subject of accounting. Generate the solution to this question: {prompt}
        """
        response = model.generate_content(prompt)
        resp = response.text
        msg = {'result':resp}
        return web.Response(text=json.dumps(msg), content_type='application/json')
 
    async def finance(self, request):
        params = dict(request.query)
        prompt = params['prompt']
        base_prompt = f"""
            You are a finance expert. You know every single detail about the
            subject of finance. Generate the solution to this question: {prompt}
        """
        response = model.generate_content(prompt)
        resp = response.text
        msg = {'result':resp}
        return web.Response(text=json.dumps(msg), content_type='application/json')

    async def business(self, request):
        params = dict(request.query)
        prompt = params['prompt']
        base_prompt = f"""
            You are a business expert. You know every single detail about the
            subject of business. Generate the solution to this question: {prompt}
        """
        response = model.generate_content(prompt)
        resp = response.text
        msg = {'result':resp}
        return web.Response(text=json.dumps(msg), content_type='application/json')

API().ignition()


