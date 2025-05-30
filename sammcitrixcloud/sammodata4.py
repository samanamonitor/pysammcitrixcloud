from requests import Session, post
from datetime import datetime

from odata import ODataService
import importlib

class OdataEntry4:
	def __init__(self, entry):
		if not isinstance(entry, object):
			raise ValueError
		self._entry = entry
		self._props = [ i for i, _ in self._entry.__dict__['__odata__'].properties]

	def __contains__(self, key):
		return key in self._props

	def get(self, key, default=None):
		return getattr(self, key, default)

	def __getitem__(self, key):
		return getattr(self, key)

	def __iter__(self):
		return iter(self.__dict__.items())

	@property
	def __dict__(self):
		out = {}
		for prop in self._props:
			out[prop] = getattr(self._entry, prop)
		return out

class OdataQuery4:
	def __init__(self, service_url=None, headers={}, 
			entity=None, filter=None, expand=None):
		if not isinstance(service_url, str) or service_url == '':
			raise TypeError("service_url must be str")
		if not isinstance(entity, str):
			raise TypeError("Invalid entity")
		self._service_url = service_url
		self._http_session = Session()
		self._http_session.headers.update(headers)
		self._expand = expand
		self._filter = filter
		session = Session()
		session.headers.update(headers)
		self._service = ODataService(
			url=self._service_url,
			session=session,
			reflect_entities=True,
			reflect_output_package="generated.citrix")
		self._lib = importlib.import_module("generated.citrix")
		self._entity = getattr(self._lib, entity)
		if not isinstance(self._entity, type):
			raise TypeError(f"Entity {entity} doesn't exist")

	def __iter__(self):
		self._query = self._service.query(self._entity)
		if self._filter is not None:
			self._query.filter(self._filter)
		for e in self._expand.split(","):
			self._query = self._query.expand(getattr(self.entity, e))
		self._es_iterator = iter(self._query)
		return self

	def __next__(self):
		return OdataEntry4(next(self._es_iterator))
