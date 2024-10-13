# 此指令用於從類型庫匯入List資料類型，以確定變數和參數的類型   
from typing import List

#定義了一個名為 countLetters 的函數，countLetters 函數接受單一參數、句子，並使用資料型態 str 進行註釋
def countLetters(sentence: str) -> List[int]:

    #letterCount：List[int]：是 letterCount 變數的資料型別註解。指示 letterCount 是一個包含整數值的清單。用 26 個元素初始化列表，每個元素的值為 0
    letterCount: List[int] = [0] * 26

    #此命令列有助於對字串「sentence」的每個字元執行特定操作（在循環內定義）。
    for char in sentence:

        #檢查字串中的目前字元是否為字母。如果該字元是字母，則將執行 if 區塊中的下一行程式碼。如果字元不是字母，則 if 內的語句區塊將被忽略。
        if char.isalpha():

            #此命令列將 char 字元轉換為表示其在字母表中的位置的數字（從 0 開始）。
            index = ord(char) - ord('a')
            
            #命令列用於統計字串中每個字母出現的次數。
            letterCount[index] += 1

    #該命令將傳回一個列表，其中包含輸入字串中每個字母的出現次數。
    return letterCount

#當您還不想編寫程式碼或想跳過程式的特定部分而不引起錯誤時，可以使用 pass 關鍵字。
pass

#此函數接受表示字母出現次數的整數列表並列印該資訊。它不會傳回任何值，而只是在螢幕上執行列印操作。
def printLetterCount(letterCount: List[int]) -> None:

    #命令列設定了26次循環，i的值分別為0到25。
    for i in range(26):

        #檢查 letterCount 清單中位置 i 處字母的出現次數是否大於 0
        if letterCount[i] > 0:

            #命令列用於列印letterCount清單中每個字母出現的次數
            print(f"{chr(i + ord('a'))}: {letterCount[i]}")
pass

#此命令列會建立一個包含字串「this is an apple」的 inputSentence 變數
inputSentence: str = "this is an apple"

#命令列使用 inputSentence 字串呼叫 countLetters 函數，接收傳回值作為字串中字母出現次數的列表，並將其指派給 letterCount 變數以供進一步使用。
letterCount: List[int] = countLetters(inputSentence)

#命令列列印字串中每個字母出現的次數。
printLetterCount(letterCount)