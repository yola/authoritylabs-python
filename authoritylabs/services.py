# -*- coding: utf-8 -*-
from demands import HTTPServiceClient

from authoritylabs.utils import memoized_ttl


class AuthorityLabsPartnerApi(HTTPServiceClient):
    def __init__(self, api_key, account_id, url=None, **kwargs):
        url = url or 'http://api.authoritylabs.com'
        super(AuthorityLabsPartnerApi, self).__init__(
            url, params={'auth_token': api_key}, **kwargs)
        self.api_key = api_key
        self.account_id = account_id

    def get_account_status(self):
        return self.get('/account/{0}.json'.format(self.account_id)).json()

    def search_keyword(self, keyword, engine, locale, immediate=False):
        # TODO(zoidbergwill): validate engine + locale

        path = '/keywords%s' % ('/priority' if immediate else '')

        self.post(
            path,
            data={
                'keyword': keyword,
                'engine': engine,
                'locale': locale,
            })

    def get_results(self, keyword, engine, locale, rank_date):
        return self.get(
            '/keywords/get.json',
            params={
                'keyword': keyword,
                'response_format': 'json',
                'engine': engine,
                'locale': locale,
                'rank_date': rank_date,
            }).json()
