import httpx
import typing as t
GEOHUB_DATA_URL = 'https://dev.undpgeohub.org/api/datasets'


def search_datasets(url=GEOHUB_DATA_URL, query=None) -> t.Dict[str,t.List]:
    """
    Retrieves links from Geohub datasets using a query word or expression
    :param url: str, https://geohub.data.undp.org/api/datasets
    :param query:
    :return: dict where the key is the dataset id and the value is a list of various resources as url's
             associated with this dataset
    """
    assert query not in [None,''], f'Invalid query={query}'
    rdict = dict()
    with httpx.Client() as client:
        uri = f'{url}?query={query}'
        resp = client.get(uri)
        data = resp.json()
        for feature in data['features']:
            feat_props = feature['properties']
            dataset_id = feat_props['id']
            rdict[dataset_id] = feat_props['links']
    return rdict


if __name__ == '__main__':
    results = search_datasets(query='bangladesh buildings')
    for ds_id, links in results.items():
        for l in links:
            print(l)


