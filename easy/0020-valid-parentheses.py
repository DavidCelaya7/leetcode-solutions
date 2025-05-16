class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Lista usada como pila (estructura LIFO) para gestionar los paréntesis de apertura

        # Diccionario que mapea los paréntesis de cierre con su correspondiente apertura
        mapping = {")": "(", "}": "{", "]": "["}

        # Iteramos sobre cada carácter en la cadena
        for c in s:
            if c in mapping:  # Si el carácter es un paréntesis de cierre
                # Verificamos dos cosas:
                # 1. Que la pila no esté vacía (para evitar errores y validar que haya algo que cerrar)
                # 2. Que el último elemento de la pila coincida con el par correspondiente
                if not stack or stack[-1] != mapping[c]:
                    return False  # La cadena está mal formada, regresamos False
                stack.pop()  # Eliminamos el último paréntesis abierto porque ya fue cerrado correctamente
            else:
                # Si el carácter no está en el diccionario, es un paréntesis de apertura
                # Lo agregamos a la pila para esperar a que sea cerrado más adelante
                stack.append(c)

        # Al final, si la pila está vacía, significa que todos los paréntesis se cerraron correctamente
        return not stack

# Bloque de prueba
if __name__ == "__main__":
    sol = Solution()
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    
    for s in test_cases:
        print(f"{s} -> {sol.isValid(s)}")
