def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    safety = ["",
             " conglatuation! ",
             "|               ",
             "|               ",
             "|       \o/     ",
             "|        |      ",
             "|_______/_\______"
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:#ハングマンは８行
        print("\n")
        msg = "Guess a letter 残り{}回 :".format(len(stages)-wrong-1)
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'#.indexの性能により，仮にレターが２つ以上重複していた場合，検索が一回のみ有効になるため，これを避けるため正解（検索したワード）を違うワードに置き換えている
        else:
            wrong += 1
        print((" ".join(board)))#joinで配列要素全てを合体
        e = wrong + 1
        print("\n".join(stages[0: e]))#ハングマン要素連結(スライスの特性により，プラス１している)
        if "__" not in board:
            print("\n".join(safety))
            print("You win!")
            print(" ".join(board))#joinで配列要素全てを合体
            win = True
            break
    if not win:
        stages[2]="|    game over  "
        print("\n".join(stages))
        print("You lose! It was {}.".format(word))

hangman("cat")