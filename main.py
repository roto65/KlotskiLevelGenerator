import json

def main(): 

    levelList = []

    with open('levels.json', 'r') as file:
        levels = json.load(file)

        levelList = levels['levels']
    
    for level in levelList:
        saveLevel(level)

def saveLevel(level):

    filename = 'levels/' + f"{level['level']:03d}" + '.json'

    board = level['board']
    del level['board']

    level['blocks'] = evalBlocks(board)


    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(level, file, ensure_ascii = False, indent = 2)

def evalBlocks(boardString):

    board = list(boardString)

    columns = 4

    blocks = []

    for i in range(0, len(board)):
        c = board[i]

        if c == 'z' or c == '@':
            continue

        pos = {
            'x': -1,
            'y': -1
        }

        block = {
            'pos': pos,
            'blockType': 'none'
        }

        if i < len(board) - 4:
            if c == board[i + 4] and c == board[i + 1]:

                block['blockType'] = 'LARGE'
                
                pos['x'] = i % columns
                pos['y'] = i // columns

                block['pos'] = pos

                board[i] = 'z'
                board[i + 1] = 'z'
                board[i + 4] = 'z'
                board[i + 5] = 'z' 
                
                blocks.append(block)
                continue
            elif c == board[i + 4]:
                block['blockType'] = 'WIDE_VERTICAL'
                
                pos['x'] = i % columns
                pos['y'] = i // columns

                block['pos'] = pos

                board[i] = 'z'
                board[i + 4] = 'z' 

                
                blocks.append(block)
                continue
        if i < len(board) - 1:
            if c == board[i + 1]:

                block['blockType'] = 'WIDE_HORIZONTAL'
                
                pos['x'] = i % columns
                pos['y'] = i // columns

                block['pos'] = pos

                board[i] = 'z'
                board[i + 1] = 'z' 
                
                blocks.append(block)
                continue
        
        block['blockType'] = 'SMALL'
        
        pos['x'] = i % columns
        pos['y'] = i // columns

        block['pos'] = pos

        board[i] = 'z' 
        
        blocks.append(block)

    return blocks


if __name__ == "__main__":
    main()