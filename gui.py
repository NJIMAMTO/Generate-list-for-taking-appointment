import PySimpleGUI as sg
import pandas as pd

class Scraping_GUI():
    def __init__(self):
        #  セクション1 - オプションの設定と標準レイアウト
        sg.theme('Dark Blue 3')

        self.layout = [
            [sg.Text('Python GUI')],
            [sg.Text('キーワード', size=(15, 1)), sg.InputText('〇〇屋さん')],
            [sg.Text('エリアワード', size=(15, 1)), sg.InputText('△△△△村')],
            [sg.Submit(button_text='検索する')]
        ]

    def generate_window(self):
        # セクション 2 - ウィンドウの生成
        self.window = sg.Window('入力画面', self.layout)

    def event_loop(self):
        # セクション 3 - イベントループ
        while True:
            event, values = self.window.read()

            if event is None:
                print('exit')
                break

            if event == '検索する':
                if values[0] == '' or values[1] == '':
                    show_message = 'なにも入力されていません！'
                    sg.popup(show_message)

                else:
                    # セクション 4 - ウィンドウの破棄と終了
                    self.window.close()
                    #キーワードとエリアワードを返す
                    return values[0], values[1]

    def store_is_none(self):
        sg.popup("該当する店舗がありませんでした")

class Output_GUI():
    def __init__(self, df):
        #CSVファイルを読み込む
        #df = pd.read_csv(file_name)
        header_list =  list(df.columns)
        data = df.values.tolist()

        #  セクション1 - オプションの設定と標準レイアウト
        sg.theme('Dark Blue 3')

        self.layout = [[sg.Table(values=data,
                            headings=header_list,
                            max_col_width=25,
                            auto_size_columns=True,
                            justification='right',
                            # alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]

    def output(self):
        # セクション 2 - ウィンドウの生成
        self.window = sg.Window('出力結果', self.layout)

        # セクション 3 - イベントループ
        while True:
            event, _ = self.window.read()

            #Xボタンが押されたらループを終了する
            if event is None:
                break

        # セクション 4 - ウィンドウの破棄と終了
        self.window.close()