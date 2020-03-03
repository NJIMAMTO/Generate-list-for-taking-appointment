#===============#特定のキーワードと該当する地域の電話アポリストを作るプログラム#===============#
from selenium import webdriver
import pandas as pd
import sys

class Scraping():
    def __init__(self, keyword, areaword):
        self.keyword = keyword
        self.areaword = areaword

    def open_browser(self):
        #スクレイピング用ブラウザを開く
        self.browser = webdriver.Chrome()
        self.browser.get("https://itp.ne.jp/keyword/?keyword={}&areaword={}".format(self.keyword,self.areaword))

    def show_more_btn_click(self):
        while True:
            elem = self.browser.find_element_by_id('__layout')
            try:
                elem = elem.find_element_by_class_name("o-result-article-readmore")
                show_more_btn = elem.find_element_by_class_name("u-hover")
                show_more_btn.click()
            #さらに表示するボタンが無くなったらループを抜ける
            except:
                return 0

    def get_store_list(self):
        try:
            list_store = self.browser.find_element_by_class_name('o-result-article-list')
            stores = list_store.find_elements_by_class_name('o-result-article-list__item')
        #該当する店舗がない場合に終了
        except:
            return -1

        self.name = []
        self.category = []
        self.phone_number = []
        self.address = []

        for store in stores:
            #店舗名を取得
            store_name = store.find_element_by_class_name("m-article-card__header__title__link")
            self.name.append(store_name.text)
            
            #店舗のカテゴリを取得
            store_category = store.find_element_by_class_name("m-article-card__header__category")
            self.category.append(store_category.text)
            
            #店舗の注釈（電話番号と住所）を取得
            store_captions = store.find_elements_by_class_name("m-article-card__lead__caption")
            
            #要素が3つある(電話番号が掲載されている場合)
            if len(store_captions) == 3:
                store_phone_number = store_captions[1]
                store_phone_number = store_phone_number.text.split(' ')
                self.phone_number.append(store_phone_number[1])

                store_address = store_captions[2]
                store_address = store_address.text.split('】')
                self.address.append(store_address[1])
                
            #要素が3つない(電話番号が掲載されていない場合)
            else:
                self.phone_number.append("電話番号が公開されていません")

                store_address = store_captions[1]
                store_address = store_address.text.split('】')
                self.address.append(store_address[1])

        return 0

    def output_CSV(self):
        #店舗リストをCSVファイルに出力する
        df = pd.DataFrame()

        df['店舗名'] = self.name
        df['カテゴリ'] = self.category
        df['電話番号'] = self.phone_number
        df['住所'] = self.address

        output_file = '電話アポ　{}の{}リスト.csv'.format(self.areaword, self.keyword) 
        df.to_csv(output_file, index=False, encoding='utf_8_sig')

        return output_file

    def output_dataframe(self):
        #店舗リストをデータフレームに引き渡す
        df = pd.DataFrame()

        df['店舗名'] = self.name
        df['カテゴリ'] = self.category
        df['電話番号'] = self.phone_number
        df['住所'] = self.address

        return df

    def close(self):
        self.browser.close()