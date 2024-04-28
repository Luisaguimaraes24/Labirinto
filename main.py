import random
from collections import deque
import time

def generate_maze():
    maze = [[1 for _ in range(15)] for _ in range(15)]  # matriz 15 por 15

    # posição de entrada e saída
    entry_position = (0, random.choice([1, 13]))  # Entrada na primeira linha, em uma posição aleatória
    exit_position = (14, random.choice([1, 13]))  # Saída na última linha, em uma posição aleatória
    maze[entry_position[0]][entry_position[1]] = 2  # Marca a entrada
    maze[exit_position[0]][exit_position[1]] = 3  # Marca a saída

    #caminho entre a entrada e a saída
    current_position = (1, entry_position[1])  # Define a posição atual como a próxima à entrada
    maze[current_position[0]][current_position[1]] = 0  # Marca a posição atual como visitada
    path = [current_position]  # Lista para armazenar o caminho principal

    while current_position[0] != exit_position[0] - 1 or current_position[1] != exit_position[1]:  
        # Enquanto não estiver uma linha acima da saída ou na mesma coluna da saída
        possible_moves = []

        # Verifica os movimentos possíveis: norte, sul, leste, oeste
        if current_position[0] > 0 and maze[current_position[0] - 1][current_position[1]] == 1:
            possible_moves.append((-1, 0))  # Norte
        if current_position[0] < 14 and maze[current_position[0] + 1][current_position[1]] == 1:
            possible_moves.append((1, 0))  # Sul
        if current_position[1] > 0 and maze[current_position[0]][current_position[1] - 1] == 1:
            possible_moves.append((0, -1))  # Oeste
        if current_position[1] < 14 and maze[current_position[0]][current_position[1] + 1] == 1:
            possible_moves.append((0, 1))  # Leste

        if not possible_moves:  # Se não houver movimentos possíveis
            return generate_maze()  # Reinicia a geração do labirinto

        # Escolhe um movimento aleatório e move para a próxima posição
        move = random.choice(possible_moves)
        current_position = (current_position[0] + move[0], current_position[1] + move[1])
        maze[current_position[0]][current_position[1]] = 0  # Marca a próxima posição como visitada
        path.append(current_position)  # Adiciona a próxima posição ao caminho principal

    # Adiciona becos sem saída ao caminho principal
    num_dead_ends = random.randint(7, 8)  # Define o número de becos sem saída
    for _ in range(num_dead_ends):
        # Escolhe uma posição aleatória ao longo do caminho principal
        position_index = random.randint(1, len(path) - 2)
        position = path[position_index]

        # Verifica se a posição escolhida já não é um beco sem saída
        if maze[position[0]][position[1]] == 0:
            continue

        # Bloqueia a posição escolhida como um beco sem saída
        maze[position[0]][position[1]] = 1

    return maze

def depth_first_search(maze, current_position, exit_position, visited):
    if current_position == exit_position:  # Se encontrou a saída, retorna True
        return True

    x, y = current_position
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Direções: leste, oeste, sul, norte

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == 0 and (next_x, next_y) not in visited:
            visited.add((next_x, next_y))
            maze[next_x][next_y] = 4  # Marca como visitado
            print("\nPasso:")
            visualize_search(maze)
            time.sleep(0.5)
            if depth_first_search(maze, (next_x, next_y), exit_position, visited):
                return True
            maze[next_x][next_y] = 0  # Desmarca se não levar à saída

    return False

def breadth_first_search(maze, entry_position, exit_position):
    queue = deque([(entry_position, [])])  # Armazena o caminho percorrido junto com a posição
    visited = set()
    visited.add(entry_position)

    while queue:
        current_position, path = queue.popleft()
        x, y = current_position
        if current_position == exit_position:  # Se encontrou a saída, retorna o caminho percorrido
            return path + [exit_position]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Direções: leste, oeste, sul, norte

        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == 0 and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                queue.append(((next_x, next_y), path + [(next_x, next_y)]))
                maze[next_x][next_y] = 4  # Marca como visitado
                print("\nPasso:")
                visualize_search(maze)
                time.sleep(0.5)

    return None

def visualize_search(maze):
    for row in maze:
        print(" ".join(map(str, row)))

def visualize_dfs(maze, entry_position, exit_position):
    print("Labirinto inicial:")
    visualize_search(maze)
    print("\nBusca em profundidade:")

    visited = set()
    visited.add(entry_position)
    if depth_first_search(maze, entry_position, exit_position, visited):
        print("Saída encontrada:")
    else:
        print("Não foi possível encontrar a saída por busca de profundidade.")
    visualize_search(maze)

def visualize_bfs(maze, entry_position, exit_position):
    print("Labirinto inicial:")
    visualize_search(maze)
    print("\nBusca em largura:")

    shortest_path = breadth_first_search(maze, entry_position, exit_position)
    if shortest_path:
        for position in shortest_path:
            x, y = position
            maze[x][y] = 5  # Marca o caminho mais curto como 5
        print("Saída encontrada:")
    else:
        print("Não foi possível encontrar a saída por busca de largura")
    visualize_search(maze)

# Exemplo de uso
if __name__ == "__main__":
    maze = generate_maze()
    entry_position = (0, maze[0].index(2))
    exit_position = (14, maze[14].index(3))

    visualize_dfs(maze, entry_position, exit_position)
    print("\n\n")
    visualize_bfs(maze, entry_position, exit_position)

