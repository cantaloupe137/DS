class BlockWorld:
    def __init__(self, n):
        """初始化積木世界"""
        self.n = n
        # 每個積木的位置：[堆疊編號, 在堆疊中的位置]
        self.positions = [[i, 0] for i in range(n)]
        # 每個堆疊中的積木
        self.stacks = [[i] for i in range(n)]

    def return_blocks_above(self, stack_id, position):
        """將指定位置以上的積木歸位到原來的堆疊"""
        stack = self.stacks[stack_id]
        # 從上到下處理積木
        for i in range(len(stack) - 1, position, -1):
            block_id = stack[i]
            # 將積木放回原來的堆疊
            self.stacks[block_id].append(block_id)
            self.positions[block_id] = [
                block_id, len(self.stacks[block_id]) - 1]
        # 移除已歸位的積木
        self.stacks[stack_id] = stack[:position + 1]

    def move_onto(self, a, b):
        """將積木a移動到積木b上面，並將兩者上方的積木歸位"""
        if self.positions[a][0] == self.positions[b][0]:
            return  # 同一個堆疊，無需操作

        # 將a上方的積木歸位
        self.return_blocks_above(self.positions[a][0], self.positions[a][1])
        # 將b上方的積木歸位
        self.return_blocks_above(self.positions[b][0], self.positions[b][1])

        # 移動a到b上面
        self._move_block(a, b)

    def move_over(self, a, b):
        """將積木a移動到積木b所在的堆疊頂部，並將a上方的積木歸位"""
        if self.positions[a][0] == self.positions[b][0]:
            return  # 同一個堆疊，無需操作

        # 將a上方的積木歸位
        self.return_blocks_above(self.positions[a][0], self.positions[a][1])

        # 移動a到b所在的堆疊頂部
        self._move_block(a, b)

    def pile_onto(self, a, b):
        """將積木a及其上方的積木移動到積木b上面，並將b上方的積木歸位"""
        if self.positions[a][0] == self.positions[b][0]:
            return  # 同一個堆疊，無需操作

        # 將b上方的積木歸位
        self.return_blocks_above(self.positions[b][0], self.positions[b][1])

        # 移動a及其上方的積木到b上面
        self._move_pile(a, b)

    def pile_over(self, a, b):
        """將積木a及其上方的積木移動到積木b所在的堆疊頂部"""
        if self.positions[a][0] == self.positions[b][0]:
            return  # 同一個堆疊，無需操作

        # 移動a及其上方的積木到b所在的堆疊頂部
        self._move_pile(a, b)

    def _move_block(self, a, b):
        """移動單個積木a到積木b所在的堆疊頂部"""
        # 從原堆疊移除a
        old_stack_id = self.positions[a][0]
        old_pos = self.positions[a][1]
        self.stacks[old_stack_id].pop(old_pos)

        # 更新原堆疊中a後面積木的位置
        for i in range(old_pos, len(self.stacks[old_stack_id])):
            self.positions[self.stacks[old_stack_id][i]][1] = i

        # 將a添加到新堆疊
        new_stack_id = self.positions[b][0]
        self.stacks[new_stack_id].append(a)
        self.positions[a] = [new_stack_id, len(self.stacks[new_stack_id]) - 1]

    def _move_pile(self, a, b):
        """移動積木a及其上方的所有積木到積木b所在的堆疊頂部"""
        old_stack_id = self.positions[a][0]
        old_pos = self.positions[a][1]
        new_stack_id = self.positions[b][0]

        # 獲取要移動的積木列表
        blocks_to_move = self.stacks[old_stack_id][old_pos:]

        # 從原堆疊移除這些積木
        self.stacks[old_stack_id] = self.stacks[old_stack_id][:old_pos]

        # 將積木添加到新堆疊
        for block_id in blocks_to_move:
            self.stacks[new_stack_id].append(block_id)
            self.positions[block_id] = [new_stack_id,
                                        len(self.stacks[new_stack_id]) - 1]

    def print_state(self):
        """打印當前狀態"""
        for i in range(self.n):
            print(f"{i}:", end="")
            for block in self.stacks[i]:
                print(f" {block}", end="")
            print()


def main():
    while True:
        try:
            n = int(input())
            world = BlockWorld(n)

            while True:
                command = input().strip()
                if command == "quit":
                    break

                parts = command.split()
                if len(parts) != 4:
                    continue

                action, a, preposition, b = parts
                a, b = int(a), int(b)

                # 檢查參數有效性
                if a == b or a >= n or b >= n or a < 0 or b < 0:
                    continue

                # 執行操作
                if action == "move" and preposition == "onto":
                    world.move_onto(a, b)
                elif action == "move" and preposition == "over":
                    world.move_over(a, b)
                elif action == "pile" and preposition == "onto":
                    world.pile_onto(a, b)
                elif action == "pile" and preposition == "over":
                    world.pile_over(a, b)

            world.print_state()

        except EOFError:
            break
        except ValueError:
            break


if __name__ == "__main__":
    main()
