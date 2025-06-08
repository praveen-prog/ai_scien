import requests

def search_arxiv(query, max_results=5):
    url = 'http://export.arxiv.org/api/query'
    params = {
        'search_query': f'all:{query}',
        'start': 0,
        'max_results': max_results
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # Parse the XML response
        import xml.etree.ElementTree as ET
        root = ET.fromstring(response.text)
        entries = root.findall('{http://www.w3.org/2005/Atom}entry')
        results = []
        for entry in entries:
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            link = entry.find('{http://www.w3.org/2005/Atom}id').text
            results.append({'title': title, 'link': link})
        return results
    else:
        return []

# Example usage:
papers = search_arxiv("physics")

