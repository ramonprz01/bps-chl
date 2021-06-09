# Bonus Problem #1

Sypht!

We would love to see what you can do with the Sypht API. Sign-up for a free account (https://sypht.com) and use one or more of the provided AI products to create a demo which shows off your skills.

Checkout https://app.sypht.com/marketplace/catalog for available extraction types. If there’s something outside the free tier you’d like to use, just shoot us a message.

See https://github.com/sypht-team for API client libraries (e.g. Python client) and https://sypht.gitbook.io/sypht/ for the developer guide to help you get started.

## Requirements
- Build a simple web app frontend for our REST API which lets a user upload files and view the results
- Do something on top of data extracted by Sypht, e.g:
    - Analyse or plot bill size distribution over time from a corpus of receipts
    - Integrate with a third party API to verify the Supplier ABN on an invoice
    - Cluster similar fields by label from data returned by the generic fieldset
    
    
## Solution

Please make sure your environment is active first and that you have the module panel installed. If those two are good to go, please run,

```sh
panel serve sypht_app.py
```

or, you can initialize jupyter lab and run the cells in the notebook called, `sypht_app.ipynb`.