# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # Фиктивный узел для начала результирующего списка
        current = dummy  # Текущий узел
        carry = 0  # Перенос

        while l1 or l2 or carry:
            # Получаем значения из l1 и l2, если они существуют
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Сумма текущих значений и переноса
            total = val1 + val2 + carry
            carry = total // 10  # Вычисляем новый перенос
            digit = total % 10  # Вычисляем текущую цифру

            # Создаём новый узел с полученной цифрой
            current.next = ListNode(digit)
            current = current.next

            # Переходим к следующим узлам, если они существуют
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Возвращаем список, начиная после фиктивного узла
# Функция для преобразования списка в связанный список
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Функция для вывода связного списка
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Создание связных списков для примера
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

# Решение задачи
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Вывод результата
print(print_linked_list(result))  # Ожидаемый результат: [7, 0, 8]