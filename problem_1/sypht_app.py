import requests
import base64
import os
import json
import panel as pn
from io import BytesIO

pn.extension()


file = pn.widgets.FileInput(value=None)

@pn.depends(file.param.value)
def get_data(file):
    
    ## Authentication
    url_auth = 'https://auth.sypht.com/oauth2/token'
    payload_auth = 'client_id=' + '259mg2c0d970ls6ieehvege3vc' + '&grant_type=client_credentials'
    auth_slug = '259mg2c0d970ls6ieehvege3vc' + ':' + '3al4aah5jugp5db9omgqr3pvoivh93qk0bc8fqbcra7mnmrbp87'
    auth_slug_enc = base64.b64encode(auth_slug.encode('utf-8')).decode('utf-8')
    headers_auth = {
      'Accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': 'Basic ' + auth_slug_enc
    }
    
    response = requests.request('POST', url_auth, headers=headers_auth, data=payload_auth, allow_redirects=False)
    token = json.loads(response.text)["access_token"]
    
    if file:
    
        ## Loading Data
        url_load = 'https://api.sypht.com/fileupload'
        payload_load = {'products': '["sypht.document"]'}
        files = {'fileToUpload': file}
        headers_load = {
          'Accept': 'application/json',
          'Authorization': f'Bearer {token}',
        }

        response_load = requests.request('POST', url_load, headers=headers_load, data=payload_load, files=files, allow_redirects=False)
        fileID = json.loads(response_load.text)["fileId"]


        ## Response
        url_results = f'https://api.sypht.com/result/final/{fileID}'
        headers_results = {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': f'Bearer {token}'
        }
        response_results = requests.request('GET', url_results, headers=headers_results, allow_redirects=False)
        response_results = json.loads(response_results.text)
        the_pic = pn.pane.PNG(BytesIO(file), width=500, height=500, sizing_mode="fixed", align="center")

        return pn.Row(pn.pane.JSON(response_results, max_height=500), the_pic, width=910, height=500, sizing_mode="fixed", align="center")
    
    
    
header = pn.pane.Markdown("# Document Analyzer App", style={"color": "#3b4252"}, width=500, 
                          sizing_mode="stretch_width", margin=(10,5,10,15))

p1 = pn.pane.PNG("https://www.seekpng.com/png/full/265-2650386_clipart-info-cartoon-document.png", 
                 height=50, sizing_mode="fixed", align="center")
p2 = pn.pane.PNG("https://image.shutterstock.com/image-vector/pile-document-cartoon-vector-illustration-600w-547626148.jpg", 
                 height=50, sizing_mode="fixed", align="center")
title = pn.Row(header, pn.Spacer(), p1, p2, background="#d8dee9", sizing_mode='fixed', width=910, height=70)

text = pn.pane.Markdown("""
    This app uses the Sypht API to analyze invoices. It can currently take one at a time, produce a view of the
    invoice, and return 4 useful pieces of info from it. There is more to come soon.

""", style={"color": "#d8dee9"})

file_button_title = pn.Column(pn.pane.Markdown("# Upload an Invoice", style={"color": "#d8dee9"}), file)

row2 = pn.Row(text, pn.Spacer(width=70), file_button_title, width=910, height=250, sizing_mode="fixed", align="center")


app = pn.Column(title, row2, get_data, background='#3b4252', width=910, height=920, sizing_mode="fixed", align="center")
app.show()