class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def get_sort_key(log: str):
            identifier, content = log.split(" ", maxsplit=1)
            if content[0].isalpha():
                return (0, content, identifier)
            else:
                return (1,)

        return sorted(logs, key=get_sort_key)
