class FileSystem:
    class File:
        __slots__ = ("is_file", "files", "content")
        def __init__(self):
            self.is_file = False
            self.files = {}
            self.content = ""
    
    __slots__ = ("_root",)

    def __init__(self):
        self._root = self.File()

    def ls(self, path: str) -> List[str]:
        files = []
        curr = self._root
        name = ""
        if path != "/":
            # traverse down to the bottom
            _, *nodes = path.split("/")
            for node in nodes:
                curr = curr.files[node]
                name = node
        if curr.is_file:
            return [name]
        files.extend(curr.files.keys())
        return sorted(files)

    def mkdir(self, path: str) -> None:
        _, *nodes = path.split("/")
        curr = self._root
        for node in nodes:
            if node not in curr.files:
                curr.files[node] = self.File()
            curr = curr.files[node]

    def addContentToFile(self, file_path: str, content: str) -> None:
        # traverse down to the bottom
        _, *nodes = file_path.split("/")
        curr = self._root
        for node in nodes:
            if node not in curr.files:
                curr.files[node] = self.File()
            curr = curr.files[node]
        
        if not curr.is_file:
            curr.is_file = True
            
        curr.content += content

    def readContentFromFile(self, file_path: str) -> str:
        # traverse down to the bottom
        _, *nodes = file_path.split("/")
        curr = self._root
        for node in nodes:
            curr = curr.files[node]
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
