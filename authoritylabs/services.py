# -*- coding: utf-8 -*-
from demands import HTTPServiceClient

from authoritylabs.utils import memoized_ttl


SUPPRESSED_LOCALES = [
    # en-gb is only supported by Bing, and they all have en-uk
    'en-gb',
]

INCONSISTENT_DESCRIPTIONS = {
    'en-ph': 'Philippines - English',
    'en-uk': 'United Kingdom - English',
    'en-za': 'South Africa - English',
    'nl-nl': 'Netherlands - Dutch',
    'pt-br': 'Brazil - Portuguese',
    'tr-tr': 'Turkey - Turkish',
}

INCONSISTENT_LOCALES = {
    'fi-fl': {
        'bing': 'fi-fi',
        'yahoo': 'fi-fl',
    },
    'no-no': {
        'bing': 'nb-no',
        'yahoo': 'no-no',
    },
    'pt-br-br': {
        'bing': 'pt-br',
        'yahoo': 'pt-br',
    },
    'zh-hk-hk': {
        'bing': 'zh-hk',
        'yahoo': 'zh-hk',
    },
}


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
        if engine != 'google' and locale in INCONSISTENT_LOCALES:
            engine_locale = INCONSISTENT_LOCALES[locale].get(engine)
            if engine_locale:
                locale = engine_locale

        if locale in self.get_supported_locales(engine):
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

    @memoized_ttl(ttl=86400)
    def get_supported_locales(self, engine):
        return self.get('supported/{0}.json'.format(engine)).json()['locales']
