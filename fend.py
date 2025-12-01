import tkinter as tk
import requests
import json

class GUI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, 'Business Agent')
        self.geometry('600x800')

        self.address = 'http://localhost:8080/{}'

        prompt_frame = tk.Frame(self)
        self.prompt = tk.Text(prompt_frame, width=40, height=10, font=('TimesNewRoman',25,))
        self.prompt.pack(side=tk.TOP)
        prompt_frame.pack(side=tk.TOP)

        button_frame = tk.Frame(self)
        tk.Label(button_frame, text='\t').grid(row=1, column=1)
        tk.Button(button_frame, text='Accounting', font=('TimesNewRoman',25,), command=lambda: self.accounting_request()).grid(row=2, column=1)
        tk.Button(button_frame, text='Finance', font=('TimesNewRoman',25,), command=lambda: self.finance_request()).grid(row=2, column=2)
        tk.Button(button_frame, text='Business', font=('TimesNewRoman',25,), command=lambda: self.business_request()).grid(row=2, column=3)
        tk.Button(button_frame, text='Clear', font=('TimesNewRoman',25,), command=lambda: self.clear_data()).grid(row=2, column=4)
        
        button_frame.pack(side=tk.TOP)

        result_frame = tk.Frame(self)
        self.result = tk.Text(result_frame, width=40, height=5, font=('TimesNewRoman',25,))
        self.result.pack(side=tk.BOTTOM)
        result_frame.pack(side=tk.BOTTOM)

    def clear_data(self):
        self.prompt.delete('1.0','end')
        self.result.delete('1.0','end')

    def accounting_request(self):
        msg = {'prompt':self.prompt.get('1.0','end')}
        resp = requests.get(self.address.format('accounting'), params=msg).json()
        final_text = resp['result']
        self.result.insert('1.0', final_text)

    def finance_request(self):
        msg = {'prompt':self.prompt.get('1.0','end')}
        resp = requests.get(self.address.format('finance'), params=msg).json()
        final_text = resp['result']
        self.result.insert('1.0', final_text)

    def business_request(self):
        msg = {'prompt':self.prompt.get('1.0','end')}
        resp = requests.get(self.address.format('business'), params=msg).json()
        final_text = resp['result']
        self.result.insert('1.0', final_text)

        

GUI().mainloop()