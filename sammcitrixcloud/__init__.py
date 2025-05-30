from requests import post
from .sammodata4 import OdataQuery4

class SammOdataCitrixCloud:
	def __init__(self, customer_id, client_id, client_secret, 
			entity=None, filter=None, expand=None):
		self._customer_id = customer_id
		self._client_id = client_id
		self._client_secret = client_secret
		self._url = 'https://api.cloud.com/monitorodata/'
		self._auth_url = 'https://api-us.cloud.com/cctrustoauth2/root/tokens/clients'
		headers = self.get_auth_header()
		self.query = OdataQuery4(service_url=self._url, headers=headers, 
			entity=entity, filter=filter, expand=expand)

	def get_auth_header(self):
		payload = dict(client_id=self._client_id, 
			client_secret=self._client_secret, 
			grant_type='client_credentials')
		r = post(self._auth_url, data=payload)
		if not r:
			raise Exception("Authentication Error")
		resdata = r.json()
		return {
			'Citrix-CustomerId': self._customer_id,
			'Authorization': f"CWSAuth Bearer={resdata['access_token']}"
		}

	def __iter__(self):
		self._iter = iter(self.query)
		return self

	def __next__(self):
		return next(self._iter)
