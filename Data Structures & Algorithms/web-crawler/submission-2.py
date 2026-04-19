# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # get the hostname from a url
        def get_hostname(url: str) -> str:
            return url_parser(url)[0]

        # returns hostname, path. we may assume all http:// protocol, no port
        def url_parser(url: str) -> List[str]:
            hostname, *path = url[7:].split("/", 1)
            return hostname, path
        
        start_hostname = get_hostname(startUrl)
        visited = set()
        
        queue = deque([startUrl])
        while queue:
            qlen = len(queue)
            for _ in range(qlen):
                url = queue.popleft()
                visited.add(url)

                for link in htmlParser.getUrls(url):
                    hostname = get_hostname(link)
                    if link in visited or hostname != start_hostname:
                        continue
                    queue.append(link)
        return list(visited)
        