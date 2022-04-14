class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        if not properties:
            return 0

        properties.sort(key=lambda x: (x[0], -x[1]))

        stack = []
        size = len(properties)

        for i in range(size):
            defen = properties[i][-1]
            if not stack:
                stack.append(defen)
            else:
                while stack and defen > stack[-1]:
                    stack.pop()

                stack.append(defen)

        return size - len(stack)
